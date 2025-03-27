import numpy as np


def norm_cut(est_dist, org_dist):
    estimates = np.copy(est_dist)
    order_index = np.argsort(estimates)
    n = sum(org_dist)

    total = 0
    for i in range(len(order_index)):
        total += estimates[order_index[- 1 - i]]
        if total > n:
            break

    for j in range(i + 1, len(order_index)):
        estimates[order_index[- 1 - j]] = 0

    return estimates * n / total
