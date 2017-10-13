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
        self.Ip = []  # I+
        self.In = []  # I-
        self.xi1 = np.array([])  # positive input data set
        self.xj1 = np.array([])  # negative input data set
        self.X = np.array([])  # vector of input data, this is going to be alpha list of
        # the data, it's an array of arrays
        self.A, self.B, self.C = np.array([]),np.array([]),np.array([])
        self.D, self.E = np.array([]),np.array([])
        self.xip = np.array([])
        self.m, self.mp, self.mn = 0, 0, 0
        self.lamb_da = 0

    def read(self, class_letter, train_folder_name):
        found_data = False
        indexCounter = 0
        names_of_files = []
        for file_name in os.listdir(train_folder_name):
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
            np.append(self.X,
                utils.load_image(train_folder_name + "/" + file_name))
            if not found_data:  # TODO Will this work ?
                for data_format in self.FILE_FORMAT:
                    if file_name.endswith(data_format):
                        found_data = True
            indexCounter += 1
        print "X from read:", self.X
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
            return self.__polynomial_kernel(x, y, 4)  # For this HW, p = 4
        else:
            print 'Kernel type is not supported'
            exit(0)

    def __polynomial_kernel(self, x, y, p):
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
        rp = xip_norms.max()
        for x in self.X:
            xin_norms = np.linalg.norm(x - self.mn)
        rn = xin_norms.max()
        self.lamb_da = (r / (rp + rn)) / 2
        return self.lamb_da * x + (1 - self.lamb_da) * self.m


    def initialization(self, kernel_type):
        # xi1 is the first positive value (image)
        xi1 = self.X[self.first_index[0]]
        xj1 = self.X[self.first_index[1]]
        # m calculation formula indicates in slide 5 (Sep 27)
        self.calculate_ms()
        xi1p = self.prime(xi1)
        xj1p = self.prime(xj1)
        self.A = self.kernel(xi1p, xi1p, kernel_type)
        self.B = self.kernel(xj1p, xj1p, kernel_type)
        self.C = self.kernel(xi1p, xj1p, kernel_type)
        for i in range(0, len(self.X)):
            xip = self.prime(self.X[i])
            self.D[i] = self.kernel(xip, xi1p, kernel_type)
            self.E[i] = self.kernel(xip, xj1p, kernel_type)

    def stop(self, a, b, c, d, e, eps):
        mi = np.array([])
        for i in xrange(len(self.X)):
            if i in Ip:
                mi.append((d[i] - e[i] + b - c) / math.sqrt(a + b - 2 * c))
            else:
                mi.append((e[i] - d[i] + a - c) / math.sqrt(a + b - 2 * c))
        t = np.argmin(mi)
        if math.sqrt(a - b - 2 * c) - mi[t] < eps:
            return True, t
        return False, t

    def adapt(self, i, delta, a, b, c, dt, et, x, y, t):
        k = self.kernel(x, y, 'P')
        if t in Ip:  # t belong to I+
            m = (a - dt + et - c) / (a + k - 2 * (dt - et))
            q = min(1, m)
            self.alpha[i] = (1 -q) * alpha[i] + q * delta
            self.A = self.A * ((1 - q) ** 2) + 2 * (1 -q) * q * dt + (q ** 2) * k
            self.C = (1 - q)*c + q * et
            for i in range(len(self.X)):
                self.D[i] = (1 - q) * self.D[i] + q * k
        else:  # t belong to I-
            m = (b - et + dt - c) / (b + k - 2 * (et - dt))
            q = min(1, m)
            self.alpha[i] = (1 - q) * alpha[i] + q * delta
            self.B = self.B * ((1 - q) ** 2) + 2 * (1 - q) * q * et + (q ** 2) * k
            self.C = (1 - q) * self.C + q * dt
            self.E[i] = (1 - q) * self.E[i] + q * k
