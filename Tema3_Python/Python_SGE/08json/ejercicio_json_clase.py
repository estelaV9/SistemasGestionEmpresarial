import os
import json

# CREAR UNA FUNCION QUE GENERE UN FICHERO JSON CON LOS MISMOS DATOS DEL EJERCICIO ANTERIOR
json_file = "prueba.json"
def generar_fichero ():
    data = {
     "nombre": "Eduardo",
     "edad": 23,
     "fecha_nacimiento": "12-02-2004",
     "modulos": ["Java", "Kotlin", "Python"]
    }

    with open(json_file, "w") as json_data:
        json_file.dump(data, json_data) # dump CONVIERTE EL DICCIONARIO EN FORMATO JSON Y LO ESCRIBE 
        
    with open(json_file, "r") as json_data:
        print(json_data.read())


# CREAR UNA CLASE PERSON QUE TENGA UN CONSTRUCTOR QUE RECIBA COMO ATRIBUTOS LOS DATOS DEL FICHERO
class Person:
    def __init__(self, nombre, edad, fecha_nacimiento, modulos):
        # ALMACENAR LOS ATRIBUTOS EN VARIABLES DE INSTANCIA DENTRO DE LA CLASE
        self.nombre = nombre
        self.edad = edad
        self.fecha_nacimiento = fecha_nacimiento
        self.modulos = modulos


with open(json_file, "r") as json_data:     
    person = Person(json_file.__getattribute__)
    
# ELIMINAR EL FICHERO JSON
print("Borrando el fichero json")
os.remove(json_file)