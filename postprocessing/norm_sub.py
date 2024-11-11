import numpy as np


def norm_sub(est_dist, org_dist):

    estimates = np.copy(est_dist)
    n = sum(org_dist)

    tolerance = 0.0001
    while (np.abs(sum(estimates) - n) > tolerance) or (estimates < 0).any():
        estimates[estimates < 0] = 0
        total = sum(estimates)
        mask = estimates > 0
        diff = (1 - total) / sum(mask)
        estimates[mask] += diff

    return estimates
