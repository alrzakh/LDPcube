import math
import random


def perturb(age, epsilon, domain_size):

    bit_vector = [0] * domain_size
    bit_vector[age] = 1

    prob = math.exp(epsilon / 2) / (math.exp(epsilon / 2) + 1)

    for i in range(domain_size):
        if prob > random.random():
            continue
        else:
            bit_vector[i] = abs(bit_vector[i] - 1)

    return bit_vector


def aggregate(perturbed_ages, epsilon, domain_size):

    sum_list = [0] * domain_size
    prob = math.exp(epsilon / 2) / (math.exp(epsilon / 2) + 1)
    q = 1 / (math.exp(epsilon / 2) + 1)

    for entry in perturbed_ages:
        sum_list = [sum(x) for x in zip(sum_list, entry)]

    for i in range(domain_size):
        newValue = (sum_list[i] - (len(perturbed_ages) * q)) / (prob - q)
        sum_list[i] = newValue

    return sum_list
