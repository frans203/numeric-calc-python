import sympy as sp
sp.init_printing(use_unicode=True)

x1, x2, x3 = sp.symbols('x1,x2,x3')

n = 3 

x = sp.zeros(1, n)
A = sp.zeros(n,n)
aux = 0*A

for i in range(n):
    x[i] = sp.symbols('x' + str(i + 1))
    for j in range(n):
        if i == j: #diagonal
            A[i,i] = sp.symbols('a' + str(i + 1) + str(i+1))
        elif j > i:
            aux[i, j] = sp.symbols('a' + str(i+1) + str(j+1))


A = A + aux.T + aux
A = sp.Matrix(A)

x = sp.Matrix(x)
x= x.T

c = (x.T)*A*x
print(sp.expand(c[0]))