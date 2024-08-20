class Perro:

    #Atributo de la clase 
    patas = 4

    def __init__(self, nombre,edad):
        self.nombre = nombre
        self.edad = edad

    def ladrar(self):
        print(f"{self.edad} Guauuu!!!")


mi_perro = Perro("Docky",5)
print(mi_perro.nombre)
mi_perro.ladrar()
print(mi_perro.patas) 