from pathlib import Path

# Path("/usr/bin")
# Path()
# Path.home()
# Path("one/__init__.py")

path = Path("hola-mundo/mi-archivo.py")
print(path.is_file(),
path.is_dir(),
path.exists())

print(
    path.name,
    "\n",
    path.stem,
    "\n",
    path.suffix,
    "\n",
    path.parent,
    "\n",
    path.absolute()

)

p = path.with_name("chanchito")
print(p)
p = path.with_suffix(".exe")
print(p)
p = path.with_stem("el_archivo")
print(p)