import numpy as np
import xxhash
from sys import maxsize
import math


def perturb(actual_value, epsilon, domain_size):

    g = int(round(np.exp(epsilon))) + 1

    p = math.exp(epsilon) / (math.exp(epsilon) + g - 1)
    q = 1.0 / (math.exp(epsilon) + g - 1)

    rnd_seed = np.random.randint(0, maxsize, dtype=np.int64)
    hashed_value = (xxhash.xxh32(str(actual_value), seed=rnd_seed).intdigest() % g)

    perturbed_value = hashed_value
    p_sample = np.random.random_sample()
    if p_sample > p - q:
        perturbed_value = np.random.randint(0, g)

    return perturbed_value, rnd_seed


def aggregate(reports, epsilon, domain_size):

    if len(reports) == 0:
        raise ValueError('List of reports is empty.')
    if epsilon > 0:

        # Number of reports
        n = len(reports)

        g = int(round(np.exp(epsilon))) + 1

        count_report = np.zeros(domain_size)
        for tuple_val_seed in reports:
            for v in range(domain_size):
                if tuple_val_seed[0] == (xxhash.xxh32(str(v), seed=tuple_val_seed[1]).intdigest() % g):
                    count_report[v] += 1

        p = np.exp(epsilon) / (np.exp(epsilon) + g - 1)
        q = 1 / g

        est_freq = np.array((count_report - n * q) / (p - q))

        return est_freq

    else:
        raise ValueError('epsilon (float) needs a numerical value greater than 0.')


