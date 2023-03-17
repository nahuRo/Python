def n_perfumeria():
    for n in range(1,10000):
        yield f"P - {n}"

def n_farmacia():
    for n in range(1,10000):
        yield f"F - {n}"

def n_cosmetica():
    for n in range(1,10000):
        yield f"C - {n}"

p = n_perfumeria()
f = n_farmacia()
c = n_cosmetica()

def decorador(rubro):

    print("\n" + "*" * 23)
    print("Su turno es:")

    if rubro == "P":
        print(next(p))
    elif rubro == "F":
        print(next(f))
    else:
        print(next(c))

    print("Aguarde y sera atendido")
    print("*" * 23 + "\n")