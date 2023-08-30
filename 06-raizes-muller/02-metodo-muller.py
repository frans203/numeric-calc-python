import sympy as sy
import numpy as np
import matplotlib.pyplot as plt
from numpy import linspace, where, logical_and
def metodo_muller(f, x0, dx, EPS, N):
    if N < 3:
        raise("N deve ser maior que 3")
    #pontos proximos
    x1 = x0 - dx
    x2 = x0 + dx

    #intervalos entre os pontos
    h0 = x1 - x0
    h1 = x2 - x1

    #estimativas das taxas de variação
    d0 = (f(x1) - f(x0))/h0
    d1 = (f(x2) - f(x1))/h1

    # estimativa do coeficiente angular da reta tangente local à curva da funçao
    # nos pontos x1 e x2
    d = (d1 - d0)/(h1 + h0)
    i = 3

    while i<= N:
        b = d1 + h1*d
        
        # discriminante 
        D = (b**2 - 4*f(x2)*d)**0.5        
        
        # Verificando o denominador:
        # Esta condição irá definir o maior denominador
        # haja vista que b + sgn(b)D.
        # (critério de sgn(b))
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D
        
        h = -2*f(x2)/E
        x = x2 + h
        if abs(h) < EPS:
            return x
        
        # atualização
        x0 = x1
        x1 = x2
        x2 = x        
        h0 = x1 - x0
        h1 = x2 - x1
        d0 = (f(x1) - f(x0))/h0
        d1 = (f(x2) - f(x1))/h1
        d = (d1 - d0)/(h1 + h0)
        
        i += 1


#EXEMPLO -01
# f = lambda x: 4*x**3 + 3.5*x**2 + 2.2*x - 1

# raizes = metodo_muller(f, 0.5, 0.5, 1e-5, 100)
# print(raizes)
# X = np.linspace(0.2,1.7,100)
# plt.plot(X, f(X))
# plt.plot(X, 0*f(X))
# plt.axvline(x=raizes.real, c='r', ls='--')
# plt.show()

# EXEMPLO 2
f = lambda x: x**4 - 3*x**3 + x**2 + x + 1
#raizes = metodo_muller(f, -0.5, 0.5, 1e-5, 100) #temos um numero completo 



#Escolhendo estimativas diferentes
c1 = metodo_muller(f, 1.5, 0.5, 1e-5, 100) 
c2 = metodo_muller(f, 2.0, 0.5, 1e-5, 100)

x = np.linspace(-1, 2.8, 50)
plt.plot(x, f(x))
plt.plot(x, 0*f(x), ":")
xi = where(logical_and(x>= -0.5, x<= 0.5))
xi = x[xi]
plt.plot(xi, 0*f(xi), '-g', label='intervalo onde a raiz é complexa')
plt.plot(c1,0,'or',c2,0,'or',label='raiz real')
plt.legend()
plt.show()
#obtivemos raizes complexas no primeiro caso por que o polinomio não intersecta o eixo x