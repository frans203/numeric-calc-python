import numpy as np
from scipy import linalg

# A = np.array([[4,-2,-3,6],[-6,7,6.5,-6],[1,7.5,6.25,5.5],[-12,22,15.5,-1]])
# b = np.array([12,-6.5,16,17])
# x = linalg.solve(A, b)
# print(x)

M = np.array([[1.0,1.5,-2.0],[2.0,1.0,-1.0],[3.0,-1.0,2.0]])
def eliminacao(M):
    m,n = M.shape
    for i in range(m):
        for j in range(i+1,n):
            pivo = M[j,i]/M[i,i]                        
            for k in range(m):
                M[j,k] += -pivo*M[i,k]
    return M

print(eliminacao(M))
M2 = np.random.rand(5,5)
print(eliminacao(M2))