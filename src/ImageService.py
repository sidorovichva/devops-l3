from PIL import Image
import random


def create_image():
    width, height = 200, 200
    image = Image.new("RGB", (width, height), "white")
    for x in range(width):
        for y in range(height):
            color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            image.putpixel((x, y), color)
    image.show()
    return image
