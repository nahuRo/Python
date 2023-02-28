#analizador de textos

# el usuario debe ingresar un texto luego debe ingresar 3 letras y los que el analizador imprime debe ser:
# 1 - cantidad de veces que aparece la 1era, 2da y 3er letra ingresada por el usuario sobre el texto ingresado
# 2 - cantidad de palabras que tiene el texto ingresado
# 3 - primera y ultima letra del texto ingreso
# 4 - texto invertido
# 5 - existencia de la palabra python en el texto ingresado

text = input("Ingresa un texto")
text =  text.lower()

letra1 = input("1er letra")
letra2 = input("2da letra")
letra3 = input("3era letra")

letra1 = letra1.lower()
letra2 = letra2.lower()
letra3 = letra3.lower()

print(f"""
cantidad de {letra1}: {text.count(letra1)}
cantidad de {letra2}: {text.count(letra2)}
cantidad de {letra3}: {text.count(letra3)}
cantidad de palabras: {len(text.split(" "))}
primera: {text[0]} y ultima: {text[-1]}
texto invertido: {text[::-1]}
existe la python en el texto: {"python" in text}
""")

