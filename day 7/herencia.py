class Animal:
    # contructor
    def __init__(self, edad, color):
        self.edad = edad
        self.color = color
        
    def nacer(self):
        print("Este animal ha nacido")

    def hablar(self):
        print("Este animal emite un sonido")


# para heredar de otra clase, esta se coloca en los parametros de la que hereda
class Pajaro(Animal):
    # constructor forma 1
    def __init__(self, edad, color, altura_vuelo):
        super().__init__(edad, color)
        self.altura = altura_vuelo

    # contructor forma 2
    # def __init__(self, edad, color, altura_vuelo):
    #     self.edad = edad
    #     self.color = color
    #     self.altura = altura_vuelo

    # si tengo una fun/atri con el mismo nombre que la clase 'padre', este se sobreescribe
    def hablar(self):
        print("pio")

    def volar(self, metros):
        print(f"El pajaro vuela {metros}")


piolin = Pajaro(2, "verde", 60)

piolin.nacer()

