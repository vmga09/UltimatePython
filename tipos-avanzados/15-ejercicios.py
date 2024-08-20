# 1. Eliminar espacio

def elimina_espacios(texto):
    return  [x for x in texto if x != " " ]
     
print(elimina_espacios(" Victor Gonzalez "))


# 2.- Devolver en un diccionario valor de caracteres de un string

def contar_letras(texto):
    dic = {}
    sin_espacio = elimina_espacios(texto.lower())
    for x in sin_espacio:
        dic[x]= sin_espacio.count(x)
    return dic

print(contar_letras(" Hola Soy Victor Gonzalez"))


# 3.- De un diccionario devolver una lista que contenga tupla

def lista_tuplas(texto):
    dic = contar_letras(texto)
    return [(keys,value) for keys , value in dic.items()]

# 4.- devolver las tuplas de mayor valor

def mayor(texto):
    lista = lista_tuplas(texto)
    max = 0
    for x in lista:
        if x[1] > max:
            max = x[1]
    return [x for x in lista if x[1] == max]

print(mayor("lalala"))


# 5.- Crea mensaje que indica los caracteres que se repiten

def set_messages(texto):
    lista = mayor(texto)
    print("Los caracteres que mas se repiten: ")
    for x in  lista:
        print(f"- {x[0].upper()} : {x[1]}")


set_messages("lalala rororo")

    




