from numpy.linalg import cholesky

import numpy as np
R = 5.
B = np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ])
L = cholesky(B) 
#Temos B e queremos encontrar a matriz triangular inferior L que ao ser multiplicada pela transposta resulte em B
# print(L)

A = np.matmul(L, L.T)
print(A)