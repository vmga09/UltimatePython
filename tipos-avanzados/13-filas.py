from collections import deque

lista = [1,2,3,4,5]

fila = deque(lista)
fila.append(6)
print(fila)
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
fila.popleft()
print(fila)
fila.popleft()
print(fila)
if not fila:
    print("No hay elementos")



