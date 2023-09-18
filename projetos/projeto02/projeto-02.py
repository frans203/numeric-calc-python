# import numpy.linalg as linalg
import numpy as np
from scipy import linalg


def lu_nopivot(A):
    n = np.shape(A)[0] 
    L = np.eye(n) 
    
    for k in np.arange(n):
        L[k+1:n,k] = A[k+1:n,k]/A[k,k]        
        for l in np.arange(k+1,n):
            A[l,:] = A[l,:] - np.dot(L[l,k],A[k,:])
            
    U = A
    return (L,U)

def lu_pivot(A):
    n = np.shape(A)[0]
    L = np.eye(n)
    P = np.eye(n)

    for k in range(n):
        max_index = np.argmax(np.abs(A[k:n, k])) + k
        A[[k, max_index]] = A[[max_index, k]]
        P[[k, max_index]] = P[[max_index, k]]

        L[k + 1:, k] = A[k + 1:, k] / A[k, k]
        for l in range(k + 1, n):
            A[l, k:] = A[l, k:] - L[l, k] * A[k, k:]
    
    U = A
    return P, L, U




A = np.array([[2.04, -1, 0, 0], [-1, 2.04, -1, 0], [0, -1, 2.04, -1], [0,0,-1, 2.04]])
b = np.array([40.8, 0.8, 0.8, 200.8])

L, U = lu_nopivot(A)
print("L) \n", L)
print("")
print("U) \n", U)

y = linalg.solve(L, b)
x = linalg.solve(U, y)
print("\nVetor resultante: ")
print(x)