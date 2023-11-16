numero = ""
operacion = ""


while numero != "Salir" or operacion != "Salir":
    if numero == "":
        numero = float(input("Ingrese numero\n"))
        operacion = input("Ingrese operacion\n")
        numero_sig = float(input("Ingrese numero siguiente\n"))
        if operacion.lower() == "suma":
            numero = numero + numero_sig
            print(f"El resultado es: {numero}")
        elif  operacion.lower() == "resta":
            numero = numero - numero_sig
            print(f"El resultado es: {numero}")
        elif operacion.lower() == "multi":
            numero = numero * numero_sig
            print(f"El resultado es: {numero}")
        elif operacion.lower() == "div":
            numero = numero / numero_sig
            print(f"El resultado es: {numero}")
        elif operacion.lower() == "salir":
            break
        else:
            print(f"Ingrese una operacion válida")
    else:
        operacion = input("Ingrese operacion\n")
        numero_sig = float(input("Ingrese numero siguiente\n"))
        if operacion.lower() == "suma":
            numero = numero + numero_sig
            print(f"El resultado es: {numero}")
        elif  operacion.lower() == "resta":
            numero = numero - numero_sig
            print(f"El resultado es: {numero}")
        elif operacion.lower() == "multi":
            numero = numero * numero_sig
            print(f"El resultado es: {numero}")
        elif operacion.lower() == "div":
            numero = numero / numero_sig
            print(f"El resultado es: {numero}")
        elif operacion.lower() == "salir":
            break
        else:
            print(f"Ingrese una operacion válida")