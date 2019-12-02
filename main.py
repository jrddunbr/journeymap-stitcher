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

X = list(map(lambda x: x[0],  clist))
Z = list(map(lambda x: x[1],  clist))

left  = min(X)
right = max(X)

bottom = max(Z)
top    = min(Z)

print(clist)


width = right - left + 1
height = bottom - top + 1

print("({},{}) to ({},{})".format(left, top, right, bottom))
print("{} by {} image".format(TILE_SIZE*width, TILE_SIZE*height))

bigimg = Image.new('RGB', (TILE_SIZE * width, TILE_SIZE * height))

print("starting stitch")

for x,z in clist:
    fn = "{},{}.png".format(x, z)
    img = Image.open(INPUTPATH + fn)
    print("adding ({},{}) image".format(x, z))
    bigimg.paste(im=img, box=((x-left) * TILE_SIZE, (z-top) * TILE_SIZE))

bigimg.save("output.png")

print("done")
