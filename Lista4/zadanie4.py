import numpy as np
from scipy import optimize

def fdz(x):
    return [ x[0] + np.exp(-x[0]) + x[1] ** 3,
             x[0] ** 2 + 2 * x[0] * x[1] - x[1] ** 2 + np.tan(x[0])]

def calc(x):
    y = optimize.root(fdz, x)
    if y.success:
        print(y.x,' ', y.nfev)

# values of x1, x2 and x3 are taken from the plot
x1 = np.array([-1.450, -1.260])
x2 = np.array([-0.750, -0.700])
x3 = np.array([1.200, 1.210])

calc(x1)
calc(x2)
calc(x3)