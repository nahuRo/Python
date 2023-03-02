# Loops /  bucles

nombres = ["juan", "alan", "jesus", "agus"]

# for
for nombre in nombres:
    numero_nombre = nombres.index(nombre) + 1
    print(f"{numero_nombre} --> hola {nombre}")

for letra in "python":
    print(letra)

for a,b in [[1,2],[3,4],[5,6],[7,8],[9,10]]:
    print(f"{a} --> {b}")

# while (sale cuando no se cumple la condicion)

monedas = 5
while monedas > 0:
    print(f"tengo {monedas}")
    monedas -= 1 # monedas = monedas - 1
else:
    print("no tengo mas monedas")

# tanto para while como for puedo usar:
# pass, break, continue