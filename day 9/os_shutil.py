import os
import shutil

# para saber donde estoy parado
print(os.getcwd())

# para escribir/crear un archivo
archivo = open("curso.txt", "w")
archivo.write("archivo de prueba")
archivo.close()

# shutil, para mover archivos
# shutil.move("curso.txt","lugar a donde lo voy a mover")

# os.walk("ruta"), lo uso para poder ver los elementos en un arbol de carpetas, archivos en el order: carpeta, subcarpeta, archivo

