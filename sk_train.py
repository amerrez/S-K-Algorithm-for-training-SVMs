import sys
import math
import numpy as np
from SK import SKAlgo

KERNEL_TYPE = 'P'  # P: for polynonimal, G: Gauss, L: Layer

def train(sk, eps, max_update_num):
    # xi1 is the first positive value (image)
    sk.initialization(KERNEL_TYPE)
    # xj1 is the first negative value (image)
    adapt_count = 0
    is_stop = False
    while not is_stop and adapt_count < max_update_num and (adapt_count <
                                                            len(sk.X)):
        is_stop, t = sk.stop(eps)
        # The stop function check the model convergence < epsilon
        if not is_stop:
            sk.adapt(adapt_count,t)
        else:
            lamb_da_t = sk.lamb_da
        adapt_count += 1
    if adapt_count >= max_update_num:
        print "Max updates reached."

    alpha_pair = []
    for a in sk.alpha:
       if a != 0:
            y = 0
            if sk.alpha.index(a) in sk.Ip:
                y = 1
            alpha_pair.append([sk.alpha.index(a),float(sk.alpha[sk.alpha.index(a)]),y])
    print adapt_count
    result = ""
    result += "class_letter: " + class_letter + "\n"
    result += "m: "+str(sk.m) + "\n"+","+"mp: "+str(sk.mp) + "\n"+","+"mn: "+ str(sk.mn) + "\n"+","+str(sk.lamb_da)+"\n"
    result += str(sk.A)+","+str(sk.B)
    for alph in alpha_pair:
        result+=str(alph)+"\n"
    f = open(model_file_name,'w')
    f.write(result)
    f.close()

args = sys.argv
epsilon = float(args[1])
max_updates = int(args[2])
class_letter = args[3]
model_file_name = args[4]
train_folder_name = args[5]

sk = SKAlgo()
sk.read(class_letter, train_folder_name)
train(sk, epsilon, max_updates)
