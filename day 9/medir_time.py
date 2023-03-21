import time 
import timeit

def prueba_for(n):
    lista = []
    for n in range(1, n + 1):
        lista.append(n)
    return lista

def prueba_while(n):
    lista = []
    contador = 1
    while contador <= n:
        lista.append(contador)
        contador += 1
    return lista

inicio = time.time() 
prueba_for(100000)
final = time.time()
print(final - inicio)

inicio = time.time() 
prueba_while(100000)
final = time.time()
print(final - inicio)

