import numpy as np
from scipy import linalg
A = np.array([[1, 2, 4], [0, 2, 2], [0, 0, 3]])
B = np.array([3, 4, -6])
x = linalg.solve(A, B) #substituição direta 

#depois disso po
print(x)