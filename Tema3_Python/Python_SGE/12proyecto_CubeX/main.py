""" ***************** PRACTICA 12: CUBE_X TIENDA DE CUBOS *******************************
REALIZADO POR: Estela de Vega Martin 2DAM 
CURSO: 24/25
ASIGNATURA: Sistemas de Gestión Empresarial """

print("¡Bienvenido a CubeX! ¿Qué desea hacer en nuestra tienda?")
try:
    print("**** MENU ****",
          "\n1 - Ver todos los productos disponibles.",
          "\n2 - Ver tus productos.",
          "\n3 - Crear productos",
          "\n4 - Modificar productos",
          "\n5 - Eliminar productos",
          "\n6 - Salir de la tienda.")
    opcion = int(input("Tu ooción: "))
    while (opcion != 6):
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
            case _: 
                print("Opción no válida. Introduzca un número del 1 al 6.")
        
    print(opcion)
except Exception as e:
    print(f"Ocurrió un error: {e}")
print("¡Vuelva pronto!")