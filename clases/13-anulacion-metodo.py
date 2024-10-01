class Animal:
    def comer(self):
        print("Comiendo Animal")

class Caminador(Animal):
    def caminar(self):
        print("Caminando")

    def comer(self):
        # Llama a los métodos o atributos de la clase padre 
        super().comer()
        print("Camiendo Perro")

class Volador(Animal):
    def volar(self):
        print("Volando")

class Nadador(Animal):
    def nadar(self):
        print("Nadando")

class Perro(Caminador,Nadador):
    def ladrar(self):
        print("Ladrando")

toki = Perro()

toki.comer()