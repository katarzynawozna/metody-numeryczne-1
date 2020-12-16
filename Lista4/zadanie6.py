import numpy as np
from scipy import optimize

def f(params):
    x, y = params    
    f1 = np.tan(x) - y - 1
    f2 = np.cos(x) - 3 * np.sin(y)
    return [f1, f2]

roots = []

for x in np.arange(0, 1.5):
    for y in np.arange(0, 1.5):
        roots.append(optimize.fsolve(f, [x, y]))

print(roots)
    
