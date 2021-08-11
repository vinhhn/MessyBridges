"""
Various utility functions to make life easier

Author: Sam Vinitsky
"""

from PIL import Image
import numpy as np
from IPython.display import display

def read_image_as_bw(path):
    """
    Reads in the image from the given path as a black and white image.

    Returns a numpy array of pixels, with values from 0-255

    :param path: path to original image
    """

    # open as a PIL Image
    input_image = Image.open(path)
    bw_image = input_image.convert(mode='L')

    #convert into an array
    bw_array = np.asarray(bw_image)
    return bw_array.copy()

def show_image(im_array):
    """
    Displays a numpy array as an image

    :param im_array: image array to show
    """

    # convert to Image object 
    im_object = Image.fromarray(im_array)

    im_object.show()

def save_bw_image(im_array, path):
    """
    Takes a black and white numpy array and saves it as an image

    :param im_array: numpy array, to be interpreted as a black and white image
    :param path: location to store the array to, including 
    """

    im_object = Image.fromarray(im_array)
    bw_image = im_object.convert(mode='L')

    if "." not in path:
        path+= ".png"

    bw_image.save(path, mode='L')