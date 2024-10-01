class Producto:
    def __init__(self,nombre,precio) -> None:
        self.nombre = nombre
        self.precio = precio
        
    def __str__(self) -> str:
        return f"Producto:  {self.nombre} Precio: {self.precio}"




class Categoria:
    productos = list()
    def __init__(self,nombre,productos) -> None:
        self.nombre = nombre
        self.productos = productos
    
    def agregar(self,producto):
        self.productos.append(producto)
        
    def imprimir(self):
        for x in self.productos:
            print(x)



kayak = Producto("kayak",1000)
pelota = Producto("pelota",200)
bicicleta = Producto("Bicicleta",1000)

deportes = Categoria("Deportes",[kayak,pelota])
deportes.agregar(bicicleta)
deportes.imprimir()

