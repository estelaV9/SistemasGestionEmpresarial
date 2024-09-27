""" FUNCIONES: es un conjunto de instrucciones agrupadas bajo un nombre concreto
que pueden reutilizarse invocando a la funcion tantas veces como sea necesario

SINTAXIS
def nombre_funcion(parametros):
    BLOQUE / CONJUNTOS DE INSTRUCCIONES """ 
    
# FUNCIONES SIMPLES
def greet():
    print("Holaa!!, bienvenidos al curso 24/25")
    
greet() # INVOCAMOS LA FUNCION

# FUNCION RETORNO
def return_greet():
    return "Holaa!!, bienvenidos al curso 24/25"
print(return_greet())

# FUNCION CON PARAMETROS
def arg_greet(name):
    print(f"Hola, {name}")

arg_greet("Eugenio")

# FUNCIONES CON UN NUMERO VARIABLES DE ARGUMENTOS
""" def variable_arg_greet(*greet): # PODEMOS PASAR MAS DE UN NOMBRE, SEPARADO POR COMAS
    for name in names:
        print(f"Buenos dias, {name}")
variable_arg_greet("Uno", "Dos", "Tres")"""

# FUNCIONES CON NUMERO VARIABLES DE ARGUMENTOS CON PALABRA CLASE
# ** SIGNIFICA QUE CADA ARGUMENTO ESTA FORMADO POR UNA CLAVE Y UN VALOR
