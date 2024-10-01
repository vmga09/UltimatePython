class Perro:
    def __init__(self, nombre,edad):
        # Con doble "_" se converte en una propiedad privada.
        self.__nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.__nombre} dice Guauuu!!!")

    def get_nombre(self):
        return self.__nombre


    @classmethod
    def factory(cls):
        return cls("toky",5)
    







perro3 = Perro.factory()
print(perro3.get_nombre())
print(perro3.__nombre)