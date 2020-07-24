# Nathan Shulkin made this
# to divide an image into parts and crop the image into those parts.
# then save the cropped images in the same directory as the original image.

from PIL import ImageColor
from PIL import Image


# get the image
print('what is the image filename?')
imName = str(input())
try:
    im = Image.open(imName)
except:
    print('sorry, could not open image, make sure the image is in the same directory as the program.')
    exit()

width, height = im.size

# get the number of crops in x and y direction
print('how many crops would you like in the x direction/horizontal?')
xCrop = int(input())

print('how many crops would you like in the y direction/vertical?')
yCrop = int(input())


# get the ratio to crop it up
totalSq = xCrop * yCrop

xInc = int(width / xCrop)
yInc = int(height / yCrop)


# increment and file name saver
i = 1
k = 1
# crop it up
for y in range(0, yCrop):
    j = 1
    for x in range(0, xCrop):
        print(xInc * k, yInc * j)
        croppedIm = im.crop(((x * xInc), (y * yInc), (xInc * j), (yInc * k)))
        # croppedIm.show()
        croppedIm.save("crop" + str(i) + ".png")
        i += 1
        j += 1
    k += 1
