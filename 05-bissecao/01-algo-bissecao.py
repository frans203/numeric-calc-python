#f(x)
#estimativas iniciasi: [a, b]
#erro absoluto desejado: e
# N numero maximo de iterações

import inspect, re
import numpy as np
import matplotlib.pyplot as plt
from warnings import warn
from prettytable import PrettyTable as pt
from sympy import symbols, exp, lambdify


def bissecao(f,a,b, tol, N):
    #retorno é a raiz da função
    table = pt()
    #substituição por cada um das funções que vem de f pela correspondente do numpy
    f = re.sub('(sin|sinh|cos|cosh|tan|tanh|exp|log|sqrt|log10|arcsin|arccos|arctan|arcsinh|arccosh|arctanh)', r'np.\1', f)
    # this code searches for a valid Python variable name in the input string f. If it finds one, it extracts that variable name. 
    var = re.search(r'([a-zA-Z][\w]*) ?([\+\-\/*]|$|\))', f).group(1)
    
    #cria uma função anonima baseada no var retornado, variavel independente, de forma dinamica
    f = eval('lambda ' + var + ' :' + f)

    #checa sea função é de uma variavel
    if len(inspect.getfullargspec(f).args) - 1 > 0:
        raise ValueError("O código é valido para apenas uma variável")
    
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
    table.field_names = ['i','xm','f(xm)','a','b','f(a)','f(b)','EA']

    xm = (a + b)/2

    i = 1


    #acaba o loop de duas maneiras: abs(a-b) < tol, ou, encontrando a raiz no else do while
    while abs(a-b) > tol and (not done and N != 0):
        fxm = f(xm)
        #adcionando linha na table
        table.add_row([i,np.round(xm,8),np.round(f(xm),8),
                   np.round(a,4),np.round(b,4),
                   np.round(f(a),4),np.round(f(b),4),
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
    
    table.add_row([i,np.round(xm,8),np.round(f(xm),8),
                   np.round(a,4),np.round(b,4),
                   np.round(f(a),4),np.round(f(b),4),
                   f'{abs(a-b):e}'])
    table.align = 'c'; 
    print(table)

    return xm


def eq_paraq(tempo, massa, vel, grav):

    #você pode usar o sympy dessa maneira para fazer manipulações simbolicas
    g,m,t,v,c = symbols("g,m,t,v,c")

    f = (g*m/c)*(1-exp((-c/m)*t)) - v

    fs = f.subs({'g': grav, 'm': massa, 'v': vel, 't': tempo})

    #expressao simbolica convertida para numerica
    #c como variavel independente
    #fs como função simbolica
    #numpy eh a library usada para gerar a função numerica 
    fn = lambdify(c, fs, 'numpy')
    print(type(fn))
    print(type(fs))

    print(f'Equacao particular: f(c) = {fs}')

    return (fs, fn)

    


# x = np.linspace(-0.2, 1, 100)
# plt.plot(x, -np.arccos(x) + 4*np.sin(x) + 1.7, '-r', x, 0*x, '-g')
# plt.show()


#exemplo 1
# xm = bissecao("-arccos(x) + 4*sin(x) + 1.7", -0.2, 1, 1e-10, 40)

#exemplo 2 

# z = np.linspace(4, 6, 100)
    #o [4, 6] foi definido ao observar o grafico pois
    #queriamos achar o valor da raiz naquele intervalo
    #grafico de multiplas raizes
# plt.plot(z, -z/(1-2*z) - np.tan(z + 1), '-r', z, z*0, '-g')
# plt.show()


# xm = bissecao("-z/(1-2*z) - tan(z + 1)", 4, 6, 1e-5, 100)

# print(xm)

# parâmetros de entrada
tempo, massa, vel, grav = 8, 120, 50, 9.81

# equação particular
fs,fn = eq_paraq(tempo,massa,vel,grav)
c= np.linspace(14, 16, 100)
plt.plot(c, fn(c), c, 0*c)
plt.show()

xm = bissecao(str(fs), 14, 16, 1e-6, 20)
print(xm)