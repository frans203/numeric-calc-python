# Aplica a função f a todos os elementos em uma sequencia s
# A função f deve retornar True ou False.
def biggerThan5(x):
    if x > 5:
        return True
    else:
        return False

filteredList = list(filter(biggerThan5, [2,3,12,312]))
print(filteredList)

#usando lambda

filteredList2 = list(filter(lambda x:x>5, [2,3,12,312]))
print(filteredList2)