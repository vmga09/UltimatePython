# agregar * a los argumentos los vuelve iterables

def suma(*numeros):
    resultados = 0
    for numero in numeros:
        resultados +=  numero
    print(f"El resultado es: {resultados}")
    
suma(2,3,4,5,6,7)