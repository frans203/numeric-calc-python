import time
import numpy
N = 10000000

def timeit(f, args): #uma função e uma tupla
    startTime = time.time()
    y = f(*args) # passa todos os itens da tupla como argumentos de f
    endTime = time.time()
    return endTime - startTime, y

def forloop1(N):
    s = 0
    for i in range(N):
        s += float(i) * float(i)

def forloop2(N):
    y = [0] * N # lista com N elementos preenchidos com 0
    for i in range(N):
        y[i] = float(i) ** 2
    return sum(y)

def listcomp(N):
    return sum([float(x) * x for x in range(N)])

def numpy_(N):
     #arrange retorna uma array com os valores especificados
     # sum retorna a soma dos elementos da array
     # dtype='d' representa o type double
     # cada elemento da lista vai receber **2 
    return numpy.sum(numpy.arange(0, N, dtype='d') ** 2)


timings = []
print("N =", N)
forloop1_time, f1_res = timeit(forloop1, (N,))
timings.append(forloop1_time)
print("for-loop1", forloop1_time)
forloop2_time, f2_res = timeit(forloop2, (N,))
timings.append(forloop2_time)
print("for-loop2", forloop2_time)
listcomp_time, lc_res = timeit(listcomp, (N,))
timings.append(listcomp_time)
print("listcomp", listcomp_time)
numpy_time, n_res = timeit(numpy_, (N,))
timings.append(numpy_time)
print("numpy", numpy_time)

print("O metodo mais lento eh {:.10f} vezes mais lento do que o metodo mais rapido.".format(
max(timings)/min(timings)))