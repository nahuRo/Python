def suma():
    n1 = int(input("Primer numero: "))
    n2 = int(input("Segundo numero: "))

    print(n1 + n2)
    print("Gracias por sumar")


try:
    # intento con este codigo
    suma()
except TypeError:
    # manejo los errores
    # atajo errores de tipo TypeError
    print("Estas intentando concatenar tipos distintos")
except ValueError:
    # atajo errores de tipo ValueError
    print("Ese no es un numero")
else:
    # si a ejecutar si no hay error aparte del que esta en try
    print("Hiciste todo bien")
finally:
    # independientemente lo que pase, ejecuto este codigo
    print("Eso fue todo")


def pedir_numero():
    
    while True:
        try:
            numero = int(input("Dame un numero: "))
        except:
            print("Ese no es un numero")
        else:
            print(f"Ingresaste el numero {numero}")
            break # salgo del bucle

    print("Gracias")