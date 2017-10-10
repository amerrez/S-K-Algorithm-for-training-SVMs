import numpy as np
from PIL import Image
import sys
import os

#checking if there is data in the folder specified by user in arg[5]
args = sys.argv
train_folder_name = args[5]
file_format = ["Q.PNG","O.PNG","P.PNG","S.PNG"]
found_data = False
for filepng in os.listdir(train_folder_name):
    for data_format in file_format:
        if filepng.endswith(data_format):
            found_data = True
if found_data != True:
    print("NO DATA")



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


#
#
# im = Image.open("1_P.PNG")
# im_array = np.fromstring(im.tobytes(), dtype=np.uint8) #1-dimensional
# print im_array
# im_array.reshape((im.size[1], im.size[0], 3))
# print im_array
