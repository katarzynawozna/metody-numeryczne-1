import numpy as np

def hilbert_matrix(n):
# Function which creates Hilbert's matrix for n rows and columns
    return np.array([[1 / (i + j + 1) for j in range(n)] for i in range(n)])

# for n = 4
print(hilbert_matrix(4))

# matrix inversion
print(np.linalg.inv(hilbert_matrix(4)))

#for n = 8
print(hilbert_matrix(8))

# matrix inversion
print(np.linalg.inv(hilbert_matrix(8)))

for n in range (5, 21):
    print(np.linalg.det(hilbert_matrix(n)))