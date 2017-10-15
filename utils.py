import numpy as np
from PIL import Image


# this takes image file name and returns Numpy array of that image
def load_image(file_name):
    # pixel_array = np.array([])
    im = Image.open(file_name)
    # create np array from image pixels
    pixel_array = np.array(list(im.getdata()))
    pixel_array = pixel_array.flatten()  # create one dimensional array
    for i in range(0,len(pixel_array)): # convert pixel array in 0s and 1s
        if pixel_array[i] < 127 :
            pixel_array[i] = 0
        else :
            pixel_array [i] = 10
    return pixel_array

def delta(i, t):
    return 1.0 if t == i else 0.0
