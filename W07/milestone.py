# This line imports or includes the library we will need
from PIL import Image

image_original = Image.open('penguin.jpg')

width, height = image_original.size
pixels_original = image_original.load()

r, g, b = pixels_original[100, 200]

print(r)
print(g)
print(b)

for i in range(0, 100):
    for j in range(0, 100):
        pixels_original[100 + i, 200 + j] = 255, 0, 255

image_original.show()
image_original.save("penguin_modified.jpg")