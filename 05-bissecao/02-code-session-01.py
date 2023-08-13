import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect 
import math
from prettytable import PrettyTable as pt
from sympy import symbols, exp, lambdify, sqrt, coth, Abs, tan

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
# plt.show()
# xr = bisect(f, 0.4, 0.5)
# print(np.rad2deg(xr))

#PROBLEMA 7

# q, g, b, h0, h, H
# q, g, b, h0, H
# h = ?



# Q = 1.2 # m3/s 
# g = 9.81 # m/s2
# b = 1.8 # m
# h0 = 0.6 # m
# H = 0.075 # m

# #para ficar mais facil de renomear os valores
# def a(Q, g, b, H, h0):
#     return Q,g,b,H,h0

# def f(h):
#     frate,grav,width, bHeight,ups = a(Q,g,b,H,h0)
#     c = lambda arg: frate**2/(2*grav*width**2*arg**2)
#     #criamos uma função f em função de h, agora para um valor h que zerar f, teremos as raizes ou seja, o valor de h para
#     #os parametros da questão 
#     return c(h) - c(h0) + h - h0 + H

# xLins = np.linspace(0.2, 0.5)
# plt.plot(xLins, f(xLins))
# plt.axhline(y=0, color='r')
# plt.axvline(x=0, color='r')
# plt.show()

# x1 = bisect(f, 0.2, 0.3)
# x2 = bisect(f, 0.4, 0.5)
# print(x1, x2)


import inspect, re

def bissecao(f,a,b, tol, N):
    #retorno é a raiz da função
    table = pt()
    fa = f(a)
    fb = f(b)
    if fa*fb >= 0:
        raise ValueError('A função deve ter sinais opostos em a e b!')
    
    done = False

    #numero minimo de iterções 
    niter = int(np.ceil(np.log((b-a)/tol)/np.log(2)))

    if N < niter:
        print(f'! São necessárias pelo menos {niter} iterações, mas N = {N}.\n')

    #header da tabela
    table.field_names = ['i','em','f(em)','a','b','f(a)','f(b)','EA']

    xm = (a + b)/2
    print(xm)

    i = 1


    #acaba o loop de duas maneiras: abs(a-b) < tol, ou, encontrando a raiz no else do while
    while abs(a-b) > tol and (not done and N != 0):
        fxm = f(xm)
        #adcionando linha na table
        table.add_row([i,xm,f(xm),
                   a,b,
                   f(a),f(b),
                   f'{abs(a-b):e}'])

        if fxm*fa > 0:
            a = xm
            fb = fxm
            xm = (a + b)/2
        elif fxm*fa < 0:
            b = xm
            fb = fxm
            xm = (a + b)/2
        else:
            done = True
        N -= 1
        i += 1
    
    table.add_row([i,xm,f(xm),
                   a,b,
                   f(a),f(b),
                   f'{abs(a-b):e}'])
    table.align = 'c'; 
    print(table)

    return xm

m = 9 / 10**31 #kg
h = 6.6 / 10 ** 34 #J*s jaule X segundo
a = 1 / 10**10 #m
v = 1.1215 / 10 **19 #joule


# m = 9 #kg
# h = 6.6  #J*s jaule X segundo
# a = 1  #m
# v = 1 #joule
#radianos
def cotang(angle):
    return 1/np.tan(angle)

def auxCotangTun(e):
    return (np.sqrt(2*m*e)*a)/h

def func(x):
    return x

def f(e):
    return (np.sqrt(2*m*e)/h)*cotang(auxCotangTun(e))

def g(e):
    return np.sqrt(2*m*(np.abs(v-e)))/h

def t(e):
    return f(e) + g(e)


# def tunelamento(e):
#     return (np.sqrt(2*m*e)/h)*cotang(auxCotangTun(e)) + np.sqrt(2*m*(np.abs(v-e)))/h

xLins = np.linspace(4 /10 ** 20, 20000 /10 ** 20)
# xLins = np.linspace(1.25 / 10 ** 16, 1.35 / 10 ** 16)
plt.plot(xLins, t(xLins), 'g')
# plt.plot(xLins, -g(xLins), 'k')
plt.axhline(y=0, color='r')
plt.axvline(x=0, color='r')
plt.show()

# def eqLambidyBisect(massa, plank, ac, ve):
#     #você pode usar o sympy dessa maneira para fazer manipulações simbolicas
#     m,h,a,v,e = symbols("m,h,a,v,e")

#     u = (sqrt(2*m*e)/h)*1/tan((sqrt(2*m*e)*a)/h) + (sqrt(2*m*(Abs(v-e)))/h)

#     fs = u.subs({'m': massa, 'h': plank, 'a': ac, 'v': ve})

#     #expressao simbolica convertida para numerica
#     #c como variavel independente
#     #fs como função simbolica
#     #numpy eh a library usada para gerar a função numerica 
#     fn = lambdify(e, fs, 'numpy')
#     return (fs, fn)

    




# x1 = bissect(str(t), 1.25 / 10 ** 16, 1.35 / 10 ** 16, 1/10**16, 30)
# print(x1)
# fs,fn = eqLambidyBisect(m, h, a, v)
xm = bissecao2(t , 1.25 / 10 ** 16, 1.35 / 10 ** 16, 1/10**20, 30) 
print(xm)
# print(tunelamento(4 /10 ** 20))

