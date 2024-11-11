import numpy as np


def l1_error(real_list, new_list):

    if len(real_list) != len(new_list):
        raise ValueError('Length of real_list and new_list do not match!')
    error_sum = 0.0
    length = len(real_list)
    for x in range(length):
        error_sum += np.abs(real_list[x] - new_list[x])
    return error_sum / length

