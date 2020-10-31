import numpy as np

def extended_precision(x):
    return np.longdouble((((x ** 4) + 4) ** (1 / 2)) - 2)