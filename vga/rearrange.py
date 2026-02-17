# based off of ben eater's python program from "World's worst video card? The exciting conclusion"
from PIL import Image
import os
print(os.listdir('vga'))

image = Image.open("vga/keyboard characters.png")
pixels = image.load()
out_file = open("keyboard_char_rearranged.bin", "wb")
data = bytearray([])
rearranged = bytearray([])

position = [17,22,66,65,64,129,21,37,132,69,133,25,70,38,24,40,16,128,33,20,68,130,32,34,36,18,23,15,31,30,46,78,29,45,77,28,44,76]

for z in range(38):
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

for z in range(256*8):
    rearranged.append(0)

print(len(rearranged))
print(len(data))
print(len(position))

for x in range(38):
    for y in range(8):
        rearranged[position[x]*8+y] = data[x*8+y]
        data[x*8+y]


with open("keyboard_char_rearranged.bin", "wb") as file:
    file.write(rearranged)
