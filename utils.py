import numpy as np
from PIL import Image


# this takes alpha file name and returns Numpy array of that image
def load_image(file_name):
    try:
        im = Image.open(file_name)
        im = np.array(list(im.getdata()))  # create np array from image pixels
        im = im.flatten()  # create one dimensional array
    except IOError:
        print 'Cannot open the image file:' + file_name
    return im
