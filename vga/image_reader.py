# based off of ben eater's python program from "World's worst video card? The exciting conclusion"
from PIL import Image
import os
print(os.listdir('vga'))

image = Image.open("vga/characters.png")
pixels = image.load()
out_file = open("characters.bin", "wb")
data = bytearray([])

for z in range(255):
    for y in range(8):
        temp = 0
        for x in range(8):
            if (pixels[z*8 + (8-x), y] == 0 or pixels[z*8 + (8-x), y] == 1):
                print(pixels[z*8 + (8-x), y], end="")
                temp =2*temp
            else:
                print(pixels[z*8 + (8-x), y], end="")
                temp =2*temp + 1
        print("--")
        print("--")
        print(hex(temp))
        data.append(temp)
    print("--------------")


with open("characters.bin", "wb") as file:
    file.write(data)

