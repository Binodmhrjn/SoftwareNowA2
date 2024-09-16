import time
from PIL import Image
current_time = int(time.time())
generated_number = (current_time % 100) +50

if generated_number % 2 == 0:
    generated_number += 10

n = generated_number
print("Generated number =", n)

image = Image.open(r"C:\Users\thapa\Downloads\Assignment 2\chapter1.jpg")
image.show()

image = image.convert('RGB')
pixels = image.load()
width, height = image.size
red_sum = 0

for x in range(width):
    for y in range(height):
        r, g, b = pixels [x,y]
        pixels[x,y] = (r+n, g+n, b+n)
        r, g, b = pixels [x,y]
        red_sum += r
image.save(r"C:\Users\thapa\Downloads\Assignment 2\chapter1Out.jpg")
print("Total number of red pixels in new image =", red_sum)
image.show()