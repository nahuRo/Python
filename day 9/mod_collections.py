from collections import Counter, defaultdict, namedtuple

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 2, 3, 1, 4, 3, 4]

print(Counter(numeros))

mi_dic  = {"uno":"verde","dos":"rojo","tres":"azul"}

# defaultdict, es para darle un valor por defecto al diccionario en caso de acceder a una propiedad que no exista

Persona = namedtuple("Persona",["nombre","altura","peso"])

ariel = Persona("Ariel", 1.63, 78)

print(ariel.altura)