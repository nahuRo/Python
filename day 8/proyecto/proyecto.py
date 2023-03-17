import gen_turnos

def preguntar():
    print("\nBienvenido a Farmacias Learning\n")

    while True:
        print(" [P] - Perfumeria\n [F] - Farmacia\n [C] - Cosmeticos \n")

        try:
            mi_rubro = input("Elija su rubro: ").upper()
            ["P","F","C"].index(mi_rubro)
        except:
            print("\nElija una opcion valida\n")
        else: 
            break # salgo del loop

    gen_turnos.decorador(mi_rubro)

def inicio():
    while True:
        preguntar()
        try:
            otro_turno = input("Quieres sacar otro turno? [S] [N]: ").upper()
            ["S", "N"].index(otro_turno)
        except:
            print("Elija una opcion valida")
        else: 
            if otro_turno == "N":
                print("\nGracias por su visita")
                break # salgo del loop

inicio()