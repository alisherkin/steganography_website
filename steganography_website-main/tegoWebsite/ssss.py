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