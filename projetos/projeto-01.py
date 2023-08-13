import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import bisect 
from prettytable import PrettyTable as pt


#METODO DA BISSECAO
#Passamos a função, dois pontos onde a raiz pode estar, tolerancia e numero de passos
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
h = 6.6 / 10 ** 34 #jaule X segundo
a = 1 / 10**10 #m/s^2
v = 1.1215 / 10 **19 #joule

#equacao auxiliar da cotang
#radianos
def cotang(angle):
    return 1/np.tan(angle)

#equacao auxiliar do valor em rad da tg
def auxCotangTun(e):
    return (np.sqrt(2*m*e)*a)/h

#parte um da equacao
def f(e):
    return (np.sqrt(2*m*e)/h)*cotang(auxCotangTun(e))

#parte dois da equacao
def g(e):
    return np.sqrt(2*m*(e-v))/h

#equacao inteira
def t(e):
    return f(e) + g(e)

xLins = np.linspace(4 /10 ** 20, 20000 /10 ** 20)
plt.xlabel('e')
plt.ylabel('t(e)')
plt.plot(xLins, t(xLins), color='#800080', label='Schrodinger')
# plt.plot(xLins, f(xLins), 'g', label='Schrodinger-1')
# plt.plot(xLins, -g(xLins), 'r', label='Schrodinger-2')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title("Schrodinger")
plt.legend()
plt.grid()
plt.show()
    
x1 = bisect(t, 1.25 / 10 ** 16, 1.35 / 10 ** 16)
xm = bissecao(t , 1.25 / 10 ** 16, 1.35 / 10 ** 16, 1/10**20, 30) 
print(xm)
print(x1)

