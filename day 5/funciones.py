# funcion que no devuelve nada
def saludar(nombre):
    """
    soy un comentario de varios lineas
    """
    print(f"Hola {nombre}")

saludar("agus")

# funcion que devuelve algo
def sumar(num1,num2):
    return num1 + num2

print(sumar(12,21)) 

# funciones dinamicas
def chequear_3_cifras(lista):
    lista_3 = []

    for n in lista:
        if n in range(100,1000):
            lista_3.append(n)
        else:
            pass

    return lista_3


resultado = chequear_3_cifras([545,99,923])
print(f"chequear_3_cifras --> {resultado}")

# ejemplo para el uso de funciones
precios_cafe = [("capuchino",1.5),("expreso",1.2),("moka",1.9)]

def cafe_caro(precios):
    precio_mayor = 0
    cafe_mas_caro = ""

    for cafe,precio in precios:
        if precio > precio_mayor:
            precio_mayor = precio
            cafe_mas_caro = cafe
        
    return (cafe_mas_caro,precio_mayor)

print(cafe_caro(precios_cafe))