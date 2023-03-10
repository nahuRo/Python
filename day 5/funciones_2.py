from random import shuffle

# lista inicial
palitos = ['-','--','---','----']

# mezclar palitos
def mezclar(lista):
    shuffle(lista)
    return lista


# pedirle intento
def probar_suerte():
    intento = ''

    while intento not in [1,2,3,4]:
        intento = int(input("elige un numero del 1 al 4: "))

    return intento

# comprobar intento
def chequear_intento(lista,intento):
    if lista[intento -1] == '-':
        print(" ---- a lavar los platos ---- ")
    else:
        print("te salvaste")

    print(f"lo que te toco fue: {lista[intento-1]}")

palitos_mezclados = mezclar(palitos)
seleccion = probar_suerte()

chequear_intento(palitos_mezclados,seleccion)