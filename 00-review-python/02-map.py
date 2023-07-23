listResult = list(map(str.capitalize,  ['banana', 'maca', 'laranja']))
# map retorna um mpa object que precisa ser convertido para list
print(listResult)
# frequentemente usa-se lambd com map
listResultMap = list(map(lambda x: x + 2, [1,2,3,4]))
print(listResultMap)