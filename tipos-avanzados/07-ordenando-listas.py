numeros = [2,1,5,22,6,23,9,25]

numeros.sort(reverse=True)
print(numeros)

numeros = [2,1,5,22,6,23,9,25]
numeros_sor = sorted(numeros)
print(numeros_sor)

# numeros.reverse()





# print(numeros)

new_lista = [["perro", 30], ["juan", 10], ["maria", 20]]

def ordena(element):
    return element[1]



new_lista.sort(key=ordena)

print(new_lista)