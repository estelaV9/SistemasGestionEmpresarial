""" ***************** PRACTICA 12: CUBE_X TIENDA DE CUBOS *******************************
REALIZADO POR: Estela de Vega Martin 2DAM 
CURSO: 24/25
ASIGNATURA: Sistemas de Gestión Empresarial """
from dao import user_dao
from model.product import product
from model.user import user

try:
    option = -1
    list_cube = [] # LISTA DONDE SE GUARDARAN LOS CUBOS

    # añadir unos objetos de productos por defecto
    cube1 = product("Rubik 3x3 Gan 356 XS", 39.99, 2, "3x3x3")
    cube2 = product("MoYu WeiLong WR M 2020", 29.99, 5, "3x3")
    cube3 = product("QiYi MS 2x2", 8.99, 10, "2x2")
    cube4 = product("YJ YuLong Pyraminx V2 M", 12.99, 3, "Pyraminx")
    cube5 = product("Yuxin Little Magic 4x4", 13.99, 7, "4x4")
    cube6 = product("ShengShou Megaminx", 14.99, 4, "Megaminx")
    cube7 = product("X-Man Bell Magnetic Skewb", 17.99, 6, "Skewb")
    list_cube = [cube1, cube2, cube3, cube4, cube5, cube6, cube7] # CREAR UNA LISTA CON ESOS PRODUCTOS


    print("¿Cómo quieres entrar a nuestra tienda?\n1-Iniciando sesión\n2-Creando una cuenta")
    metodo_login = int(input())
    if metodo_login == 1:
        print("******** INICIAR SESION ********")
        email = input("Email: ")
        password = input("Contraseña: ")
        user_log = user(email, password, name_user=None)
        """ nota (para mi): para indicar que la funcion devuelva false en vez de poner '!' en Python es con 'not' """
        if not user_dao.log_in(user_log):
            print("No se ha encontrado usuario. Por favor, pruebe con otro usuario o crease una cuenta.")
        else:
            print("Inicio de sesión exitosa")

    else:
        print("******** CREAR UNA CUENTA ********")
        name_user = input("Nombre del usuario: ")
        email = input("Email: ")
        password = input("Contraseña: ")
        new_user = user(email, password, name_user)
        if user_dao.create_user(new_user):
            print("Creación de cuenta exitosa")
        else:
            print("Ya tienes una cuenta, inicia sesión para entrar a nuestra tienda")

    print("¡Bienvenido a CubeX! ¿Qué desea hacer en nuestra tienda?")
    while option != 0:
        print("**** MENU ****",
          "\n1 - Ver todos los productos disponibles.",
          "\n2 - Ver tus productos.",
          "\n3 - Comprar productos",
          "\n4 - Crear productos",
          "\n5 - Modificar productos",
          "\n6 - Eliminar productos",
          "\n0 - Salir de la tienda.")
        option = int(input("Introduzca la opción: "))

        match option:
            case 1:
                product.devolver_productos(list_cube)
            case 2:
                print("********** TUS PRODUCTOS **********")
            case 3:
                print("********** COMPRAR PRODUCTOS **********")
            case 4:
                print("********** CREAR PRODUCTOS **********")
            case 5:
                print("********** MODIFICAR PRODUCTOS **********")
            case 6:
                print("********** ELIMINAR PRODUCTOS **********")
            case 0:
                print("Gracias por visitar nuetra tienda.")
            case _:
                print("Opción no válida.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
print("¡Vuelva pronto!")