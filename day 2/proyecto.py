# Proyecto: calculadora de comisiones 
nombre = input("Cual es tu nombre")
ventas = float(input("valor de ventas"))

comision = round(ventas * 13 / 100, 2)

print(f"{nombre}, tus ganancias por comisiones son: ${comision}")