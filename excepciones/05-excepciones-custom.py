class MiError(Exception):
    "Esto es para representar un error"
    def __init__(self, mensaje,codigo ) -> None:
        self.mensaje = mensaje
        self.codigo = codigo



def division(n=0):
    if n == 0:
        raise MiError("No se puede dividir por 0",800)
    return 5/n

try:
    division()
except MiError as e:
    print(e.mensaje,e.codigo)