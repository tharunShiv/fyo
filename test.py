import base64
with open("testimage.jpg", "rb") as img_file:
    my_string = base64.b64encode(img_file.read())

print(len(my_string))
