
#Inyeccion dependencia Clase
# class Perro(Correa):
#     def __init__(self):
#         self.correa = Correa()

#Inyeccion dependencia función
# def guardar(entidad):
#     entidad.guardar()


# def init_app(bbdd, api):
    #inicializacion del modulo

from pathlib import Path

path = Path()
paths = [_p for _p in path.iterdir() if _p.is_dir()]

dependencias = {
    "db": "base de datos",
    "api": "API rest",
    "grafql": " Esto es grafql"
}

def load(_p):
    paquete = __import__(str(_p).replace("/","."))
    try:
        paquete.init()
    except:
        print("el paquete no tiene init")

list(map(load,paths))



    


