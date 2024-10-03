""" **************************** FUNCIONES LAMBDA ******************************** 
Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas 
y anónimas (no es necesario proporcionar un nombre para las funciones lambda).
Resultan útiles cuando se desea definir una función pequeña de forma concisa. """


# SINTAXIS DE UNA FUNCION LAMBDA
# lambda argumentos: expresión

# CODIGO DE EJEMPLO
    # FUNCION LAMBDA PARA CALCULAR EL CUADRADO DE UN NUMERO
square = lambda x: x ** 2
print(square(3)) # RESULTADO: 9

    # FUNCION TRADICIONAL PARA CALCULAR EL CUADRADO DE UN NUMERO
def square1(num):
  return num ** 2
print(square(5)) # Resultado: 25