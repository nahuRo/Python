# clase
class Pajaro:
    alas = True

    # constructor, entiendo que self es como el 'this' en otros lenguajes, siempre va al comienzo y de forma explicita
    def __init__(self, color, especie):
        self.color = color
        self.especie = especie
    
    # metodos de instancia
    def piar(self):
        print(f"Pio Pio, mi color es {self.color}")

    def volar(self, metros):
        print(f"el pajaro ha volado {metros}")
        self.piar()
    
    def pintar_negro(self):
        self.color = "negro"
        print(f"Ahora el pajaro es de color {self.color}")

    # metodos de clase, no puedo usar self pero si acceder a los atributos de la clase
    @classmethod 
    def poner_huevos(cls, cantidad):
        print(f"puso {cantidad} huevos")

        # puedo acceder a los atributos de la clase
        cls.alas = False
        print(Pajaro.alas)

    # metodos estatitos, no puedo usar self ni tampoco acceder a los atributos de la clase
    @staticmethod
    def mirar():
        print("El pajaro mira")

        

# instanciando 
pajaro1 = Pajaro("negro","tucan")
pajaro2 = Pajaro("azul","normal")


# ejecutando con metodo de instancia
pajaro1.alas = False

print(pajaro1.color)
print(pajaro1.especie)
pajaro1.piar()
pajaro1.volar(120)

# ejecutando con metodo de clase, no necesito instaciar una clase para usar el metodo
Pajaro.poner_huevos(3)

# ejecutando con metodo de clase, no necesito instaciar una clase para usar el metodo
Pajaro.mirar()