import os
import sys
import re
import utils

model_file_name = args[1]
lamb_da = -1
m = []

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
        model_result = self.predict(test_folder_name,f)
        #correct
        if (model_result and image_letter == class_letter) or (not model_result and
                                                image_letter != class_letter):
            result_counter+=1
            print("Correct")
        elif(model_result and image_letter != class_letter):
            false_Positive +=1
            print("False Positive")
        elif(not model_result and image_letter == class_letter):
            false_Negative +=1
            print("False Negative")
    total_sum = false_Negative+false_Positive+result_counter
    fraction_correct = result_counter/total_sum
    fraction_false_Positive = false_Positive/total_sum
    fraction_false_Negative = false_Negative/total_sum
    output = 'fraction_correct: '+str(fraction_correct)+"\n"
    output+='fraction_false_Positive: '+str(fraction_false_Positive)+"\n"
    output+='fraction_false_Negative: '+str(fraction_false_Negative)+"\n"
    print(output)

# this is the main logic of test
def predict(test_folder_name,test_file_name):
    test_item = utils.load_image(test_folder_name+"/"+test_file_name)
    f = open(self.model_file_name)
    class_letter = f.readline()[-1]
    params = f.readline()
    m,mp,mn,lamb_da = params.split(",")
    m = np.array(m)
    mp = np.array(mp)
    mn = np.array(mn)
    lamb_da = int(lamb_da)
    A,B = f.readline().split(",")
    A = np.array(A)
    B = np.array(B)
    index_vec = []
    alpha_vec = []
    y_vec = []
    while not eof:
        index,alpha,y = [map(f.readline().split(","),int)]
        index_vec.append(index)
        alpha_vec.append(alpha)
        y_vec.append(y)
        g = []
    #calculating the hyper plane g(x)
    for svm in svm_vector:
        k.append(kernal(test_item,svm))
    for i in xrange(len(alpha_vec)):
        g += alpha_vec[i] * y_vec[i] * k[i] + (B−A)/2)
    if g == 0:
        model_result = False
    else:
        model_result = True
    image_num = int(test_file_name.split('_')[0])
    image_letter = test_file_name.split('_')[1][0]
    correct_result_counter=0
    false_Positive = 0
    false_Negative = 0

def prime(x):
    return self.lamb_da * x + (1 - self.lamb_da) * self.m

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

test()
