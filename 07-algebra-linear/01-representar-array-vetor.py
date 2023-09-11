import numpy as np
import numpy.linalg as lin
#vetores: arrays 1d
#matrix: arrays 2d

u = np.array([3, -2, 9])
v = np.array([-2, 4, 0])
w = np.array([1, 0, 0])

arr = np.array([u, v, w])
print('arr: ')
print(arr)

result = np.array([[3, -2, 1],
                    [-2, 4, 0],
                    [9,0,0]
                   ])

l1 = np.array([2, -2])
l2 = np.array([4, 1])
l3 = np.array([2, 1])


result2 = np.array([l1, l2, l3])
# print(result2)

# transposicao
A2T = result2.T
# print(A2T)
# print(np.array([u, v, w]))
AT = np.array([u, v, w]).T
print("\nArr transposta:")
print(AT)
# print(AT)

# teste de igualdade
equal = AT == np.array([u, v, w])
# print(equal)

#adição e subtração

ad = AT + arr
print("\nSoma: ")
print(ad)

sub = AT - arr
print('\nSubtracao: ')
print(sub)


#produtor interno
    #coordenadas de dois vetores mutiplicadas respecitivamente e somadas
pi = np.dot(u, v) #se ambos são um 
print("\nProduto interno")
print(pi)
pi2 = np.dot(np.array([3,1]),np.array([-1,-1]))
print(pi2)

#norma de vetor
 #raiz quadrada do quadrado da soma de cada uma das coordenadas do vetor

norma1 = np.sqrt(np.dot(u, u))
print("\nNorma:")
print(norma1)

#multiplicacao de matrizes

mult1 = np.dot(arr, AT)


#produo matriz vetor
b = np.array([3, 4, 1])
multi2 = np.dot(arr, b)
print("\n Produto matriz vetor")
print(multi2)

#DETERMINANTE
det = lin.det(AT)
print("\nDeterminante")
print(det)

#INVERSA
B2 = np.array([[1,2,3],
              [2,3,4],
              [1,2,0]]) 
B3 = lin.inv(B2)
print("\nInversa:")
print(np.matmul(B3, B2))

# SOLUCAO DE SISTEMAS LINEARES

A = np.array([[-4, 1], [3, 5]])
b = np.array([1/2, 10]).T #transformar em coluna
X = lin.solve(A, b)
print("\nSolucao de um sistema:")
print(X)

#Inversa de matriz
    #apenas para matrizes quadradas de uma dimensão
Ainv = lin.inv(A)
print("\nInversa de uma matriz:")
print(Ainv)

    #realizar prova real do sistema anterior
x2 = np.dot(lin.inv(A), b)
print("\nProva real do sistema anterior:")
print(x2)
print("Comparando x e x2", X == x2)
    #forma mais consistende de computar a norma do vetor erro entre as duas matrriz seria e = b - Ax
e = b - np.dot(A, X)
print("\n verificando os erros mais precisamente")
print(lin.norm(e))
### OBS: Nunca compare dois números reais (float) usando igualdade. Ou seja, x == y, não é, em geral, um bom teste lógico para verificar se x e y possuem o mesmo valor numérico.

#algumas matrizes especiais
#nula=so de zeros
#identidade=1 na diagonal principaç
#matriz de uns=1 em tudo
#triangular inferior = so tem itens da diagonal pra baixo
#triangular superior = so tem itens da diagonal pra cima