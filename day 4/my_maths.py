# from random import randint
import random

# randint(1,10)
num_random = random.randint(1,10)
print(num_random)

# uniform
num_random2 = round(random.uniform(0,10),1)
print(num_random2)

# random --> numero float entre 0 y 1
num_random3 = random.random()
print(num_random3)

# choice --> aleatorio en lista
colores = ["red", "green", "blue", "yellow"]
color_random = random.choice(colores)
print(color_random)

# shuffle --> me mezcla la lista, me cambia la lista, la muta
numeros = list(range(1,10))
random.shuffle(numeros)
print(numeros)
