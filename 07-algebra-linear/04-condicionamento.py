import numpy as np
from scipy import linalg

A1 = np.array([[1,2],[1.1,2]])
b1 = np.array([10,10.4])
x1 = linalg.solve(A1, b1)
d = 0.045
A2 = np.array([[1,2],[1.1-d,2]])
b2 = np.array([10,10.4])
print('matriz')
print(A2)
print('vetor')
print(b2)
x2 = linalg.solve(A2, b2)
print(x1)
print(x2)
print(linalg.det(A1),linalg.det(A2))