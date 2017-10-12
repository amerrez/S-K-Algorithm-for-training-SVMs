import sys
import math
import numpy as np

from skalgkernel import SKAlgKernel

KERNEL_TYPE = 'P'  # P: for polynonimal, G: Gauss, L: Layer


def train(sk, eps, max_update_num):
    # xi1 is the first positive value (image)
    xi1 = sk.X[sk.first_index[0]]
    xj1 = sk.X[sk.first_index[1]]
    sk.calculate_ms()
    xi1p = sk.prime(xi1)
    xj1p = sk.prime(xj1)
    xip = sk.prime(sk.X)
    A = sk.kernel(xi1p, xi1p, KERNEL_TYPE)
    B = sk.kernel(xj1p, xj1p, KERNEL_TYPE)
    C = sk.kernel(xi1p, xj1p, KERNEL_TYPE)
    D = sk.kernel(xip, xi1p, KERNEL_TYPE)
    E = sk.kernel(xip, xj1p, KERNEL_TYPE)
    index_counter = 0
    while image in sk.X:    # iterate for all images in X (training starts)
        is_image_positive = False
        if index_counter in sk.Ip:
            is_image_positive = True
        flag_stop, t = stop(A, B, C, D, E, eps, is_image_positive)
        if not flag_stop :
            if is_image_positive :
                q = min(1,(A-D[t]+E[t]-C)/(A+sk.kernel(sk.prime(sk.X[t]),
                                    sk.prime(sk.X[t]),'P')- 2.0*(D[t]-E[t])))
                sk.alpha[index_counter] = (1-q)* sk.alpha[index_counter] +
                                          q*delta(index_counter,t)
                A = A(1-q)^2+2.0*(1-q)*q*D[t]+q^2*sk.kernel(sk.prime(sk.X[t]),
                                                        sk.prime(sk.X[t]),'P')
                C = (1-q)*C+q*E[t]
                for i in xrange(len(sk.X)):   # for all i
                    D[i] = (1-q)*D[i]+q*sk.kernel(sk.prime(sk.X[t]),
                                                  sk.prime(sk.X[t]),'P')
            else :
                q = min(1,(B-E[t]+D[t]-C)/(B+sk.kernel(sk.prime(sk.X[t]),
                                    sk.prime(sk.X[t]),'P')- 2.0*(E[t]-D[t])))
                sk.alpha[index_counter] = (1 - q) *
                        sk.alpha[index_counter] + q * delta(index_counter, t)
                B = B*(1−q)^2+2.0*(1−q)*q*E[t]+q^2*  #TODO could not understnad why red line here
                            sk.kernel(sk.prime(sk.X[t]),sk.prime(sk.X[t]),'P')
                C = (1-q)*C+q*D[t]
                for i in xrange(len(sk.X)):
                    E[i] = (1-q)*E[i] + q*
                            sk.kernel(sk.prime(sk.X[t]),sk.prime(sk.X[t]),'P')
        else:
            break
        index_counter += 1 #TODO why code not rechable here


    # xj1 is the first nagative value (image)
    # m is form slode 5
    # method for prime

def delta(i,t):
    if (i==t):
        return 1.0
    else :
        return 0.0

def stop(a, b, c, d, e, eps, classified_flag):
    mi = []
    if classified_flag:
        for i in range(0, len(d)):
            mi[i] = ((d[i] - e[i] + b - c) / math.sqrt(a + b - 2 * c))
    else:
        for i in range(0, len(d)):
            mi[i] = ((e[i] - d[i]  + a - c) / math.sqrt(a + b - 2 * c))
    t = mi.argmin()
    if math.sqrt(a - b - 2*c) - mi[t] < eps:
        return True, t
    return False, t


args = sys.argv
epsilon = args[1]
max_updates = args[2]
class_letter = args[3]
model_file_name = args[4]
train_folder_name = args[5]

sk = SKAlgKernel()
sk.read(class_letter, train_folder_name)
train(sk, epsilon, max_updates)
