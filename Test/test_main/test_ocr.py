from pytesser3 import *

im = Image.open("test.jpg")
if im:
    print(im)
    text_code = image_to_string(im)
    print(text_code)