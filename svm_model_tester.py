import os
import sys
import re
import utils

model_file_name = args[1]

def validate_arguments(arguments):
    if len(arguments) < 3:
        print ('Missing arguments')
        return False
    if not os.path.isdir(arguments[2]):
        print ('Train folder is not alpha directory')
        return False
    if not os.path.isdir(arguments[3]):
        print ('Test folder is not alpha directory')
        return False
    # All the test passed
    return True


def test(test_folder_name):
    image_files = os.listdir(test_folder_name)
    trial_num, correct_sum, false_positive_sume, false_negative_sum = 0
    for f in image_files:
        output = ''
        trial_num += 1
        output += str(trial_num)

# this is the main logic of test
def predict(test_folder_name,test_file_name):
    test_item = utils.load_image(test_folder_name+"/"+test_file_name)
    f = open(self.model_file_name)
    params = f.readline()
    mp,mn,lamb_da = params.split(",")
    mp = np.array(mp) # this doesn't work, we need to mfind a better way to convert strin to @ dimensional array
    mn = np.array(mn)
    lamb_da = int(lamb_da)
    A,B = f.readline().split(",")
    A = np.array(A) # this doesn't work, we need to mfind a better way to convert strin to @ dimensional array
    B = np.array(B)
    index_vec = []
    alpha_vec = []
    y_vec = []
    while not eof:
        index,alpha,y = [map(f.readline().split(","),int)]
        index_vec.append(index)
        alpha_vec.append(alpha)
        y_vec.append
    #calculating the hyper plane g(x)
    for svm in svm_vector: #TODO svm_vector, this is the list of x_prime (the x values from training data that are called support vecotrs and their alpha is 1 while all other alhpas are 0)
        k.append(kernal(test_item,svm))
    for i in xrange(len(alpha_vec)):
        g += alpha_vec[i] * y_vec[i] * k[i] + (B−A)/2)
    # g(x) out put could be one of two things(we are guessing)
    # 1) if its an integer value 0 or 1 then
        # 1 means test image belongs to the class and 0 is otherwise
    # 2) the out put of g(X) could be an equasion and then we need to use it to see if the tes_items belong to the right side or the left side 




def kernel(self, x, y):
    return (np.dot(x.transpose(), y) + 1) ** 4

# Main function
if validate_arguments(sys.argv):
    args = sys.argv
    model_file_name = args[1]
    if not os.path.exist(model_file_name):
        print ("CAN'T FIND MODEL FILE")
        exit(0)

    train_folder_name = args[2]
    train_files = os.listdir(train_folder_name)
    if train_files.count() == 0:
        print('NO TRAINING DATA')
        exit(0)

    test_folder_name = args[3]
    test_files = os.listdir(test_folder_name)
    if test_files.count() == 0:
        print('NO TEST DATA')
        exit(0)

    regex = r"\d + '_' + ('P' | 'W' | 'Q' | 'S')"
