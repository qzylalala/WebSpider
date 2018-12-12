import tesserocr
from PIL import Image


image = Image.open('code.jpg')
result = tesserocr.image_to_text(image)
print(result) 