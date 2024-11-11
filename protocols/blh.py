
import math
import numpy as np
import xxhash
from sys import maxsize


def perturb(input_data, epsilon, k):

    if input_data < 0 or input_data >= k:
        raise ValueError('input_data (integer) should be in the range [0, k-1].')
    if epsilon > 0:

        g = 2
        p = math.exp(epsilon) / (math.exp(epsilon) + g - 1)

        rnd_seed = np.random.randint(0, maxsize, dtype=np.int64)
        hashed_input_data = (xxhash.xxh32(str(input_data), seed=rnd_seed).intdigest() % g)

        domain = np.arange(g)

        if np.random.binomial(1, p) == 1:
            sanitized_value = hashed_input_data
        else:
            sanitized_value = np.random.choice(domain[domain != hashed_input_data])
        return sanitized_value, rnd_seed

    else:
        raise ValueError('epsilon (float) needs a numerical value greater than 0.')


def aggregate(reports, epsilon, domain_size):

    g = 2
    counts = [0] * domain_size
    number_of_users = len(reports)
    p = math.exp(epsilon) / (math.exp(epsilon) + g - 1)

    for tuple_val_seed in reports:
        for v in range(domain_size):
            if tuple_val_seed[0] == (xxhash.xxh32(str(v), seed=tuple_val_seed[1]).intdigest() % g):
                counts[v] += 1

    a = g / (p * g - 1)
    b = number_of_users / (p * g - 1)
    counts = [a * val - b for val in counts]

    return counts

