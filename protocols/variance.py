import numpy as np


def calculate_variances(protocol, epsilon, domain_size, population_size):
    
    e_eps = np.exp(epsilon)
    
    var = 0
    if protocol == "grr" or protocol == "subset":
        nominator = e_eps * domain_size - 2
        denominator = population_size * ((e_eps - 1) ** 2)
        var = nominator / denominator
    elif protocol == "rappor":
        nominator = np.exp(epsilon / 2)
        denominator = population_size * ((np.exp(epsilon / 2) - 1) ** 2)
        var = nominator / denominator
    elif protocol == "oue" or protocol == "olh":
        
        nominator = 4 * e_eps
        denominator = population_size * ((e_eps - 1) ** 2)
        var = nominator / denominator
        
    elif protocol == "blh":
        nominator = (e_eps + 1) ** 2
        denominator = population_size * ((e_eps - 1) ** 2)
        var = nominator / denominator

    return var
