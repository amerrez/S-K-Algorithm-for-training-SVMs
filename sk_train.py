import numpy as np
from PIL import Image
import sys
import os

# I = [...k]
# a = [1,0,1,0,0,0,0] # Alpha for the first positive image =1 and the same for
# the first negative on
#TODO # a = [1,0,1,0,0,0,0] # Alpha for the first positive image =1 and the same for
#TODO dot product in kernal

#checking if there is data with the naming convention in the folder specified by user
args = sys.argv
train_folder_name = args[5]
model_file_name = args[4]
class_letter = argv[3]
max_updates = argv[2]
epsilon = arhv[1]

file_format = ["Q.PNG","O.PNG","P.PNG","S.PNG"]
found_data = False
class_letters = ["O", "P", "W", "Q", "S"]
names_of_files = []
a = []
first_positive_index = -1
first_negative_index = -1
images = []
Ip = []
In = []
xi1 = []
xj1 = []
xi = [] # this is going to be a list of the images, it's an array of arrays
A,B,C = []
D,E = []
indexCounter = 0
m,mp,mn = 0
for file_name in os.listdir(train_folder_name):
    ###
    # here we should check each file.. and call a training method
    ##
    names_of_files.append(file_name)
    if file_name.CONSTANTS(class_letter+"."):
        Ip.append(indexCounter)
        if first_positive_index == -1:
            a.append(1)
            first_positive_index = 1
        else:
            a.append(0)
    else:
        In.append(indexCounter)
        if first_negative_index =-1:
            a.append(1)
            first_negative_index = 1
        else:
            a.append(0)
    xi.append(load_image(file_name))
    if not found_data:
        for data_format in file_format:
            if file_name.endswith(data_format):
                found_data = True
    indexCounter +=1
if found_data != True:
    print("NO DATA")

#this takes a file name and returns an array of that image
def load_image(file_name):
    im = Image.open(train_folder_name+"/"+file_name)
    return np.array(im)


def train():
    #xi1 is the first positive value (image)
    xi1 = xi[first_positive_index]
    xj1 = xi[first_negative_index]
    calculate_ms()
    xi1p = prime(xi1)
    xj1p = prime(xj1)
    xip = prime(xi)
    A = kernal(xi1p,xi1p)
    B = kernal(xj1p,xj1p)
    C = kernal(xi1p,xj1p)
    D = kernal(xip,xi1p)
    E = kernal(xip,xj1p)
    #xj1 is the first nagative value (image)
    #m is form slode 5
    #method for prime
def calculate_ms():
    xi_sum = xi[1]#initialize
    xip_sum = xi[Ip[0]]#initializing wth the first positive element
    xin_sum = xi[In[0]]#initializing wth the first negative element
    for i in xrange(1,xi):
        xi_sum = np.add(xi_sum,xi[i])
    m = xi_sum/len(xi)
    #calculating m+
    for i in Ip[1:]:#starting from the second postitive element
        xip_sum = np.add(xip_sum,xip[i])
    mp = xip_sum/len(Ip)
    #calculating m-
    for i in In[1:]:#starting from the second postitive element
        xin_sum = np.add(xin_sum,xin[i])
    mn = xin_sum/len(In)

def kernal(x,y):
    #TODO test
    return (np.dot(x.transpose(),y)+1)^4

def prime(x): # make sure we are handeling the different values correctly (vector xi or a single value vector)
    #assumng that lambdaa is in the mid of the inequality that determines lambdaa acepted range
    r = np.linalg.norm(mp - mn)
    xip_norms = []
    xin_norms = []
    for x in xi:
        xip_norms = np.linalg.norm(x-mp)
    rp = max(xip_norms)
    for x in xi:
        xin_norms = np.linalg.norm(x-mn)
    rn = max(xin_norms)
    lambdaa = (r/(rp+rn))/2
    return lambdaa*x + (1-lambdaa)*m

read()
train()
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
