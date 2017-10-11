import sys

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
    # xj1 is the first nagative value (image)
    # m is form slode 5
    # method for prime


args = sys.argv
epsilon = args[1]
max_updates = args[2]
class_letter = args[3]
model_file_name = args[4]
train_folder_name = args[5]

sk = SKAlgKernel()
sk.read(class_letter, train_folder_name)
train(sk, epsilon, max_updates)
