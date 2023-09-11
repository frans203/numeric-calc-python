from numpy.linalg import cholesky
import numpy.linalg as linalg
import numpy as np
R = 5.
D = np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ])
b = np.array([0,0,120]) #matriz dos resultados


def choleskyImplementation(A):
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)

    for i in range(n):
        for j in range(i+1):
            if i == j:
                s = np.sum(L[i, k] ** 2 for k in range(j))
                L[i, j] = np.sqrt(A[i, i] - s)
            else:
                s = np.sum(L[i, k] * L[j, k] for k in range(j))
                L[i, j] = (A[i, j] - s) / L[j, j]

    return L



print(choleskyImplementation(np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ], dtype=float)))
 # fator
L = cholesky(D)
print(L)
# passo 1
# Ly = b
# y = linalg.solve(L, b)

# #passo 2
# #L^t x = y
# x = linalg.solve(L.T, y)

# print(x)