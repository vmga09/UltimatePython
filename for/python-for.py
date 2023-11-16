for x in range(5):
    print(f" X es : {x}")
    

data = [(1,2),(3,4),(5,6)]
    
for x,y in data:
    print(f" {x} e {y}")
    
buscar = 5
for numero in range(10):
    if numero == buscar:
        print(f"Encontrado {numero}")
        break
    
    
buscar = 7
for numero in range(5):
    if numero == buscar:
        print(f"Encontrado {numero}")
        break
else:
     print("Numero no encontrado")