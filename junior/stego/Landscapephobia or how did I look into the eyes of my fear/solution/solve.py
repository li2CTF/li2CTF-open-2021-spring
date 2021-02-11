from PIL import Image

im1 = Image.open('photo1.png')
im2 = Image.open('photo2.png')

pixels1 = im1.load()
pixels2 = im2.load()
width, height = im1.size

diff = Image.new('RGB', (width, height))
pixelsDiff = diff.load()

for x in range(width):
    for y in range(height):
        if pixels1[x, y] != pixels2[x, y]:
        	pixelsDiff[x, y] = (255, 0, 0)
        
diff.save("result.png")