import numpy as np
from scipy import optimize

def Newton(x, n):
    # where x is a number and n is a root which we want to calculate 
    y = lambda x, a: x ** n - a
    dy = lambda x, a: n * x ** (n - 1)
    return optimize.newton(y, 3, fprime=dy, args=(x,))

x = 32
n = 5

print(Newton(x, n)) 
#2
