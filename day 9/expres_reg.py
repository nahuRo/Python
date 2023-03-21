import re

texto = "Si necesitas ayuda llama a este numero 657-232-1332"

patron = r'\d{3}-\d{3}-\d{4}'

busqueda = re.search(patron, texto)
print(busqueda.group())