import numpy as np;
import matplotlib.pyplot as plt


# Um algoritmo em força bruta 
# deverá percorrer todos os pontos sobre a curva e 
# verificar se um ponto está abaixo do eixo e seu sucessor imediato está acima, 
# ou vice-versa. Se isto ocorrer, então deve haver uma raiz neste intervalo.

f = lambda x: np.exp(-x**2)*np.cos(3*x)
x = np.linspace(0, 4, 1000) 
# usando x = np.linspace(3.6, 3.7, 1000) conseguimos provar que existe uma 4a raiz sim


def forca_bruta(f, a, b, n):
    x = np.linspace(a, b, n)
    y = f(x) #resultado de f sendo aplicado aos pontos do linspace. resulta em uma array de resultados
    raizes = []
    for i in range(n - 1):
        if y[i]*y[i+1] < 0:
            raiz = x[i] - ((x[i+1] - x[i])/(y[i+1] - y[i]))*y[i]
            raizes.append(raiz)
    
    if len(raizes) == 0:
        print("Nenhuma raiz foi encontrada")
    return raizes

a, b, n = 0, 4, 1000
raizes = forca_bruta(f, a, b, n)
print(raizes)

plt.plot(x, f(x), 'r', x, 0*f(x), 'g:', raizes, np.zeros(4), 'ok')
plt.grid()
plt.xlabel('$x$',fontsize=14)
plt.ylabel('$f(x)$',fontsize=14)    
plt.title('Raízes de $e^{-x^2}\cos(3x)$')
plt.show()