#!/usr/bin/python3

from PIL import Image
from os import listdir
from os.path import isfile, join

def getImageSize(filename):
    img = Image.open(filename)
    return img.size[0]

INPUTPATH = "./input/"
filelist = [f for f in listdir(INPUTPATH) if isfile(join(INPUTPATH, f))]
clist = [(int(x.split(",")[0]), int(x.split(",")[1])) for x in [f.split(".",1)[0] for f in filelist]]
TILE_SIZE = getImageSize(INPUTPATH + filelist[0])

# coordinate directions
# x,z
# -,-   +,-
#
# -,+   +,+

bottom = -1000
top = 1000
left = 1000
right = -1000

print(clist)

for entry in clist:
    x = entry[0]
    z = entry[1]
    if (x > right):
        right = x
    if (x < left):
        left = x
    if (z < top):
        top = z
    if (z > bottom):
        bottom = z

# These may be wrong for things that don't pass through the origin.
width = abs(left) + abs(right) + 1
height = abs(top) + abs(bottom) + 1

print("({},{}) to ({},{})".format(left, top, right, bottom))

bigimg = Image.new('RGB', (TILE_SIZE * width, TILE_SIZE * height))

print("starting stitch")

# again, comment about the origin
for z in range(top, bottom+1):
    for x in range(left, right+1):
        fn = "{},{}.png".format(x, z)
        if fn in filelist:
            print("#", end="")
            img = Image.open(INPUTPATH + fn)
            bigimg.paste(im=img, box=((x + abs(left)) * TILE_SIZE, (z + abs(top)) * TILE_SIZE))
        else:
            print(" ", end="")
    print()

bigimg.save("output.png")

print("done")
