import numpy as np


def base_pos(est_dist, org_dist=None):
    estimates = np.copy(est_dist)
    estimates[estimates < 0] = 0
    return estimates

