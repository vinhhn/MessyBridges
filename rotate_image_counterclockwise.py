import math
import numpy
import utils
import sys

img_array_original = utils.read_image_as_bw(sys.argv[1])

shape = img_array_original.shape

width = shape[1]
height = shape[0]

img_array_new = numpy.array([[0 for x in range(height)] for y in range(width)])
new_height = len(img_array_new)
new_width = len(img_array_new[0])

flipped_image = img_array_original.copy()
for x in range(width):
    for y in range(height):
        flipped_x = width - x - 1
        flipped_image[y][x] = img_array_original[y][flipped_x]

for y in range(width):
    for x in range(height):
        img_array_new[y][x] = flipped_image[x][y]

utils.save_bw_image(img_array_new, sys.argv[2])