import qrcode
from PIL import Image

flag = "flag{4c7u4lly_Bl4ck_4nd_Wh173_l0l}"

# creating qrcode image
img = qrcode.make("XOR original with 0xBB or go home")
img.save("black&almostblack.png")

# making it black and almost black
im = Image.open("black&almostblack.png")
im = im.convert('RGBA')
pixels = im.load()
for i in range(img.size[0]):
    for j in range(img.size[1]):
        if pixels[i, j] != (0, 0, 0, 255):
            pixels[i, j] = (1, 0, 0, 255)
im.save("black&almostblack.png")

# adding XORed flag in the end
with open("black&almostblack.png", "rb") as f:
    data = f.read()
for i in range(len(flag)):
    data += bytes([ord(flag[i]) ^ 0xBB])
    print(hex(ord(flag[i]) ^ 0xBB)[2:], end="")
print()
with open("black&almostblack.png", "wb") as f:
    f.write(data)
