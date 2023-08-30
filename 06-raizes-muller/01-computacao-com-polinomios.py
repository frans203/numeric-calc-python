import sympy as sy
import numpy as np
import matplotlib.pyplot as plt

sy.init_printing()

n = 3

x = sy.Symbol('x')
a = [ sy.Symbol('a'+ str(i)) \
     for i in range(0, n+1) ] 
p, dp = 0,0
for j in range(n, -1, -1):
    dp = dp*x + p
    p = a[j] + p*x

dp2 = sy.diff(p, x)

# define valores dos coeficientes aj para o polinômio
# na ordem a0 + a1x + a2x**2 + ...
v = [-1, 2.2,3.5,4]

# escreve o polinômio
pn = p.subs(dict(zip(a,v))) #emparelha os valores de v com os valores de a: -1 com A0 O A1 com 2.2
print(pn)
rc = sy.roots(pn, x, multiple=True) #Multiple faz com que mostre as raizes mesmo sendo repetidas
print(rc)
rr = sy.roots(pn, x, multiple=True, filter='R')
print(rr)

#Avaliando polinomios

## temos que inverter a lista convertida para array, so assim podemos usar o polyval do numpy

vi = np.flip(np.asarray(v), axis=0)
xi = np.pi
result1 = np.polyval(vi, x) #setamos os coeficientes e os valores para colocar nos x com xi
    #note que se usassemos o x aqui então teriamos um valor igual da definição do polinomio

# convertendo de função simbolica para função lambda
f = sy.lambdify(x, pn)
xf = np.linspace(-1, 1, num=20);

#plotagem
plt.axhline(y=f(rr[0]),c='r',ls='--')
plt.axvline(x=rr[0],c='r',ls='--')
plt.plot(xf,f(xf))
plt.plot(rr[0],f(rr[0]),'ro') #single red dot
plt.xlabel('$x$')
plt.ylabel('$P(x)$') #$ garante que a forma será o latex
plt.show()