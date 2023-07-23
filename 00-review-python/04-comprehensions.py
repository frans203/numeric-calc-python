# criar e modificar listas sem map, filter, lambda
frutas_frescas = [' banana', ' framboesa ', 'maracujá ']
fruits = [item.strip() for item in frutas_frescas] #copia a array
# print(fruits)
vec = [2, 4, 6]
vec2 = [item * 2 for item in vec]
vec3 = [item * 2 for item in vec if item < 2]
vec4 = [item * 2 for item in vec if item > 3]
# print(vec)
# print(vec2)
# print(vec3)
# print(vec4)

#usando o metodo range
    #obs: range gera 10 numeros
arr1 = [x for x in range(0, 10, 2)]
# print(arr1)

print([x for x in range(11) if x > 5])