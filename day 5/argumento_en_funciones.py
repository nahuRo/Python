# *args
# lo mas comun es nombrarlo *args, pero prodira haber sido *cosas,*muchos, lo que importa en el *
def suma(*args):
    total = 0
    for arg in args:
        total += arg
    return total

print(suma(1,2,2,5,87))

# **kwargs 
# se usa para pasar parametros comupuestos o sea clave, valor
def suma2(**kwargs):
    for clave,valor in kwargs.items(): 
        print(f"clave {clave} y valor {valor}")

suma2(x=3,y=2,z=1)

