import math
import numpy
import utils
import sys

img_array_original = utils.read_image_as_bw(sys.argv[1])
img_array_new = img_array_original.copy()

shape = img_array_original.shape
width = shape[1]
height = shape[0]

for x in range(width):
    for y in range(height):
        flipped_y = height - y - 1
        img_array_new[y][x] = img_array_original[flipped_y][x]



utils.save_bw_image(img_array_new, sys.argv[2])