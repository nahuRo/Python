# ocupan menos que los listas y se escriben mu parecidos
# al igual que los strings son inmutables
mi_tupla = (1,2,3,(3.5,4),5,1,1)
mi_tupla2 = 6,7,8,9,10


a,b,c,d,e = mi_tupla2 # creo variables y le asigno cada valor en orden de la tupla, valido para listas

print(mi_tupla[3][0])
print(mi_tupla2)

# mi_nuevo = list(mi_tupla)
# mi_nuevo2 = tuple(mi_nuevo)

print(mi_tupla.count(1)) # cantidad de veces que aparece
print(mi_tupla.index(3))