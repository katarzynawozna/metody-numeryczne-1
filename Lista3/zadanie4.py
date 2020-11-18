import numpy as np
from scipy import linalg

def guass_elimination(A, B):
    #Ax = B, A and B should be np.array() objects

    n = len(B)
    x = np.zeros(n)

    #Elimination
    for k in range(n-1):
        if np.fabs(A[k, k]) < 1.0e-12:
            for i in range(k+1, n):
                if np.fabs(A[i, k]) > np.fabs(A[k, k]):
                    A[[k, i]] = A[[i, k]]
                    B[[k, i]] = B[[i, k]]
                    break
        for i in range(k+1, n):
            if A[i, k] == 0:
                continue
            factor = A[k, k] / A[i, k]
            for j in range(k, n):
                A[i, j] = A[k, j] - A[i, j] * factor
            B[i] = B[k] - B[i] * factor
    
    #Back-substitution
    x[n-1] = B[n-1] / A[n-1, n-1]
    for i in range(n-2, -1, -1):
        sum_Ax = 0
        for j in range(i+1, n):
            sum_Ax += A[i, j] * x[j]
        x[i] = (B[i] - sum_Ax) / A[i, i]
    return x


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

x1 = linalg.solve(A, b)
x2 = guass_elimination(A, b)

print(f"Build-in function from scipy gives {x1}")
print(f"My function gauss_elimination() gives {x2}")
