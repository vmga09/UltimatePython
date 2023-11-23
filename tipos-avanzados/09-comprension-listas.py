new_lista = [["perro", 30], ["juan", 10], ["maria", 20]]



nombres = [x[0] for x in new_lista ]
valor = [x[1] for x in new_lista]
print(nombres)
print(valor)



new_nombres = [x[0] for x in new_lista if x[1] > 21 ]
print(new_nombres)


nnombres = list(map(lambda x:x[0],new_lista))

fnombres = list(filter(lambda x:x[1] > 21,new_lista))

print(nnombres)
print(fnombres)