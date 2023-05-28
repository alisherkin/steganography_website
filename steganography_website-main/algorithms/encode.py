import wave
import numpy as np
import random
import zipfile
import os

def generate_key():
    """
    Generates a random 5-digit key for encoding message.
    """
    return random.randint(10000, 99999)


def encode_lsb_audio(audio_file_path, message):
    key = generate_key()
    print("Key: ", key)
    with open("./algorithms/img/key.txt", 'w') as file:
        file.write(str(key))
    audio = wave.open(audio_file_path, 'r')
    params = audio.getparams()
    frames = audio.readframes(audio.getnframes())

    audio_array = np.frombuffer(frames, dtype=np.int16)
    message_binary = ''.join(format(ord(c), '08b') for c in message)

    key_binary = format(key, '020b')  # Convert key to 20-bit binary representation

    message_binary = key_binary + message_binary  # Append key binary to message binary
    message_binary += '00000000'

    if len(message_binary) > len(audio_array):
        raise ValueError('Message is too long to fit in the audio file')

    audio_array_copy = audio_array.copy()
    audio_array_copy.setflags(write=True)

    for i in range(len(message_binary)):
        audio_array_copy[i] &= ~1  # Clear the least significant bit
        audio_array_copy[i] |= int(message_binary[i])

    encoded_frames = audio_array_copy.tobytes()

    encoded_audio = wave.open('./algorithms/img/encoded_audio.wav', 'w')
    encoded_audio.setparams(params)
    encoded_audio.writeframes(encoded_frames)
    encoded_audio.close()

    with zipfile.ZipFile("./algorithms/img/encoded_result.zip", 'w') as zip_file:
        # Add the audio file to the zip archive
        zip_file.write("./algorithms/img/encoded_audio.wav", os.path.basename("./algorithms/img/encoded_audio.wav"))

        # Add the text file to the zip archive
        zip_file.write("./algorithms/img/key.txt", os.path.basename("./algorithms/img/key.txt"))

    print('Message successfully encoded in audio file.')


def decode_lsb_audio(encoded_audio_file_path, key):
    encoded_audio = wave.open(encoded_audio_file_path, 'r')
    params = encoded_audio.getparams()
    frames = encoded_audio.readframes(encoded_audio.getnframes())

    encoded_audio_array = np.frombuffer(frames, dtype=np.int16)

    key_binary = ''
    for sample in encoded_audio_array[:20]:  # Extract first 20 samples for key binary
        key_binary += str(sample & 1)

    extracted_key = int(key_binary, 2)  # Convert key binary to integer

    if str(key) != str(extracted_key):
        print("Key does not match. Decoding failed.")
        return None

    message_binary = ''
    for sample in encoded_audio_array[20:]:  # Start from 21st sample for message binary
        message_binary += str(sample & 1)

    message = ''
    for i in range(0, len(message_binary), 8):
        byte = message_binary[i:i + 8]
        if byte == '00000000':
            break
        char = chr(int(byte, 2))
        message += char

    return message.strip()


if __name__ == '__main__':
    encode_lsb_audio("img/audio.wav", input("Message:"))
    print(decode_lsb_audio("img/encoded_audio.wav"))
