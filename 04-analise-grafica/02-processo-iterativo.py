import numpy as np;
import matplotlib.pyplot as plt

N  = 20

x = [1/2]

print(f'x(0) = {x[0]}')

for k in range(1, N):
    phi = x[k-1]**1/2/np.pi - x[k-1]
    x.append(phi)
    print(f'x({k}) = {phi:.4f}')

plt.figure(figsize=(8,3)) #tuple representando dimensões da figure
plt.plot(x,'go',label=r'$\dfrac{ (x^{(k)})^{1/2}}{\pi} - x^{(k)}$') #plot with the expression
plt.xticks(range(N)) #unidades do x 
plt.xlabel('$x^{(k)}$',fontsize=12)
plt.ylabel('$\phi_1^{(k)}$',fontsize=12)
plt.grid(axis='both')
plt.legend(loc='upper right')
plt.show()