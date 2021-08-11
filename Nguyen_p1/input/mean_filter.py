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

def mean(array):
    sum = 0
    
    for i in range(len(array)):
        sum = sum +array[i]
    
    average = sum // len(array)
    return average


for x in range(kernel, width-kernel):
    for y in range(kernel, height-kernel):
        position = 0
        for col in range(kernel):
            for row in range(kernel):
                neighbors[position] = img_array_original[(y-stretch)+row][(x-stretch)+col]
                position = position + 1

            avg_value = mean(neighbors) 
            img_array_original[y][x] = avg_value

#Border solution
for x in range(width):
    for y in range(height):
        small_sum = 0
        
        if ((x > 0 and x <= stretch) or (x > width-stretch and x < width)):
            if x < width//2:
                for i in range(neighbor_size):
                    small_sum = small_sum + img_array_original[y][x+i]

                img_array_original[y][x] = small_sum//neighbor_size
            else:
                for i in range(neighbor_size):
                    small_sum = small_sum + img_array_original[y][x-i]

                img_array_original[y][x] = small_sum/neighbor_size
        if ((y > 0 and y <= stretch) or (y > height-stretch and y < height)):
            if x < width//2:
                for i in range(neighbor_size):
                    small_sum = small_sum + img_array_original[y][x+i]

                img_array_original[y][x] = small_sum//neighbor_size
            else:
                for i in range(neighbor_size):
                    small_sum = small_sum + img_array_original[y][x-i]

                img_array_original[y][x] = small_sum//neighbor_size     


utils.save_bw_image(img_array_original, sys.argv[2])
utils.show_image(img_array_original)