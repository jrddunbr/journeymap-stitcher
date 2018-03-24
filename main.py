#!/usr/bin/python3

from PIL import Image
from os import listdir
from os.path import isfile, join

#
# -- Useful Library Functions
#

# open image
# img = Image.open(file)

# get image size


# create new image
# img = Image.new('RGB', (width, height))

# paste images in place
# img.paste(im=img, box=(x, y))

# show image

# img.show()

# save image
# img.save(file)

INPUTPATH = "./input/"

filelist = [f for f in listdir(INPUTPATH) if isfile(join(INPUTPATH, f))]

img = Image.open(INPUTPATH + filelist[0])
TILE_WIDTH, TILE_HEIGHT = img.size

bigX = 0
bigY = 0
smallX = 0
smallY = 0

for f in filelist:
    coord = f.split(".")
    ints = coord[0].split(",")
    x = int(ints[0])
    y = int(ints[1])
    if x > bigX:
        bigX = x
    if x < smallX:
        smallX = x
    if y > bigY:
        bigY = y
    if y < smallY:
        smallY = y

print("image map spans from ({},{}) to ({},{})".format(smallX, smallY, bigX, bigY))

bigimg = Image.new('RGB', (TILE_HEIGHT * (bigX + abs(smallX)), TILE_WIDTH * (bigY + abs(smallY))))

print("starting stitch")

for x in range(smallX, bigX):
    for y in range(smallY, bigY):
        if "{},{}.png".format(x,y) in filelist:
            img = Image.open(INPUTPATH + "{},{}.png".format(x, y))
            bigimg.paste(im=img, box=((x) * TILE_HEIGHT, (y) * TILE_WIDTH))

bigimg.save("output.png")
