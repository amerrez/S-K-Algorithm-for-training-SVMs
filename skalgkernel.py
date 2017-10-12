import numpy as np
import os
import utils
import math


class SKAlgKernel(object):
    FILE_FORMAT = ["Q.PNG", "O.PNG", "P.PNG", "S.PNG"]
    CLASS_LETTER = ["O", "P", "W", "Q", "S"]

    # I = [...k]
    # alpha = [1,0,1,0,0,0,0] # Alpha for the first positive image =1
    # and the same for the first negative on
    def __init__(self):
        self.alpha = []
        self.first_index = [-1, -1]  # first_index[0] indicates 1st +ve,
        # 1 indicates 1st -ve
        self.data = []  # In this HW, data is list of images
        self.Ip = []  # I+
        self.In = []  # I-
        self.xi1 = []  # positive input data set
        self.xj1 = []  # negative input data set
        self.X = []  # vector of input data, this is going to be alpha list of
        # the data, it's an array of arrays
        self.A, self.B, self.C = [], [], []
        self.D, self.E = [], []
        self.xip = []
        self.m, self.mp, self.mn = 0, 0, 0

    def read(self, class_letter, train_folder_name):
        found_data = False
        indexCounter = 0
        names_of_files = []
        for file_name in os.listdir(train_folder_name):
            ###
            # here we should check each file.. and call alpha training method
            ###
            names_of_files.append(file_name)
            if ("_" + class_letter + ".") in file_name:
                self.Ip.append(indexCounter)
                if self.first_index[0] == -1:
                    self.alpha.append(1)
                    self.first_index[0] = 1
                else:
                    self.alpha.append(0)
            else:
                self.In.append(indexCounter)
                if self.first_index[1] == -1:
                    self.alpha.append(1)
                    self.first_index[1] = 1
                else:
                    self.alpha.append(0)
            self.X.append(
                utils.load_image(train_folder_name + "/" + file_name))
            if not found_data:  # TODO Will this work ?
                for data_format in self.FILE_FORMAT:
                    if file_name.endswith(data_format):
                        found_data = True
            indexCounter += 1
        if not found_data:
            print("NO DATA")
        return names_of_files

    def calculate_ms(self):
        xi_sum = self.X[1]  # initialize
        xip_sum = self.X[self.Ip[0]]  # initializing wth the first positive element
        xin_sum = self.X[self.In[0]]  # initializing wth the first negative element
        for i in xrange(1, len(self.X)):
            xi_sum = np.add(xi_sum, self.X[i])
        m = xi_sum / len(self.X)
        # calculating m+
        for i in self.Ip[1:]:  # starting from the second postitive element
            xip_sum = np.add(xip_sum, self.xip[i])
        mp = xip_sum / len(self.Ip)
        # calculating m-
        for i in self.In[1:]:  # starting from the second postitive element
            xin_sum = np.add(xin_sum, self.xin[i])
        mn = xin_sum / len(self.In)
        return mp, mn

    def kernel(self, x, y, kernel_type):
        if kernel_type == 'P':  # Polynomial kernel
            return self.polynomial_kernel(x, y, 4)  # For this HW, p = 4
        else:
            print 'Kernel type is not supported'
            exit(0)

    def __polynomial_kernel(self, x, y, p):
        # TODO test
        return (np.dot(x.transpose(), y) + 1) ** p

    def prime(self, x):  # make sure we are handling the different values
        # correctly (vector xi or alpha single value vector)
        # assuming that lambda is in the mid of the inequality that
        # determines lambda accepted range
        r = np.linalg.norm(self.mp - self.mn)
        xip_norms = []
        xin_norms = []
        for x in self.X:
            xip_norms = np.linalg.norm(x - self.mp)
        rp = max(xip_norms)
        for x in self.X:
            xin_norms = np.linalg.norm(x - self.mn)
        rn = max(xin_norms)
        lamb_da = (r / (rp + rn)) / 2
        return lamb_da * x + (1 - lamb_da) * self.m

    def stop(self, a, b, c, d, e, eps, classified_flag):
        mi = []
        if classified_flag:
            for i in range(0, len(d)):
                mi[i] = ((d[i] - e[i] + b - c) / math.sqrt(a + b - 2 * c))
        else:
            for i in range(0, len(d)):
                mi[i] = ((e[i] - d[i] + a - c) / math.sqrt(a + b - 2 * c))
        t = mi.argmin()
        if math.sqrt(a - b - 2 * c) - mi[t] < eps:
            return True, t
        return False, t

    def adapt(self, c_flag, i, sigma_t, a, b, c, dt, et, x, y):
        k = self.kernel(x, y, 'P')
        if c_flag:  # t belong to I+
            m = (a - dt + et - c) / (a + k - 2 * (dt - et))
            q = min(1, m)
            self.alpha[i] = (1 -q) * i + q * sigma_t
            self.A = a * ((1 - q) ** 2) + 2 * (1 -q) * q * dt + (q ** 2) * k
            self.C = (1 - q)*c + q * et
            self.D[i] = (1 - q) * self.D[i] + q * k
        else:  # t belong to I-
            m = (b - et + dt - c) / (b + k - 2 * (et - dt))
            q = min(1, m)
            self.alpha[i] = (1 - q) * i + q * sigma_t
            self.B = b * ((1 - q) ** 2) + 2 * (1 - q) * q * et + (q ** 2) * k
            self.C = (1 - q) * c + q * dt
            self.E[i] = (1 - q) * self.E[i] + q * k
