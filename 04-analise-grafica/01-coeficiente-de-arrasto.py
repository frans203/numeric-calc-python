import numpy as np
import matplotlib.pyplot as plt

# Parâmetros fixados 
t = 12.0
v = 42.0
m = 70.0
g = 9.81

# Localização
# a, b = 1,20
# c = np.linspace(a, b, 20) 
# f = g*m/c*(1 - np.exp(-c/m*t)) - v

# plt.plot(c, f, 'g-', c, c*0, 'r--') #UNDERSTAND BETTER THIS ARGUMENTS
# plt.xlabel('c')
# plt.ylabel('f(c)')
# plt.title("Variação do coef de arrasto")
# plt.grid(True)
# plt.show()

# REFINAMENTO
# especie de zoom para obter o intervalo desejado 
a, b = 15.120, 15.140
c = np.linspace(a, b, 100)
f = g*m/c*(1 - np.exp(-c/m*t)) - v
plt.plot(c, f, "g-")
plt.plot(c, c*0, "r--")
plt.grid(True)
plt.show()

