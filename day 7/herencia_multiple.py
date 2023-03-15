class Padre:
    def hablar(self):
        print("Hola")

class Madre:
    def reir(self):
        print("ja ja")

    def hablar(self):
        print("Que tal")

# si en las clases de las que heredo tengo metodos/atributos con el mismo nombre el que obtengo es en el primer clase de la que heredo
class Hijo(Madre, Padre):
    pass

class Nieto(Hijo):
    pass

mi_nieto = Nieto()

mi_nieto.hablar() # imprime "Que tal"
mi_nieto.reir()