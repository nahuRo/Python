import os
from pathlib import Path
from os import system

ruta = os.getcwd()
mi_ruta = Path(Path.home(),"Desktop","Python","Day 6","Recetas")

def contar_receta(ruta):
    contador = 0
    for txt in Path(ruta).glob("**/*.txt"):
        contador += 1
    return contador

def mostrar_cat(ruta):
    print("\n\nCategorias: ")
    ruta_cat = Path(ruta)
    lista_cat = []
    contador = 1

    for carpeta in ruta_cat.iterdir():
        carpeta_name = str(carpeta.name)
        print(f"[{contador}] - {carpeta_name}")
        lista_cat.append(carpeta)
        contador += 1

    return lista_cat

def elegir_cat(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input("\nElija una categoria: ")

    return lista[int(eleccion_correcta) - 1]

def mostrar_recetas(ruta):
    print("\n\nEstas son las recetas disponibles")
    ruta_recetas = Path(ruta)
    lista_recetas = []
    contador = 1

    for receta in ruta_recetas.glob("*.txt"):
        receta_str = str(receta.name)
        print(f"[{contador}] - {receta_str}")
        lista_recetas.append(receta)
        contador += 1
    
    return lista_recetas

def eleccion_recetas(lista):
    eleccion_correcta = "x"

    while not eleccion_correcta.isnumeric() or int(eleccion_correcta) not in range(1,len(lista) + 1):
        eleccion_correcta = input("\nElija una receta: ")

    return lista[int(eleccion_correcta) - 1]

def leer_receta(receta):
    print(Path.read_text(receta))

def crear_receta(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la receta: ")
        nombre_receta = input() + ".txt"

        print("Escribe el contenido de la receta: ")
        contenido_receta = input()

        ruta_nueva = Path(ruta, nombre_receta)

        if not os.path.exists(ruta_nueva):
            Path.write_text(ruta_nueva, contenido_receta)
            print(f"la receta con el nombre: {nombre_receta} ha sido creada exitosamente")
            existe = True
        else:
            print("Lo siento, esa receta ya existe")

def crear_cat(ruta):
    existe = False

    while not existe:
        print("Escribe el nombre de la nueva categoria: ")
        nombre_categoria = input() 

        ruta_nueva = Path(ruta, nombre_categoria)

        if not os.path.exists(ruta_nueva):
            Path.mkdir(ruta_nueva)
            print(f"la nueva categoria: {nombre_categoria} ha sido creada exitosamente")
            existe = True
        else:
            print("Lo siento, esa categoria ya existe")

def eliminar_receta(receta):
    Path(receta).unlink()
    print(f"La receta {receta.name} ha sido eliminada")

def eliminar_cat(categoria):
    Path(categoria).rmdir()
    print(f"La categoria {categoria.name} ha sido eliminda")

def volver_home():
    eleccion_regresar = 'x'

    while eleccion_regresar.lower() != 'v':
        eleccion_regresar = input("\nIngrese 'v' para volver al menu: ")

def menu():
    system("cls")
    eleccion_menu = 'x'

    while not eleccion_menu.isnumeric() or int(eleccion_menu) not in range(1,7):
        print(f"""
                ---- Menu ----
            [1] - Leer receta
            [2] - Crear receta
            [3] - Crear categoria
            [4] - Eliminar receta
            [5] - Eliminar categoria
            [6] - Finalizar programa

            Total recetas: {contar_receta(mi_ruta)}
            Direccion de recetas: {mi_ruta}
        """)
        eleccion_menu = input("Eliga una opcion: ")
        
    return eleccion_menu


# *** MAIN ***

finalizar_programa = False

while not finalizar_programa:
    inicio = menu()
    match inicio:
        case "1":
            # mostrar categorias
            mis_cat = mostrar_cat(mi_ruta)
            
            # elegir categorias
            mi_cat = elegir_cat(mis_cat)

            # mostrar recetas
            mis_recetas = mostrar_recetas(mi_cat)

            if len(mis_recetas) < 1:
                print("no hay recetas en esta categoría.")
            else:
                # elegir receta 
                mi_receta = eleccion_recetas(mis_recetas)

                # leer receta
                leer_receta(mi_receta)
            
            # volver inicio
            volver_home()
        case "2":
            # mostrar categorias
            mis_cat = mostrar_cat(mi_ruta)
            
            # elegir categorias
            mi_cat = elegir_cat(mis_cat)

            # crear receta
            crear_receta(mi_cat)

            # volver inicio
            volver_home()
        case "3":
            # crear cat
            crear_cat(mi_ruta)

            # volver inicio
            volver_home()
        case "4":
            # mostrar categorias
            mis_cat = mostrar_cat(mi_ruta)
            
            # elegir categorias
            mi_cat = elegir_cat(mis_cat)

            # mostrar recetas
            mis_recetas = mostrar_recetas(mi_cat)
            
            if len(mis_recetas) < 1:
                print("no hay recetas en esta categoría.")
            else:
                # elegir receta 
                mi_receta = eleccion_recetas(mis_recetas)

                # eliminar receta
                eliminar_receta(mi_receta)
            
            # volver inicio
            volver_home()
        case "5":
            # mostrar categorias
            mis_cat = mostrar_cat(mi_ruta)
            
            # elegir categorias
            mi_cat = elegir_cat(mis_cat)

            # eliminar cat
            eliminar_cat(mi_cat)

            # volver inicio
            volver_home()
        case "6":
            finalizar_programa = True
            print("Hasta Luego!")


