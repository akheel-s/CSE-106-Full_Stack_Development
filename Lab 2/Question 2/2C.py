import numpy as np
from numpy import linalg

A = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])

print(linalg.det(A))