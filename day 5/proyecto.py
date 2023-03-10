import random

palabras = ["casa","auto","maestro","raton","sombrero","maestro","espejo","mueble","lengua","ropa"]

def x_word(listado):
    return random.choice(listado)

def pedir_letra():
    es_valida = False

    while not es_valida:
        player_str = input("Ingresa una letra: ").lower()

        if player_str in "abcdefghijklmnñopqrstuvwxyz" and len(player_str) == 1:
            es_valida = True
        else:
            print("letra invalida")

    return player_str

def game():
    vidas = 7

    oculto = x_word(palabras)
    palabra_censurada = ["-" for letter in oculto]
    nivel_completado = 0
    letra_usadas = set()
    letras_correctas = []

    while vidas > 0:

        print(f"""
            Palabra --> {" ".join(palabra_censurada)}
            vidas --> {vidas}
            progreso --> {nivel_completado} / {len(oculto)}
            letras elegidas --> {" ".join(list(letra_usadas))}
        """)
        
        if nivel_completado == len(oculto):
            return "*** GANASTE! ***"

        letra_elegida = pedir_letra()
        letra_usadas.add(letra_elegida)

        ind = 0
        if letra_elegida in oculto:
            for let in oculto:
                if let == letra_elegida and let not in letras_correctas:
                    palabra_censurada[ind] = letra_elegida
                    letras_correctas.append(let)
                    nivel_completado += 1
                ind += 1
        else:
            vidas -= 1


    else:
       return "GAME OVER!"

print(game())