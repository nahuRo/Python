import random
from os import system

class Persona:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido

class Cliente(Persona):
    def __init__(self, nombre, apellido):
        super().__init__(nombre, apellido)
        self.numero_cuenta = random.randint(1, 100000)
        self.balance = 0
    
    def imprimir_cliente(self):
        print(f"""
        *** Datos del Cliente ***

        Nombre: {self.nombre}
        Apellido: {self.apellido}
        Nro Cuenta: {self.numero_cuenta}
        Balance: {self.balance}
        """)

    def depositar(self, cantidad_dep):
        self.balance += cantidad_dep
        print("Deposito realizado con éxito")
        
    def retirar(self, cantidad_ret):
        if self.balance >= cantidad_ret:
            self.balance -= cantidad_ret
            print("Retiro realizado con éxito")
        else:
            print("No se puede retirar esa cantidad")

def crear_cliente():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apelllido: ")

    return Cliente(nombre, apellido)

def main():
    cliente = crear_cliente()
    finalizar_programa = False

    while not finalizar_programa:
        
        print(f"""
                ---- Menu ----
            [1] - Informe de cuenta
            [2] - Depositar
            [3] - Retirar
            [4] - Salir

        """)

        opcion_u = input(": ")

        match opcion_u:
            case '1':
                cliente.imprimir_cliente()
            case '2':
                deposito = int(input("Ingrese la cantidad a depositar: "))
                cliente.depositar(deposito)
            case '3':
                retiro = int(input("Ingrese la cantidad que desea retirar: "))
                cliente.retirar(retiro)
            case '4':
                print("Hasta luego")
                finalizar_programa = True

main()