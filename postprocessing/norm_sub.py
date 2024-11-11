import numpy as np


def norm_sub(est_dist, org_dist):
    estimates = np.copy(est_dist)
    n = sum(org_dist)
    while (np.fabs(sum(estimates) - n) > 1) or (estimates < 0).any():
        estimates[estimates < 0] = 0
        total = sum(estimates)
        mask = estimates > 0
        diff = (n - total) / sum(mask)
        estimates[mask] += diff

    return estimates
