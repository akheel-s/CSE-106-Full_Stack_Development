import numpy as np

List = [6, 75, 9, 82, 36, 42, 59, 3, 52, 1, 32, 68, 93, 4, 27, 85, 0, -3, 57]
List1 = np.array(List)
x = List1[List1 > 37]

print(x)