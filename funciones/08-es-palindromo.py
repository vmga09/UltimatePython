def eliminar_espacio(texto):
    new_texto = texto.lower().replace(" ","")
    return new_texto


def comparar(texto):
    new_texto = eliminar_espacio(texto)
    texto_reves = ""
    x=len(new_texto)
    while x >= 1:
        texto_reves += new_texto[x-1]
        x -=1
        
    print(texto_reves)
    if new_texto == texto_reves:
        return True
    else:
        return False
    
    
    
print("Hola", comparar("a b b a"))
