import bs4
import requests

# crea un url sin numero de pagina, luego se completara con el .format()
url_base = "https://books.toscrape.com/catalogue/page-{}.html"

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto = []

# iteracion de paginas
for pagina in range(1, 11):

    # crear sopa en cada pagina
    url_pagina = url_base.format(pagina) # le completo esa pagina al {}
    resultado = requests.get(url_pagina)
    sopa = bs4.BeautifulSoup(resultado.text, "lxml")

    # seleccionar datos de los libros
    libros = sopa.select(".product_pod")
    
    # iteracion de libros
    for libro in libros:

        # chequeo de estrellas de 4-5 estrellas
        if len(libro.select(".star-rating.Four")) != 0 or len(libro.select(".star-rating.Five")) != 0:
            # guardar titulo en variable
            titulo_libro = libro.select("a")[1]["title"]

            # agrego libro a la lista
            titulos_rating_alto.append(titulo_libro)


# ver los los libros matcheados
for titulo in titulos_rating_alto:
    print(titulo)
