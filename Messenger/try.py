import base64

INPUT = r"C:\Users\princess\Downloads\david.jpg"
OUTPUT = r"C:\Users\princess\Downloads\david2.jpg"


image = open(INPUT, 'rb')
image_read = image.read()
image_64_encode = base64.encodebytes(image_read)
image_64_decode = base64.decodebytes(image_64_encode)
image_result = open(OUTPUT, 'wb')
image_result.write(image_64_decode)
