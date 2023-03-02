# range (creo listas de numeros mas rapido)
for numero in range(5): # range(desde,hasta,paso) --> [0,1,2,3,4]
    print(numero)

lista = list(range(1,101))
print(lista)

# enumerate (para "agregarle ese indice")
lista2 = ["a", "b", "c", "d", "e"]

for ind,item in enumerate(lista2):
    print(ind,item)

# zip (uno listas)
nombres= ["ana", "juan", "marcos"]
edades = [12,34,23]
ciudad = ["Mexico","Mendoza","Lima"]

combinados = list(zip(nombres,edades,ciudad))
for nombre,edad,ciudad in combinados:
    print(f"{nombre} tiene {edad} y nacio en {ciudad}")

# min() y max()
menor = min([1,2,3,4,5,6])
mayor = max(1,2,3,4,5,6)

print(menor,mayor)