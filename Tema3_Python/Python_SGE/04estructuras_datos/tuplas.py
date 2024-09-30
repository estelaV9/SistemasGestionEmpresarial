# ****************** TUPLAS *********************
""" INVESTIGAR LA ESTRUCTURA DE DATOS TUPLAS 
Las tuplas son un tipo o estructura de datos que permite almacenar datos de una manera 
muy parecida a la lista, pero son INMUTABLES, es decir, que no pueden ser modificadas
una vez declaradas y se inicializan con (). """


# INSERCION
tupla = (1, 2, 3)
print(tupla) # (1, 2, 3)

tupla = 1, 2, 3 # se puede declarar sin ()
print(tupla)


# ORDENACION
""" se puede ordenar con al funcion sorted (devuelve una lista) """
 # SI NO QUEREMOS QUE SE CONVIERTA EN UNA LISTA PONEMOS tuple() PARA QUE LO VUELVA A CONVERTIR EN TUPLA
tupla = tuple(sorted(tupla))
print(tupla)
print(type(tupla)) # SE CONVIERTE EN UNA LISTA SI NO TIENE ELMETODO tuple()


# NO SE PUEDE MODIFICAR
