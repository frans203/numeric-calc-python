from numpy.linalg import cholesky
import numpy as np
R= 5.
B = np.array([ [50+R,-R,-30],[-R,65+R,-15],[-30,-15,45] ])

C = np.tril(B) - 60
C = np.tril(C) + np.tril(C,-1).T

#cholesky(C) erro pois não é positiva definida

D = np.tril(B) + 1
D = np.tril(D) + np.tril(D,-1).T
print(cholesky(D))