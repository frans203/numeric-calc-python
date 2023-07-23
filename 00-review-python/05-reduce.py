#reduce tem uma função, uma sequencia de valores e um valor inicial
    #elemento atual + atual elemento da sequencia = novo elemento atual
from functools import reduce

def add(x, y):
    return x + y

print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))
print(reduce(add, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 100))

def add_verbose(x, y):
    print("add(x=%s, y=%s) -> %s" % (x, y, x+y)) #dando mais informação sobre o processo
    return x+y
print(reduce(add_verbose, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0))

def add_len(n, s):
        print("add_len(n=%d, s=%s) -> %d" % (n, s, n+len(s))) #len pode ser usado em strings para retornar sua len
        return n+len(s)
print(reduce(add_len, ["Este","e","um","teste."],0))