import numpy as np
from PIL import Image



# #!/usr/bin/python
# from os import listdir
# from PIL import Image as PImage

# def loadImages(path):
#     # return array of images

#     imagesList = listdir(path)
#     loadedImages = []
#     for image in imagesList:
#         img = PImage.open(path + image)
#         loadedImages.append(img)

#     return loadedImages

# path = "/path/to/your/images/"

# # your images in an array
# imgs = loadImages(path)

# for img in imgs:
#     # you can show every image
#     img.show()




im = Image.open("1_P.PNG")
im_array = np.fromstring(im.tobytes(), dtype=np.uint8) #1-dimensional
print im_array
im_array.reshape((im.size[1], im.size[0], 3)) 
print im_array