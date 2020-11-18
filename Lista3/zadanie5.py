import numpy as np
from scipy.linalg import hilbert # Hilbert's matrix generated with Scipy

# Matrix norm

np.linalg.norm(hilbert(5))
np.linalg.norm(hilbert(10))
np.linalg.norm(hilbert(20))

# Condition number of matrices

np.linalg.cond(hilbert(5))
np.linalg.cond(hilbert(10))
np.linalg.cond(hilbert(20))

