# This line imports or includes the library we will need
from PIL import Image

image_original = Image.open('penguin.jpg')

width, height = image_original.size
pixels_original = image_original.load()
r, g, b = pixels_original[100, 200]
print(r)
print(g)
print(b)

image_original.show()