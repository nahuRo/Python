import os
from pathlib import Path

ruta = os.getcwd() #get current working directory
# os.chdir("") # para cambiar la ruta de lectura del archivo
print(ruta)

base = Path.home()
print(base)
guia = Path("Barcelona","Sagrada_Familia")
print(guia)

total = Path(base,"Barcelona","Sagrada_Familia")

print(f"union {total}")