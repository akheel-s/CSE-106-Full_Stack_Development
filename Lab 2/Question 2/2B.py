import numpy as np

A = np.array([(1, 2, 3), (4, 5, 6), (7, 8, 9)])
B = np.array([(3, 1, 4), (2, 6, 1), (2, 9, 7)])
C = A @ B

print(C)