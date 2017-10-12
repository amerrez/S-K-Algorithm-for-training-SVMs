import sys
import math
import numpy as np

from skalgkernel import SKAlgKernel

KERNEL_TYPE = 'P'  # P: for polynonimal, G: Gauss, L: Layer


def delta(i, t):
    if i == t:
        return 1.0
    else:
        return 0.0


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
    D = sk.kernel(xi, xi1p, KERNEL_TYPE)
    E = sk.kernel(xi, xj1p, KERNEL_TYPE)
    # xj1 is the first nagative value (image)
    # m is form slide 5
    # method for prime
    #
    # From this point, I assume the initialization step is completed. So all
    # the needed data are wrapped in SKAlgKernel object
    # TODO:I may be wrong with this loop condition
    # I just assume that I have input data for training
    #c_flag = False
    adapt_count = 0
    is_stop = False
    i = 0
    while not is_stop and adapt_count < max_update_num:
        if sk.data[i] == class_letter:  # TODO: assume the positive case
            c_flag = True
        else:
            c_flag = False
        # The stop function check the model convergence < epsilon
        is_stop, t = sk.stop(sk.A, sk.B, sk.C, sk.D, sk.E, eps, c_flag)
        if not is_stop:
            sigma = 1 if t == i else 0  # is this the right i?
            # TODO what is xt in adaptation step??? Assuming xt = [1]
            x, y = [1]  # TODO Note xt is the element in xi where i = t
            sk.adapt(c_flag, i, sigma, sk.A, sk.B, sk.C, sk.D[t], sk.E[t], x, y)
            adapt_count += 1
        else:
            i += 1
            # Repeat the process until convergence < epsilon or
            # more than max_updates adaptation steps have been done
            # (adapt_count >= max_update
            if i == len(sk.data[i]):
                i = 0


args = sys.argv
epsilon = args[1]
max_updates = args[2]
class_letter = args[3]
model_file_name = args[4]
train_folder_name = args[5]

sk = SKAlgKernel()
sk.read(class_letter, train_folder_name)
train(sk, epsilon, max_updates)
