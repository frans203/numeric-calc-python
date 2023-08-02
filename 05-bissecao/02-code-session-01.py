import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect 
# # PROBLEMA 1

# def f(x):
#     return x**3 - 3.23*x**2 - 5.54*x + 9.84

# # analise gráfica
# x = np.linspace(-1, 1)
# plt.plot(x, f(x), '-g')
# plt.axhline(y=0, color='b')
# plt.axvline(x=0, color='b');
# plt.show()

# #resolucao com bisect

# xRaiz = bisect(f, 0, 2)
# print(f"Raiz de f: {xRaiz}")

# PROBLEMA 2

# def f(x):
#     return np.cosh(x)*np.cos(x) - 1

# # analise grafica
# x = np.linspace(4, 5)
# plt.plot(x, f(x))
# plt.axvline(x=0, color='r')
# plt.axhline(y=0, color='r')
# plt.show()

# xRaiz = bisect(f, 4, 5)

# print(f"Raiz de f:{xRaiz}")

# PROBLEMA 3:
# def f(x):
#     return np.tan(x) - np.tanh(x)

# x = np.linspace(7, 7.4)
# plt.plot(x, f(x))
# plt.axvline(x=0, color='r')
# plt.axhline(y=0, color='r')
# plt.show()

# xRaiz = bisect(f, 7, 7.4)
# print(f"Raiz de f:{format(xRaiz, '.3f')}")

# Problema 4: 

# def f(x):
#     return np.sin(x) + 3*np.cos(x) - 1

# x = np.linspace(-2, 2)
# plt.plot(x, f(x))
# plt.axvline(x=0, color='r')
# plt.axhline(y=0, color='r')
# plt.show()

# x1 = bisect(f, -2, 0)
# x2 = bisect(f, 0, 2)
# print(f"Raizes de f sao: {x1} e {x2}")
# Problema 5 
# def f(x):
#     return x**4 + 0.9*x**3 - 2.3*x**2 + 3.6*x - 25.2

# x = np.linspace(-5, 5)
# plt.plot(x, f(x))
# plt.axhline(y=0, color='r')
# plt.axvline(x=0, color='r')
# # plt.show()

# x1 = bisect(f, -4, 0)
# x2 = bisect(f, 0, 4)
# print(x1, x2)

# PROBLEMA 6
# j1 = 1.82m
# j2 = 18.2m

# v0 = 15.2
# x = 18.2
# h = 1.82
# y = 2.1
# g = 9.8


# #ele quer o theta para o dado y, ou seja, f(theta) - y tem q dar zero, f(theta) = y, qual teta faz isso?
# #por isso subtraimos o y
# def f(theta):
#     return  x*np.tan(theta) - 0.5*(g*x**2/v0**2)*(1/np.cos(theta)**2) + h - y

# xLins = np.linspace(0.25, 0.50)
# plt.plot(xLins, f(xLins))
# plt.axhline(y=0, color='r')
# plt.axvline(x=0, color='r')
# # plt.show()
# xr = bisect(f, 0.4, 0.5)
# print(np.rad2deg(xr))

#PROBLEMA 7

# q, g, b, h0, h, H
# q, g, b, h0, H
# h = ?



Q = 1.2 # m3/s 
g = 9.81 # m/s2
b = 1.8 # m
h0 = 0.6 # m
H = 0.075 # m

#para ficar mais facil de renomear os valores
def a(Q, g, b, H, h0):
    return Q,g,b,H,h0

def f(h):
    frate,grav,width, bHeight,ups = a(Q,g,b,H,h0)
    c = lambda arg: frate**2/(2*grav*width**2*arg**2)
    #criamos uma função f em função de h, agora para um valor h que zerar f, teremos as raizes ou seja, o valor de h para
    #os parametros da questão 
    return c(h) - c(h0) + h - h0 + H

xLins = np.linspace(0.2, 0.5)
plt.plot(xLins, f(xLins))
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='r')
plt.show()

x1 = bisect(f, 0.2, 0.3)
x2 = bisect(f, 0.4, 0.5)
print(x1, x2)