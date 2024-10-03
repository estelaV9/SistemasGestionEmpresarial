""" **************************** FUNCIONES LAMBDA ******************************** 
Las expresiones lambda en Python son una forma corta de declarar funciones pequeñas 
y anónimas (no es necesario proporcionar un nombre para las funciones lambda).
Resultan útiles cuando se desea definir una función pequeña de forma concisa. 

SINTAXIS: lambda argumentos: expresión """

# CODIGO DE EJEMPLO
    # FUNCION LAMBDA CON UN PARAMETRO
cuadrado = lambda x: x * x
print(cuadrado(5))


    # FUNCION LAMBDA PARA CALCULAR EL CUADRADO DE UN NUMERO
square = lambda x: x ** 2
print(square(3)) # RESULTADO: 9

    # FUNCION TRADICIONAL PARA CALCULAR EL CUADRADO DE UN NUMERO
def square1(num):
  return num ** 2
print(square(5)) # Resultado: 25


# FILTRAR UNA LISTA: LAMBDA DENTRO DE LA FUNCION filter()
""" FILTER(): filtra elementos de un iterable (lista, tupla...)que cumpla una condicion
SINTAXIS: filter(functiion, iterable). 
Devuleve un objeto de tipo filter; hay que convertirlo a tipo iterable (lista...)

"""

numeros = [1, 2, 3]
pares = list(filter(lambda x: x % 2 == 0, numeros)) # FILTER DEVUELVE UN OBJETO D ETIPO FILTER
print(pares)

# MAPEAR UNA LISTA: lambda dentro de la funcion map()
""" map() se usa para aplicar UNA FUNCION A CADA UNO DE LOS ELEMENTOS DE un ITERABLE(lista, tupla...)
SINTAXIS: MAP(FUNCTION, ITERABLE, ....)
devuelve un objeto de tipo map; hay que convertirlo a tipo iterable (lista...)"""
numeros = [1, 2, 3, 4, 5, 6]
cuadrados = list(map(lambda x: x ** 2, numeros))
print(cuadrados)
