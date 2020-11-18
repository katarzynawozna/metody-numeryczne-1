import numpy as np
from scipy import linalg

A = np.array([[0, 0, 2, 1, 2], 
            [0, 1, 0, 2, -1],
            [1, 2, 0, -2, 0],
            [0, 0, 0, -1, 1],
            [0, 1, -1, 1, -1]])

b = np.array([[1],
            [1],
            [-4],
            [-2],
            [-1]])

x = linalg.solve(A, b)