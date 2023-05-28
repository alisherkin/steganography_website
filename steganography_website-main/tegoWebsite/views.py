from django.shortcuts import render
from algorithms.encode import encode_lsb_audio
from algorithms.encode import decode_lsb_audio
from algorithms.encode_video import encode_lsb_video
from algorithms.encode_video import decode_lsb_video
from algorithms.encode_img import encode_lsb_image
from algorithms.encode_img import decode_lsb_image
from django.http import HttpResponse
def my_view(request):
    return render(request, 'index.html')

def encode_audio_view(request):
    if request.method == 'POST':
        # Get the audio file and message from the POST request
        audio_file = request.FILES['audio_file']
        message = request.POST['message']
        print(audio_file)


        # Call the encode_lsb_audio function to encode the message in the audio file
        encode_lsb_audio(audio_file, message)

        # Prepare the response for file download
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="encoded_result.zip"'

        # Read the encoded audio file and write it to the response
        with open('./algorithms/img/encoded_result.zip', 'rb') as file:
            response.write(file.read())

        # Return the response to initiate the file download
        return response

    # Render the template with a form to upload an audio file and enter a message
    return render(request, 'encode.html')
def decode_audio_view(request):
    if request.method == 'POST':
        # Get the encoded audio file from the POST request
        encoded_audio_file = request.FILES['encoded_audio_file']
        key = request.POST['key']


        # Call the decode_lsb_audio function to decode the message from the encoded audio file
        message = decode_lsb_audio(encoded_audio_file,key)

        # Render the template with the decoded message
        return render(request, 'decode.html', {'message': message})

    # Render the template with a form to upload an encoded audio file
    return render(request, 'decode.html')

def encode_audio_remake_view(request):
    if request.method == 'POST':
        # Get the audio file and message from the POST request
        audio_file = request.FILES['audio_file']
        message = request.POST['message']
        print(audio_file)


        # Call the encode_lsb_audio function to encode the message in the audio file
        encode_lsb_audio(audio_file, message)

        # Prepare the response for file download
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="encoded_result.zip"'

        # Read the encoded audio file and write it to the response
        with open('./algorithms/img/encoded_result.zip', 'rb') as file:
            response.write(file.read())

        # Return the response to initiate the file download
        return response

    # Render the template with a form to upload an audio file and enter a message
    return render(request, 'encode_remake.html')
def decode_audio_remake_view(request):
    if request.method == 'POST':
        # Get the encoded audio file from the POST request
        encoded_audio_file = request.FILES['encoded_audio_file']
        key = request.POST['key']


        # Call the decode_lsb_audio function to decode the message from the encoded audio file
        message = decode_lsb_audio(encoded_audio_file,key)

        # Render the template with the decoded message
        return render(request, 'decode_remake.html', {'message': message})

    # Render the template with a form to upload an encoded audio file
    return render(request, 'decode_remake.html')

def encode_video_view(request):
    if request.method == 'POST':
        # Get the audio file and message from the POST request
        video_file = request.FILES['video_file']
        video_file_path = f"./algorithms/img/{video_file}"
        message = request.POST['message']
        print(video_file)
        # Call the encode_lsb_audio function to encode the message in the audio file
        encode_lsb_video(video_file_path, message)

        # Prepare the response for file download
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="encoded_video_result.zip"'

        # Read the encoded audio file and write it to the response
        with open('./algorithms/img/encoded_video_result.zip', 'rb') as file:
            response.write(file.read())

        # Return the response to initiate the file download
        return response

    # Render the template with a form to upload an audio file and enter a message
    return render(request, 'encode_video.html')
def decode_video_view(request):
    if request.method == 'POST':
        # Get the encoded audio file from the POST request
        encoded_video_file = request.FILES['encoded_video_file']
        encoded_video_file_path = f"./algorithms/img/{encoded_video_file}"
        key = request.POST['key']


        # Call the decode_lsb_audio function to decode the message from the encoded audio file
        message = decode_lsb_video(encoded_video_file_path,key)

        # Render the template with the decoded message
        return render(request, 'decode.html', {'message': message})

    # Render the template with a form to upload an encoded audio file
    return render(request, 'decode_video.html')


