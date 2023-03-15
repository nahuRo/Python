# polimorfismo -> muchas formas
# Dos objetos de clases distintas (vaca, oveja) pueden ejecutar metodos con el mismo nombre (aunque hagan cosas distintas cada uno de sus metodos) y funciona todo bien

class Vaca:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice muu")

class Oveja():
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print(f"{self.nombre} dice bee")

vaca_1 = Vaca("tomasa")
oveja_1 = Oveja("clara")

def animal_habla(animal):
    animal.hablar()

animal_habla(vaca_1)
animal_habla(oveja_1)

# animales = [vaca_1, oveja_1]

# for animal in animales:
#     animal.hablar()

 