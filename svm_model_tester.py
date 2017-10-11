import os
import sys
import re


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
