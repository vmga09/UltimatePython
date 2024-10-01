try:
    n1 = int(input("Ingresa primer número: "))
except Exception as e:
    print("Ingrese un valor que corresponda")
else:
    print("No ocurrió ningún error")
finally:
    print("Siempre se ejecuta")