def encode_video_remake_view(request):
    if request.method == 'POST':
        # Get the audio file and message from the POST request
        video_file = request.FILES['video_file']
        video_file_path = f"./algorithms/img/{video_file}"
        message = request.POST['message']
        print(video_file)
        # Call the encode_lsb_audio function to encode the message in the audio file
        encode_lsb_video(video_file_path, message)

        # Prepare the response for file download
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="encoded_video_result.zip"'

        # Read the encoded audio file and write it to the response
        with open('./algorithms/img/encoded_video_result.zip', 'rb') as file:
            response.write(file.read())

        # Return the response to initiate the file download
        return response

    # Render the template with a form to upload an audio file and enter a message
    return render(request, 'encode_video_remake.html')
def decode_video_remake_view(request):
    if request.method == 'POST':
        # Get the encoded audio file from the POST request
        encoded_video_file = request.FILES['encoded_video_file']
        encoded_video_file_path = f"./algorithms/img/{encoded_video_file}"
        key = request.POST['key']


        # Call the decode_lsb_audio function to decode the message from the encoded audio file
        message = decode_lsb_video(encoded_video_file_path,key)

        # Render the template with the decoded message
        return render(request, 'decode_video_remake.html', {'message': message})

    # Render the template with a form to upload an encoded audio file
    return render(request, 'decode_video_remake.html')


def encode_image_view(request):
    if request.method == 'POST':
        # Get the audio file and message from the POST request
        image_file = request.FILES['image_file']
        image_file_path = f"./algorithms/img/{image_file}"
        message = request.POST['message']
        print(image_file)
        # Call the encode_lsb_audio function to encode the message in the audio file
        encode_lsb_image(image_file_path, message)

        # Prepare the response for file download
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="encoded_image_result.zip"'

        # Read the encoded audio file and write it to the response
        with open('./algorithms/img/encoded_image_result.zip', 'rb') as file:
            response.write(file.read())

        # Return the response to initiate the file download
        return response

    # Render the template with a form to upload an audio file and enter a message
    return render(request, 'encode_image.html')
def decode_image_view(request):
    if request.method == 'POST':
        # Get the encoded audio file from the POST request
        encoded_image_file = request.FILES['encoded_image_file']
        encoded_image_file_path = f"./algorithms/img/{encoded_image_file}"
        key = request.POST['key']


        # Call the decode_lsb_audio function to decode the message from the encoded audio file
        message = decode_lsb_image(encoded_image_file_path,key)

        # Render the template with the decoded message
        return render(request, 'decode.html', {'message': message})

    # Render the template with a form to upload an encoded audio file
    return render(request, 'decode_image.html')

def encode_image_remake_view(request):
    if request.method == 'POST':
        # Get the audio file and message from the POST request
        image_file = request.FILES['image_file']
        image_file_path = f"./algorithms/img/{image_file}"
        message = request.POST['message']
        print(image_file)
        # Call the encode_lsb_audio function to encode the message in the audio file
        encode_lsb_image(image_file_path, message)

        # Prepare the response for file download
        response = HttpResponse(content_type='application/octet-stream')
        response['Content-Disposition'] = 'attachment; filename="encoded_image_result.zip"'

        # Read the encoded audio file and write it to the response
        with open('./algorithms/img/encoded_image_result.zip', 'rb') as file:
            response.write(file.read())

        # Return the response to initiate the file download
        return response

    # Render the template with a form to upload an audio file and enter a message
    return render(request, 'encode_image_remake.html')
def decode_image_remake_view(request):
    if request.method == 'POST':
        # Get the encoded audio file from the POST request
        encoded_image_file = request.FILES['encoded_image_file']
        encoded_image_file_path = f"./algorithms/img/{encoded_image_file}"
        key = request.POST['key']


        # Call the decode_lsb_audio function to decode the message from the encoded audio file
        message = decode_lsb_image(encoded_image_file_path,key)

        # Render the template with the decoded message
        return render(request, 'decode_image_remake.html', {'message': message})

    # Render the template with a form to upload an encoded audio file
    return render(request, 'decode_image_remake.html')