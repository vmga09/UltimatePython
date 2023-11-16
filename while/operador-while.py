# numero = 1
# while numero < 10:
#     print(numero)
#     numero += 1


# comando = ""
# while comando != "salir":
#     comando = input("$ ")
#     print(comando)


comando = ""
while True:
    comando = input("$ ")
    print(comando)
    if comando.lower() == "salir":
        break
    