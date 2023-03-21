import os 
import re
import time
import datetime
from pathlib import Path
import math

inicio = time.time()

base = os.getcwd() # obtengo ruta base a estos archivos
ruta_total = Path(base,"day 9","Mi_Gran_Directorio") # obtengo la ruta real a lo que quiero usar

patron = r'N\D{3}-\d{5}' # creo expresion regular
mi_date =  datetime.date.today() # me devuelve la fecha actual

numeros_encontrados = []
archivos_encontrados = []

def busqueda_patron(archivo, patron):
    este_Archivo = open(archivo,"r") # abro el achivo recibido
    text = este_Archivo.read()

    if re.search(patron, text):
        return re.search(patron, text)
    
    return ''

def crear_listas():
    for carpeta, subcarpeta, archivo in os.walk(ruta_total):
        for a in archivo:
            resultado = busqueda_patron(Path(carpeta,a), patron)
            if resultado != '':
                numeros_encontrados.append(resultado.group()) 
                archivos_encontrados.append(a.title())


def mostrar_todo():
    indice = 0
    print("-" * 50)
    print(f"fecha de busqueda: {mi_date.day}/{mi_date.month}/{mi_date.year}")
    print("\n")
    print("Archivo \tNro. Serie")
    print("------------- \t---------")
    for a in archivos_encontrados:
        print(f"{a}\t{numeros_encontrados[indice]}")
        indice += 1
    print("\n")
    print(f"Números encontrados: {len(numeros_encontrados)}")
    fin = time.time()
    duracion = fin - inicio
    print(f"Duracion de la busqueda: {math.ceil(duracion)} seg")
    print("-" * 50)


crear_listas()
mostrar_todo()





