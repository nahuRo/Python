def decorar_saludo(funcion):

    def otra_funcion(palabra):
        print("hola")
        funcion(palabra)
        print("adios")
    
    return otra_funcion

def mayuscula(texto):
    print(texto.upper())

# @decorar_saludo
def minuscula(texto):
    print(texto.lower())

mayuscula_decorada = decorar_saludo(mayuscula)
mayuscula_decorada('agustin')
mayuscula('agustin')

