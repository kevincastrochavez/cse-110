from PIL import Image

image_original = Image.open('penguin.jpg')
image_replace = Image.open('snowscape.jpg')

pixels_original = image_original.load()
pixels_replace = image_replace.load()
width, height = image_original.size

def modify_pixels(width, height, image, image_replace):
    for i in range(0, width):
        for j in range(0, height):
            green_color = (44, 207, 64)

            if image[i, j] == green_color:
                image[i, j] = image_replace[i, j]
        
modify_pixels(width, height, pixels_original, pixels_replace)

image_original.show()
image_original.save("penguin_modified.jpg")

