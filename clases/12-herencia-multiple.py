class Animal:
    def comer(self):
        print("Comiendo")

class Caminador(Animal):
    def caminar(self):
        print("Caminando")

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