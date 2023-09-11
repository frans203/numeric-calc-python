import numpy as np

def lu_nopivot(A):
    n = np.shape(A)[0]
    L = np.eye(n)
    for k in np.arange(n):
        L[k + 1:n, k] = A[k + 1:n, k]/A[k,k]
        for l in np.arange(k+1, n):    
            A[l, :] = A[l, :] - np.dot(L[l,k], A[k, :])
    
    U = A
    return (L, U)

A = np.array([[ 4., -2., -3.,  6.],[ 1.,  4.,  2.,  3.],[ 2.,  -3.,  3., -2.],[ 1.,  5.,  3.,  4.]])

L,U = lu_nopivot(A)

print(L)
print(U)