"""
1 - Crea una función llamada devolver_distintos() que reciba 3
integers como parámetros.
Si la suma de los 3 numeros es mayor a 15, va a devolver el
número mayor.
Si la suma de los 3 numeros es menor a 10, va a devolver el
número menor.
Si la suma de los 3 números es un valor entre 10 y 15
(incluidos) va a devolver el número de valor intermedio.

"""
def devolver_distintos(n1, n2, n3):
    valores = [n1, n2, n3]

    if n1 + n2 + n3 > 15:
        return max(valores)
    elif  n1 + n2 + n3 < 10:
        return min(valores)
    else: 
        valores.sort()
        return valores[1]

# print(devolver_distintos(4,0,5))

"""
2 - Escribe una función (puedes ponerle cualquier nombre que
quieras) que reciba cualquier palabra como parámetro, y que
devuelva todas sus letras únicas (sin repetir) pero en orden
alfabético.
Por ejemplo si al invocar esta función pasamos la palabra
"entretenido"
, debería devolver ['d','e','i','n','o','r','t']
"""

def unicos(palabra):
    x = [i for i in palabra] # en un nueva list imprimo el elemento por cada elemento en palabra
    y = set(x) # elimino repetidos
    z = list(y) # parseo a lista para usar el metodo sort()
    z.sort() # muto la lista para que este ordenada

    return z # devuelvo la lista ordenada sin rep

# print(unicos("holaamigos432perro"))

"""
3 - Escribe una función que requiera una cantidad indefinida de
argumentos. Lo que hará esta función es devolver True si en
algún momento se ha ingresado al numero cero repetido dos
veces consecutivas.
Por ejemplo:
(5,6,1,0,0,9,3,5) >>> True
(6,0,5,1,0,3,0,1) >>> False
"""

def busqueda(*args):
    contador = 0
    for num in args:

        if contador + 1 == len(args):
            return False
        elif args[contador] == 0 and args[contador+1] == 0:
            return True
        else:
            contador += 1

    return False
    
# print(busqueda(1,2,0,3,4,0,7))

""""
4 -Escribe una función llamada contar_primos() que requiera un
solo argumento numérico.
Esta función va a mostrar en pantalla todos los números
primos existentes en el rango que va desde cero hasta ese
número incluido, y va a devolver la cantidad de números
primos que encontró.
Aclaración, por convención el 0 y el 1 no se consideran primos.
"""

def contar_primos(num):
    primos = [2]
    iteracion = 3

    if num < 2:
        return 0
    
    while iteracion <= num:
        for n in range(3,iteracion,2):
            if iteracion % n == 0:
                iteracion += 2
                break
        else:
            primos.append(iteracion)
            iteracion += 2
    
    print(primos)
    return len(primos)

print(contar_primos(50))
    
