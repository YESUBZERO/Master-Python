from io import open
import pathlib
import shutil

# Abrir archivo
#ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
#archivo = open(ruta, "a")

# Escribir
#archivo.write("****** Soy un texto usando python ********\n")

# Cerrar archivo
#archivo.close()

# Abrir archivo
ruta = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
archivo_lectura = open(ruta, "r")

# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido y guardarlo en lista
lista = archivo_lectura.readlines()
archivo_lectura.close()

for elemento in lista:
    print(elemento)

#  Copiar
ruta_original = str(pathlib.Path().absolute()) + "/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
#ruta_alternativa = "./01-holamundo/fichero_texto.txt"
shutil.copyfile(ruta_original, ruta_nueva)