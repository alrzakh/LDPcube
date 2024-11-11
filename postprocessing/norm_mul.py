import numpy as np


def norm_mul(est_dist, org_dist):

    estimates = np.copy(est_dist)
    estimates[estimates < 0] = 0
    total = sum(estimates)
    n = sum(org_dist)
    result = estimates * n / total

    return result
