import numpy as np
from scipy import linalg

# creating matrices
A = np.array([[4, -2, 1],[-2, 4, -2], [1, -2, 4]])
B = np.array([[4, 2, 0,], [2, 5, 2], [0, 2, 4]])
w = np.array([[1], [-2], [3]])

# mulitply A*B
AB1 = A @ B
# or
AB2 = np.matmul(A, B)

# multiply A*w
Aw = A @ w

# multiply B(A*w)
BAw = np.matmul(B, Aw)

# determinant of matrices an A and B using both numpy and scipy
detA1 = np.linalg.det(A)
detA2 = linalg.det(A)
detB1 = np.linalg.det(B)
detB2 = linalg.det(B)

# inverse of matrices A and B using both numpy and scipy
invA1 = np.linalg.inv(A)
invA2 = linalg.inv(A)
invB1 = np.linalg.inv(B)
invB2 = linalg.inv(B)

