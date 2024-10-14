""" ***************** PRACTICA 12: CUBE_X TIENDA DE CUBOS *******************************
REALIZADO POR: Estela de Vega Martin 2DAM 
CURSO: 24/25
ASIGNATURA: Sistemas de Gestión Empresarial """

try:
    opcion = -1
    print("¡Bienvenido a CubeX! ¿Qué desea hacer en nuestra tienda?")
    while (opcion != 0):
        print("**** MENU ****",
          "\n1 - Ver todos los productos disponibles.",
          "\n2 - Ver tus productos.",
          "\n3 - Crear productos",
          "\n4 - Modificar productos",
          "\n5 - Eliminar productos",
          "\n0 - Salir de la tienda.")
        opcion = int(input("Introduzca la opción: "))

        match opcion:
            case 1:
                print("********** PRODUCTOS EN TIENDA **********")
            case 2:
                print("********** TUS PRODUCTOS **********")
            case 3:
                print("********** CREAR PRODUCTOS **********")
            case 4:
                print("********** MODIFICAR PRODUCTOS **********")
            case 5:
                print("********** ELIMINAR PRODUCTOS **********")
            case 0:
                print("Gracias por visitar nuetra tienda.")
            case _:
                print("Opción no válida.")
        
    print(opcion)
except Exception as e:
    print(f"Ocurrió un error: {e}")
print("¡Vuelva pronto!")