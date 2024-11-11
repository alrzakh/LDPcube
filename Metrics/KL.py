import numpy as np


def kl_divergence(p, q):

    p = np.array(p, dtype=np.float64)
    q = np.array(q, dtype=np.float64)

    mask = (p > 0) & (q > 0)

    kl_div = np.sum(p[mask] * np.log(p[mask] / q[mask]))

    return kl_div
