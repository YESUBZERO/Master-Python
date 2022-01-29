from io import open
import pathlib

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo = open(ruta, "a")

# Escribir
archivo.write("****** Soy un texto usando python ********\n")

# Cerrar archivo
archivo.close()