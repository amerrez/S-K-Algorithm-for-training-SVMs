import numpy as np
from PIL import Image
import sys
import os

# I = [...k]
# a = [1,0,1,0,0,0,0] # Alpha for the first positive image =1 and the same for
# the first negative on

#checking if there is data with the naming convention in the folder specified by user
args = sys.argv
train_folder_name = args[5]
# model_file_name : args[4]
# class_letter : args[3]
# max_updates : args[2]
# epsilon : args[1]

file_format = ["Q.PNG","O.PNG","P.PNG","S.PNG"]
class_letters = ["O", "P", "W", "Q", "S"]
names_of_files = []
a = []
first_index = [-1,-1] # first_index[0] indicates 1st +ve, 1 indicates 1st -ve
images = []
Ip = []
In = []
xi1 = []
xj1 = []
X = [] # this is going to be a list of the images, it's an array of arrays
A,B,C = [],[],[]
D,E = [],[]
xip = []
m,mp,mn = 0,0,0

def read():
    found_data = False
    indexCounter = 0
    for file_name in os.listdir(train_folder_name):
        ###
        # here we should check each file.. and call a training method
        ###
        names_of_files.append(file_name)
        if ("_"+args[3]+".") in file_name :
            Ip.append(indexCounter)
            if first_index[0] == -1:
                a.append(1)
                first_index[0] = 1
            else:
                a.append(0)
        else:
            In.append(indexCounter)
            if first_index[1] ==-1:
                a.append(1)
                first_index[1] = 1
            else:
                a.append(0)
        X.append(load_image(file_name))
        if not found_data:   #TODO Will this work ?
            for data_format in file_format:
                if file_name.endswith(data_format):
                    found_data = True
        indexCounter +=1
    if found_data != True:
        print("NO DATA")


#this takes a file name and returns Numpy array of that image
def load_image(file_name):
    im = Image.open(train_folder_name+"/"+file_name)
    return np.array(list(im.getdata()))


def train():
    #xi1 is the first positive value (image)
    xi1 = X[first_index[0]]
    xj1 = X[first_index[1]]
    calculate_ms()
    xi1p = prime(xi1)
    xj1p = prime(xj1)
    xip = prime(X)
    A = kernal(xi1p,xi1p)
    B = kernal(xj1p,xj1p)
    C = kernal(xi1p,xj1p)
    D = kernal(xip,xi1p)
    E = kernal(xip,xj1p)
    #xj1 is the first nagative value (image)
    #m is form slode 5
    #method for prime



def calculate_ms():
    xi_sum = X[1]#initialize
    xip_sum = X[Ip[0]]#initializing wth the first positive element
    xin_sum = X[In[0]]#initializing wth the first negative element
    for i in xrange(1,len(X)):
        xi_sum = np.add(xi_sum,X[i])
    m = xi_sum/len(X)
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
    for x in X:
        xip_norms = np.linalg.norm(x-mp)
    rp = max(xip_norms)
    for x in X:
        xin_norms = np.linalg.norm(x-mn)
    rn = max(xin_norms)
    lambdaa = (r/(rp+rn))/2
    return lambdaa*x + (1-lambdaa)*m




read()
train()