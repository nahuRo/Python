# en un set los elementos no se repiten
# son inmutables
# no admiten listas ni diccionarios pero si tuplas
mi_set = set([1,2,3,4,5,1,1,1,1,2,2,2])
mi_set2 = {1,2,3,8}

print(mi_set2)
print(len(mi_set))

print(2 in mi_set)

mi_set3 = mi_set.union(mi_set2)
print(mi_set3)

# mas metodos => .add() .remore() .discard() .pop() ...



