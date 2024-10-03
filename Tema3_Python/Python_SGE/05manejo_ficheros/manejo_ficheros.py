""" **************************** MANEJO DE FICHEROS ******************************** 
Para crear un fichero de tipo texto en Python, utilizamos la función open() junto con el 
modo 'w' (escritura). Si el fichero no existe, se creará; si ya existe, se sobrescribirá. 
En python se usa impor os (operacions que interactuan con el SSOO"""
import os
file_name = "fichero.txt"

""" En python se usa with y as para abrir (o crear si no existe), en la raiz del proyecto
el archivo en modo escritura. Con bloque with...as el archivo se cierra automaticamente
despues de la ejecucion del bloque"""

with open(file_name, "w") as file:
    file.write("Estela de Vega\n")
    file.write("45\n")
    file.write("Python\n")

with open(file_name, "r") as file:
    print(file.read())

# EJEMPLO SIN USAR WITH
def crear_fichero_sin_with(nombre_fichero, contenido):
    try:
        fichero = open(nombre_fichero, 'w')
        fichero.write(contenido)
    except Exception as e:
        print(f"Ocurrió un error al crear el fichero: {e}")
    finally:
        fichero.close()  # SE CIERRA EL ARCHIVO


nombre_fichero = "mi_fichero.txt"
contenido = "Hola, este es el contenido del fichero.\nGracias por usar este script."

crear_fichero_sin_with(nombre_fichero, contenido)


# EJEMPLO USANDO WITH
# EL WITH LO QUE HACE ES QUE EL ARCHIVO SE CIERRA AUTOMATICAMENTE AL SALIR DEL BLOQUE,
# LO QUE PREVIENE POSIBLES ERRORES
def crear_fichero_con_with(nombre_fichero, contenido):
    try:
        # ABRIR EL FICHERO EN MODO ESCRITURA (w)
        with open(nombre_fichero, 'w') as fichero:
            # ESCRIBIR EL CONTENIDO EN EL FICHERO
            fichero.write(contenido)
        print(f"Fichero '{nombre_fichero}' creado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al crear el fichero: {e}")

# NOMBRE DEL FICHERO A CREAR
nombre_fichero = "mi_fichero.txt"
# CONTENIDO QEU SE VA A ESCRIBIR EN EL FICHERO
contenido = "Hola, este es el contenido del fichero.\nAdios."

# LLA,AR A LA FUNCION PARA CREAR EL FICHERO
crear_fichero_con_with(nombre_fichero, contenido)


# EJEMPLO AÑADIENDO VARIAS LINEAS AL FICHERO (nombre, edad, lenguaje de programacion usado)
def crear_fichero (nombre, edad, lenguaje_programacion):
    try:
        # ABRIR EL FICHERO EN MODO ESCRITURA (w)
        with open(nombre_fichero, 'w') as fichero:
            # ESCRIBIR EL CONTENIDO EN EL FICHERO
            fichero.write(nombre)
            fichero.write(edad)
            fichero.write(lenguaje_programacion)
        print(f"Fichero '{nombre_fichero}' creado con éxito.")
    except Exception as e:
        print(f"Ocurrió un error al crear el fichero: {e}")
    

