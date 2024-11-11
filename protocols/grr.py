import math
import random
from collections import Counter


def perturb(age, epsilon, domain_size):

    prob = math.exp(epsilon) / (math.exp(epsilon) + domain_size - 1)

    if random.random() < prob:
        return age
    else:
        random_int = random.randint(0, domain_size - 1)
        while random_int == age:
            random_int = random.randint(0, domain_size - 1)
        return random_int


def aggregate(perturbed_ages, epsilon, domain_size):

    prob = math.exp(epsilon) / (math.exp(epsilon) + domain_size - 1)
    q = (1 - prob) / (domain_size - 1)

    counts = Counter(perturbed_ages)
    new_list = [0] * domain_size

    for count in counts:
        new_value = (counts[count] - (len(perturbed_ages) * q)) / (prob - q)
        new_list[count] = new_value

    return new_list
