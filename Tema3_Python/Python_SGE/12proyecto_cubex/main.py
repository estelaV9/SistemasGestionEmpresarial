""" ***************** PRACTICA 12: CUBE_X TIENDA DE CUBOS *******************************
REALIZADO POR: Estela de Vega Martin 2DAM 
CURSO: 24/25
ASIGNATURA: Sistemas de Gestión Empresarial """
from dao import user_dao, product_dao
from model.product import product
from model.user import user

email = None # SE INICIA EL MAIL

# METODO PARA INICIAR SESION
def method_login():
    print("******** INICIAR SESION ********")
    email = input("Email: ")
    password = input("Contraseña: ")
    user_log = user(email, password, name_user=None)
    """ nota (para mi): para indicar que la funcion devuelva false en vez de poner '!' en Python es con 'not' """
    if not user_dao.log_in(user_log):
        print("No se ha encontrado usuario. Por favor, pruebe con otro usuario o crease una cuenta.")
    else:
        print("Inicio de sesión exitosa")
        return email  # SALE DEL BUCLE SI SE HA INICIADO SESION CORRECTAMENTE Y ENTRA EN LA TIENDA


# METODO PARA CREARSE CUENTA
def method_signup():
    print("******** CREAR UNA CUENTA ********")
    name_user = input("Nombre del usuario: ")
    email = input("Email: ")
    password = input("Contraseña: ")
    new_user = user(email, password, name_user)
    if user_dao.create_user(new_user):
        print("Creación de cuenta exitosa")
        return email  # SALE DEL BUCLE SI SE HA CREADO CUENTA CORRECTAMENTE Y ENTRA EN LA TIENDA
    else:
        print("Ya tienes una cuenta, inicia sesión para entrar a nuestra tienda")


# METODO QEU CONTIENE EL APARTADO DE PRODUCTOS
def apartado_productos():
    # APARTADO CUBOS
    option = -1
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
                product_name = input("Introducta el producto que quieras comprar: ")
                product_dao.buy_product(product_name)
            case 4:
                print("********** CREAR PRODUCTOS **********")
                product_dao.create_product(user_dao.search_name(email))
            case 5:
                print("********** MODIFICAR PRODUCTOS **********")
                product_name = input("Introducta el producto que quieras modificar: ")
                product_dao.modify_product(product_name)
            case 6:
                print("********** ELIMINAR PRODUCTOS **********")
                product_name = input("Introducta el producto que quieras eliminar: ")
                product_dao.delete_product(product_name)
            case 0:
                print("Gracias por visitar nuetra tienda.")
            case _:
                print("Opción no válida.")


# METODO QUE CONTIENE EL APARTADO DE USUARIO
def apartado_usuario():
    option = -1
    while option != 0:
        print("\n**** MENU ****",
              "\n1 - Ver todos los usuarios de la tienda.",
              "\n2 - Ver la informacion de tu usuario.",
              "\n3 - Modificar datos del usuario.",
              "\n4 - Eliminar usuario.",
              "\n0 - Salir de la tienda.")
        option = int(input("Introduzca la opción: "))

        match option:
            case 1:
                print("********** TODOS LOS USUARIO **********")
                user_dao.list_user()
            case 2:
                print("********** TU INFORMACION **********")
                user_dao.list_user_only(user_dao.search_name(email))
            case 3:
                print("********** MODIFICAR DATOS DEL USUARIO **********")
                user_dao.modify_user(user_dao.search_name(email))
            case 4:
                print("********** ELIMINAR USUARIO **********")
                user_dao.delete_user(user_dao.search_name(email))
            case 0:
                print("Gracias por visitar nuetra tienda.")
            case _:
                print("Opción no válida.")


try:
    # INICIAR SESION
    while True:
        print("¿Cómo quieres entrar a nuestra tienda?\n1-Iniciando sesión\n2-Creando una cuenta")
        metodo_login = int(input())
        # CONTROLAR QUE PONGA LA OPCION 1 O 2
        while metodo_login > 2 or metodo_login < 1:
            metodo_login = int(input("Introduzca una opcion entre 1 y 2\n"))

        if metodo_login == 1:
            email = method_login()  # LLAMAR AL METODO PARA INICIAR SESION
            if email is not None: # SI NO ES NULO SE SALE DEL BUCLE (se encontro usuario)
                break
        elif metodo_login == 2:
            email = method_signup()  # LLAMAR AL METODO PARA CREAR CUENTA
            if email is not None: # SI SE CREA BIEN LA CUENTA SALE DEL BUCLE
                break

    # MENU PRINCIPAL DESPUES DEL INICIO DE SESION
    print("\n\n¡Bienvenido a CubeX! ¿Qué desea hacer en nuestra tienda?" +
          "\n1-Ir al apartado de usuarios" +
          "\n2-Ir al apartado de cubos")
    opcion_apartado = int(input())
    if opcion_apartado == 1:
        # APARTADO USUARIOS
        apartado_usuario()  # LLAMAR AL METODO DE APARTADO USUARIOS

    elif opcion_apartado == 2:
        # APARTADO CUBOS
        apartado_productos()  # LLAMAR AL METODO DE APARTADO PRODUCTOS
except Exception as e:
    print(f"Ocurrió un error: {e}")
print("¡Vuelva pronto!")
