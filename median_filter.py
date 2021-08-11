import math
import numpy
import utils
import sys

kernel = int(sys.argv[3])
stretch = kernel//2
neighbor_size = kernel * kernel
neighbors = [0 for x in range(neighbor_size)]

middle_index = len(neighbors)//2 + 1


img_array_original = utils.read_image_as_bw(sys.argv[1])
img_array_new = img_array_original.copy()

shape = img_array_original.shape

width = shape[1]
height = shape[0]

def sort(array):
    
    for i in range(1, len(array)):
        value = array[i]
        position = i

        while position > 0 and array[position-1] > value:
            array[position] = array[position-1]
            position = position - 1
            array[position] = value
    
    return array

for x in range(kernel, width-kernel):
    for y in range(kernel, height-kernel):

        if (img_array_original[y][x] <= 255 and img_array_original[y][x] >= 225) or (img_array_original[y][x] >= 0 and img_array_original[y][x] <= 35):
            
            position = 0
            for col in range(kernel):
                for row in range(kernel):

                    neighbors[position] = img_array_original[(y-stretch)+row][(x-stretch)+col]
                    position = position + 1

            neighbors = sort(neighbors)
            new_val = neighbors[middle_index]
            img_array_original[y][x] = new_val

for x in range(width):
    for y in range(height):
        if (img_array_original[y][x] <= 255 and img_array_original[y][x] >= 235) or (img_array_original[y][x] >= 0 and img_array_original[y][x] <= 25):
            if x < width//2:
                img_array_original[y][x] = img_array_original[y][x+1]
            else:
                img_array_original[y][x] = img_array_original[y][x-1]

utils.save_bw_image(img_array_original, sys.argv[2])