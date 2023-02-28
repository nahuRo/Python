# Fragmentar
texto = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

fragmento = texto[2:10] # [::-1] para voltear el stringo

print(fragmento)

## METODOS DE LOS STRINGS - inmutables
mi_texto = "Esta es una prueba"
mi_texto2 = ["Hola", "Como", "Estas"]

print("-----")
print(mi_texto[0])
print(mi_texto.index("p")) # indice, cuando no lo encuentra devuelve un error
print(mi_texto.find("p")) #find, cuando no lo encuentra devuelve un -1
print(mi_texto.upper()) # upper
print(mi_texto.lower()) # lower
print(mi_texto.split()) # separa en un []
print("".join(mi_texto2)) # uno [] en un string
print(mi_texto.replace("prueba","chau")) # reemplaza el 1er parametro por el 2do

print("es" in mi_texto) # existencia
print("es" not in mi_texto) #no existencia
print(len(mi_texto)) # largo del string