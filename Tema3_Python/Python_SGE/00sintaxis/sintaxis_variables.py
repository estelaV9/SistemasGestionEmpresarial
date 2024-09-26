""" Nombre del Ciclo Formativo: DAM.
Nombre del Módulo: Sistemas de gestión empresarial.
Curso: 24/25
Nombre Completo: Estela de Vega Martín """

# SINTAXIS Y VARIABLES PYTHON
my_string = "My String"; # CREAR UNA CADENA DE TEXTO
my_number = 12; # CREAR UN NUMERO ENTERO
my_decimal = 23.33; # CREAR UN NUMERO DECIMAL
my_boolean = True; # CREAR UN BOOLEANO (Bool)

# IMPRIMIR POR TERMINAL EL CONTENIDO DE LAS VARIABLES
    # IMPRIMIR DE FORMA CONCATENADA (hay que poner str a las variables)
print("******* VARIABLES PYTHON *******" +
    "\nCadena de texto: " + my_string + 
    "\nNumero Entero: " + str(my_number) +
    "\nNumero Decimal: " + str(my_decimal) +
    "\nBooleano: " + str(my_boolean) + "\n")

    # IMPRIMIR DE FORMA CONCATENADA PERO CON , (no hace falta poner str a la variables)
print("******* VARIABLES PYTHON *******" ,
    "\nCadena de texto: " , my_string ,
    "\nNumero Entero: " , my_number ,
    "\nNumero Decimal: " , my_decimal ,
    "\nBooleano: " , my_boolean , "\n")

    # IMPRIMIR EN UNA SOLA LINEA 
print("******* CONTENIDO DE VARIABLES *******")
print(my_string)
print(my_boolean)
print(my_number)
print(my_decimal)

# IMPRIMIR POR TERMINAL EL TIPO DE CADA VARIABLE
print("\n******* TIPO DE VARIABLE ********")
print(type(my_string))