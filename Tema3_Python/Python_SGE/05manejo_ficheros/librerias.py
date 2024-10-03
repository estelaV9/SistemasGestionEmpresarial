""" ************************************ LIBRERIAS ********************************************

Una libreria es un conjunto de modulos que contienen funciones, clases y variables que se pueden 
reutilizar.
Permiten aprovechar codigo ya escrito y probado por otros desarrolladores
    - Modulo: es un archivo que contiene codigo Python. Cada archivo .py que se genera es un modulo
    - Libreria: es un conjunto de modulos relaiconados entre si. La mayoria de las librerias en
    python consisten en varios modulos agrupados.
    
    
Tipos de librerias:
 - Librerias estandar de Python: son las que vienen incluidas con la instalacion de Python
 Ejmplos son math, os, random, etc
 - Librerias externas: son librerias desarrolladas por la comunidad que se pueden instalar y usar en 
 los proyectos. Ejmplo: NumPy(para operaciones numericas), Pandas....
 
 
 IMPORTANTE: El nombre del fichero no tendria que tener palabras reservadas de los metodos.
Si el archivo lo hubiesemos llamado nombre_random, daria error"""

# PROCESO
# IMPORTAR LIBRERIA
import math
result = math.sqrt(5)
print(result)

# IMPORTAR SOLO UNA FUNCION
from math import sqrt
result = sqrt(25)

# IMPORTAR LIBRERIAS EXTERNAS
""" Primero instalar pip install numpy """
import numpy as np
my_list = np.array([1, 2, 3, 4])
print(my_list)

import random
print(random.randint(10, 15)) # MOSTRAR UN NUMERO ENTERO EN EL RANGO DEL 10 Y 15

# OTRA FORMA DE IMPORTAR
from math import * # NO SE RECOMIENDA USAR


