import numpy as np
from numpy import linalg

B = np.array([(3, 1, 4), (2, 6, 1), (2, 9, 7)])

print(linalg.inv(B))