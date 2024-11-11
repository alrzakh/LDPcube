import numpy as np


def l2_error(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists should have the same length")

    distance = 0
    for a, b in zip(list1, list2):
        distance += (a - b) ** 2

    return distance ** 0.5
