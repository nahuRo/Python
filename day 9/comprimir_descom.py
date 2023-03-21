import zipfile
import shutil

# creo un zip con w para luego meterle cosas
mi_zipfile = zipfile.ZipFile("archivo_comprimido.zip","w")

# guardo el archivo por su nombre
mi_zipfile.write("day 1")

# otra manera con shutil

# carpeta_a_comprimir = "ruta" # aqui va la ruta ej 'C:\\user\\agutin'...
# nombre_del_zip = "archivo_comprimido"

# shutil.make_archive(nombre_del_zip, "zip", carpeta_a_comprimir)

# para descomprimir
# shutil.unpack_archive("archivo_comprimido.zip","carpeta descomprimida","zip")