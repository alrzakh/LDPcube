import math
import random
import numpy as np


def perturb(actual_value, epsilon, domain_size):

    Z = []
    exp = math.exp(epsilon)

    k = int(math.ceil(1.0 * domain_size / (exp + 1)))  
    if k < 1:
        k = 1
    prob_p = (k * exp) / (k * exp + domain_size - k)
    fake_val_arr = []
    for i in range(0, domain_size):
        if i != actual_value:
            fake_val_arr.append(i)

    if random.uniform(0, 1) < prob_p:
        Z = np.random.choice(fake_val_arr, k - 1, replace=False)
        Z = np.append(Z, actual_value)
    else:
        Z = np.random.choice(fake_val_arr, k, replace=False)

    return Z


def aggregate(perturbed_user_data, epsilon, domain_size):
    exp = math.exp(epsilon)
    k = int(math.ceil(1.0 * domain_size / (exp + 1)))  
    if k < 1:
        k = 1
    tbr = np.zeros(domain_size)
    number_of_users = len(perturbed_user_data)
    supports = np.zeros(domain_size)
    for i in range(len(perturbed_user_data)):
        reported_subset = perturbed_user_data[i]
        for elt in reported_subset:
            supports[elt] = supports[elt] + 1
    g_k = (k * exp) / (k * exp + domain_size - k)   
    h_k = ((k * exp) / (k * exp + domain_size - k)) * ((k-1)/(domain_size-1)) + ((domain_size-k)/(k * exp + domain_size - k)) * (k/(domain_size-1))

    for i in range(len(tbr)):
        tbr[i] = (supports[i] - number_of_users * h_k) / (number_of_users * (g_k-h_k))

    tbr = number_of_users * tbr
    return tbr
