class Perro:
    def __init__(self, nombre,edad=6):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return f"Clase perro: {self.nombre}"

    # def set_nombre(self,nombre):
    #     if nombre.strip():
    #         self.nombre = nombre

    # def get_nombre(self):
    #     return self.nombre



perro = Perro("Toqui")

texto = str(perro)
print(texto)

#perro.set_nombre("Mandinga")
#print(perro.get_nombre())