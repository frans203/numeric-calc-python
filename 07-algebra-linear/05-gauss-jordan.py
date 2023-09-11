import numpy as np
from scipy import linalg

AB = np.array([[3. , -0.1, -0.2, 7.85], [0.1, 7., -0.3, -19.3], [0.3, -0.2, 10., 71.4]])

print("array:")
print(AB)

# a11 é o elemento pivô da primeira equação, a22 da segunda e assim por diante

# Normalização da 1a. linha
AB[0,:] /= AB[0,0] # L1 <- L1/a11

#remove o primeiro termo da segunda e terceira linha
m1 = AB[1,0]
AB[1, :] -= m1*AB[0, :] 
m2 = AB[2, 0]
AB[2, :] -= m2*AB[0, :]

# normalizando a segunda linha 
AB[1, :] /= AB[1, 1]

#elimina o x2 da 1 e 3a linhas

m3 = AB[0, 1]
AB[0,:] -= m3*AB[1, :] 
m4 = AB[2, 1]
AB[2,:] -=m4*AB[1, :]

#elimina o x3 da 1 e 2 linha

AB[2, :] /= AB[2, 2]


m5 = AB[0,2]
AB[0, :] -= m5*AB[2, :]
m6 = AB[1, 2]
AB[1, :] -= m6*AB[2, :]
print(AB) #x1 é 3, x2 eh -2.5 e x3 eh 7