import numpy as np
import matplotlib.pyplot as plt


def simulacao_F(b,t,L,U):
    x = []
    epsm = b**(1-t) # epsilon de máquina
    M = np.arange(1.,b-epsm,epsm)

    E = 1
    for e in range(0,U+1):
        x = np.concatenate([x,M*E])
        E *= b    
    E = b**(-1)
    
    y = []
    for e in range(-1,L-1,-1):
        y = np.concatenate([y,M*E])
        E /= b    
    yy = np.asarray(y)
    xx = np.asarray(x)    
    x = np.concatenate([yy,np.array([0.]),xx])
    return x

Y = simulacao_F(2, 3, -5, 5)
X = np.zeros(Y.shape)


# plotagem
fig, ax = plt.subplots(figsize=(8,1),constrained_layout=True)
ax.scatter(Y,X,marker='o');
ax.get_yaxis().set_visible(False)
plt.show()