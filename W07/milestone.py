from PIL import Image

image_original = Image.open('penguin.jpg')

width, height = image_original.size
pixels_original = image_original.load()

def modify_pixels(x_axis, y_axis, red, green, blue):
    for i in range(0, 10):
        for j in range(0, 10):
            pixels_original[x_axis + i, y_axis + j] = red, green, blue

modify_pixels(100, 200, 255, 0, 255)
modify_pixels(200, 200, 193, 45, 230)
modify_pixels(300, 200, 7, 210, 183)
modify_pixels(400, 200, 48, 194, 39)
modify_pixels(500, 200, 149, 23, 1)

image_original.show()
image_original.save("penguin_modified.jpg")

