lista = [1,2,3,4,5,6]
print(*lista)

lista3 = [7,8,9]


lista2 = (1,2,3,4,5)
print(*lista2)


diccionario = {"a":1,"b":2}
print(*diccionario)
print(diccionario.items)


combinada = [*lista, *lista3]
print(combinada)
