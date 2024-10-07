""" EJERCICIO 8: FICHEROS JSON 
JSON (JavaScript Object Notation) es un formato de intercambio de datos ligero que se utiliza
comúnmente para representar datos estructurados. Se basa en la notación de objetos de JavaScript.

Elementos clave de JSON:
 - Objetos: Representados por llaves {}, contienen pares de clave-valor. {"nombre": "Juan", "edad": 30}
 - Array: Representados por corchetes [], son listas ordenadas de valores. ["rojo", "verde", "azul"]
 - Tipos de datos: Puede contener cadenas (string), números (number), booleanos (true/false), nulos (null), objetos y arrays.
 - Claves: Siempre deben ser cadenas y deben estar entre comillas dobles.

Características de JSON:
 - Formato de texto: es solo texto, lo que hace que sea facil de feer y escribir
 - De fácil lectura.
 - Soporta estructuras anidadas (objetos dentro de objetos, array dentro de objetos, etc.).
 - Suele ser aplicado más comúnmente en un entorno web, donde recibir datos entre cliente y servidor.

Usos principales de JSON:
 - Intercambio de datos entre aplicaciones y servicios web (API).
 - Almacenamiento de configuración y datos en aplicaciones.
 - Intercambio de datos entre lenguajes de programación diferentes. """
 
# EJERCICIO QUE GUARDE LOS DATOS (nombre, edad, fechaNacimiento, modulos [lista de cadenas])
import json # IMPORTARLO
import os    
data = {
     "nombre": "Eduardo",
     "edad": 23,
     "fecha_nacimiento": "12-02-2004",
     "modulos": ["Java", "Kotlin", "Python"]
}

json_file = "prueba.json"
with open(json_file, "w") as json_data:
    json.dump(data, json_data) # dump CONVIERTE EL DICCIONARIO EN FORMATO JSON Y LO ESCRIBE 
    
with open(json_file, "r") as json_data:
    print(json_data.read())

print("Borrando el fichero json")
os.remove(json_file)