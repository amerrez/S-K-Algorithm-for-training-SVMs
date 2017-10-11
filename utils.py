from PIL import Image


# this takes alpha file name and returns Numpy array of that image
def load_image(file_name):
    try:
        im = Image.open(file_name)
    except IOError:
        print 'Cannot open the image file:' + file_name
    return im
