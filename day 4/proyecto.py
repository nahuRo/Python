import random
print(" ============================= ")
print("           THE GAME            ")
print(" ============================= ")

player = input("Ingrese el nombre del jugador: ")
print(f"Hola {player}, he pensado un número entre el 1 y 100, tienes 8 intentos para adivinarlo")

intentos = 0
numero = 0
num_random = random.randint(1,100)

while intentos < 8:
    numero = int(input("Ingrese un número: "))
    intentos += 1

    if numero not in range(1,101):
        print("El número ingresado no esta en el rango mencionado, 1 al 100")
    elif numero < num_random:
        print("Incorrecto, elegiste un número menor al número secreto")
    elif numero > num_random:
        print("Incorrecto, elegiste un número mayor al número secreto")
    elif numero == num_random:
        print(f"Ganaste Felicitaciones ! Has adivinado en {intentos} intentos")
        break
   
if numero != num_random:
    print(f"Lo siento, se han agotado los intentos. El número secreto era {num_random}")


