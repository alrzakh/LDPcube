import numpy as np


def norm(est_dist, org_dist):
    estimates = np.copy(est_dist)
    total = sum(estimates)
    n = sum(org_dist)
    domain_size = len(est_dist)
    diff = (n - total) / domain_size
    estimates += diff

    return estimates
