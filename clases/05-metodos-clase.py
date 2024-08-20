class Perro:

    #Atributo de la clase 
    patas = 4

    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.edad} Guauuu!!!")

    @classmethod
    def habla(cls):
        print(f"Guauuu!!!")

    @classmethod
    def factory(cls):
        return cls("toky",5)
    






Perro.habla()
perro3 = Perro.factory()
print(perro3.edad,perro3.nombre)