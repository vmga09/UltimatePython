new_lista = [["perro", 30], ["juan", 10], ["maria", 20]]

# def ordena(element):
#     return element[1]


#Funcion lambda
new_lista.sort(key= lambda element: element[1])

print(new_lista)