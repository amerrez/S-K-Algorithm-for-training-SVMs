import sys
import math
import numpy as np

from skalgkernel import SKAlgKernel

KERNEL_TYPE = 'P'  # P: for polynonimal, G: Gauss, L: Layer


def delta(i, t):
    return 1.0 if t == i else 0.0


def train(sk, eps, max_update_num):
    # xi1 is the first positive value (image)
    sk.initialization(KERNEL_TYPE)
    # xj1 is the first negative value (image)
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
    while not is_stop and adapt_count < max_update_num:
        is_stop, t = sk.stop(sk.A, sk.B, sk.C, sk.D, sk.E, eps)
        # The stop function check the model convergence < epsilon
        if not is_stop:
            x = sk.xip[t]
            sk.adapt(i, delta(i,t), sk.A, sk.B, sk.C, sk.D[t], sk.E[t], x, x, t)
            # Repeat the process until convergence < epsilon or
            # more than max_updates adaptation steps have been done
            # (adapt_count >= max_update
        else:
            lamb_da_t = sk.lamb_da
        adapt_count += 1
    if adapt_count >= max_update_num:
        print "Max updates reached"
    else:
        alpha_pair = []
        for i in sk.alpha[i]:
            if sk.alpha[i] != 0:
                alpha_pair.append([i,float(alpha[i])],1 if i in Ip else 0)
        result = sk.mp+","+sk.mn+","+lamb_da_t+"\n"
        result += str(sk.A)+","+str(sk.B)
        for alph in alpha_pair:
            result+=str(alph[0])+str(alph[1])+"\n"
        f = open(model_file_name,'w')
        f.write(result)
        f.close()





args = sys.argv
epsilon = args[1]
max_updates = args[2]
class_letter = args[3]
model_file_name = args[4]
train_folder_name = args[5]

sk = SKAlgKernel()
sk.read(class_letter, train_folder_name)
train(sk, epsilon, max_updates)
