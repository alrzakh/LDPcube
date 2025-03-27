import numpy as np

def earth_movers_distance(p, q):

    p = np.array(p)
    q = np.array(q)
    
    cdf_p = np.cumsum(p)
    cdf_q = np.cumsum(q)
    
    emd = np.sum(np.abs(cdf_p - cdf_q))
    
    return emd
