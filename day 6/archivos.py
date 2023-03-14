# toma como raiz la carpeta general del proyecto
# mi_archivo = open('./day 6/prueba.txt',"r") # solo lectura
# mi_archivo = open('./day 6/prueba.txt',"w") # solo escritura, si existe se formatea el archivo para escribir desde cero
mi_archivo = open('./day 6/prueba.txt',"a") # escritura o lectura a partir de lo que habia en el archivo

# si no existe el archivo con "w"/"a" lo creo

# mi archivo tiene metodos
# print(mi_archivo.read())
mi_archivo.write("lo modifico")

mi_archivo.close()