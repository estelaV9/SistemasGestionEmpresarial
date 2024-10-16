""" ***************** PRACTICA 12: CUBE_X TIENDA DE CUBOS *******************************
REALIZADO POR: Estela de Vega Martin 2DAM 
CURSO: 24/25
ASIGNATURA: Sistemas de Gestión Empresarial """
from dao import user_dao, product_dao
from model.product import product
from model.user import user

try:
    option = -1
    # INICIAR SESION
    while True:
        print("¿Cómo quieres entrar a nuestra tienda?\n1-Iniciando sesión\n2-Creando una cuenta")
        metodo_login = int(input())
        # CONTROLAR QUE PONGA LA OPCION 1 O 2
        while metodo_login > 2 or metodo_login < 1:
            metodo_login = int(input("Introduzca una opcion entre 1 y 2\n"))

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
                break  # SALE DEL BUCLE SI SE HA INICIADO SESION CORRECTAMENTE Y ENTRA EN LA TIENDA

        elif metodo_login == 2:
            print("******** CREAR UNA CUENTA ********")
            name_user = input("Nombre del usuario: ")
            email = input("Email: ")
            password = input("Contraseña: ")
            new_user = user(email, password, name_user)
            if user_dao.create_user(new_user):
                print("Creación de cuenta exitosa")
                break  # SALE DEL BUCLE SI SE HA CREADO CUENTA CORRECTAMENTE Y ENTRA EN LA TIENDA
            else:
                print("Ya tienes una cuenta, inicia sesión para entrar a nuestra tienda")

    # MENU PRINCIPAL DESPUES DEL INICIO DE SESION
    print("\n\n¡Bienvenido a CubeX! ¿Qué desea hacer en nuestra tienda?")
    while option != 0:
        print("\n**** MENU ****",
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
                print("********** TODOS LOS PRODUCTOS **********")
                product_dao.list_product()
            case 2:
                print("********** TUS PRODUCTOS **********")
                product_dao.list_product_user(user_dao.search_name(email))
            case 3:
                print("********** COMPRAR PRODUCTOS **********")
            case 4:
                print("********** CREAR PRODUCTOS **********")
                product_dao.create_product(user_dao.search_name(email))
            case 5:
                print("********** MODIFICAR PRODUCTOS **********")
            case 6:
                print("********** ELIMINAR PRODUCTOS **********")
                product_name = input("Introducta el producto que quieras eliminar: ")
                product_dao.delete_product(product_name)
            case 0:
                print("Gracias por visitar nuetra tienda.")
            case _:
                print("Opción no válida.")
except Exception as e:
    print(f"Ocurrió un error: {e}")
print("¡Vuelva pronto!")
