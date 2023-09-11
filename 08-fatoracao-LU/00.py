import numpy as np
from scipy import linalg
A = np.array([[1, 0, 0], [3, 1, 0], [2, 1, 1]])
B = np.array([3, 13, 4])
x = linalg.solve(A, B) #substituição direta 

#depois disso po
print(x)