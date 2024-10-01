from pathlib import Path
path = Path("rutas")

for _p in path.iterdir():
    print(_p.exists())

for _p in path.iterdir():
    print(_p.suffix)

archivos = [p.name for p in path.iterdir() if not p.is_dir()]
archivos2 = [p.name for p in path.glob("*.py")]

print(archivos)
print(archivos2)