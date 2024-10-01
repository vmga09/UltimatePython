class Perro:
    def __init__(self, nombre,edad=6):
        self.__nombre = nombre
        self.edad = edad

    def set_nombre(self,nombre):
        if nombre.strip():
            self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre



perro = Perro("Toqui")
perro.set_nombre("Mandinga")
print(perro.get_nombre())
