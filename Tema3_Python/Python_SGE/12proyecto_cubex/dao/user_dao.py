import json
from importlib.util import source_hash
from json import JSONDecodeError
from model import user


# FUNCION PARA LEER ARICHIVO Y NO DUPLICAR CODIGO
def leer_archivo():
    try:
        with open('users.json', 'r') as file:
            users = json.load(file)  # GUARDAR TODOS LOS USUARIOS EN UNA LISTA
    except (FileNotFoundError, JSONDecodeError):
        # SI NO SE HA ENCONTRADO ARCHIVO, INCIAR LA LISTA EN NULO
        users = []
    return users


# FUNCION CON SET PARA QUE UN USUARIO NO TENGA UN NOMBRE YA EXISTENTE
""" def unique_list_users(insert_name):
     # SE DECLARA UNA LISTA SET PARA QUE NO HAY ANOMBRES REPETIDOS
    usuarios_set = set(leer_archivo()) # SE GUARDA LOS USUARIOS QUE HAYA EN EL JSON
    if insert_name in usuarios_set:
        # SI EL NOMBRE ESTA EN LA BASE DE DATOS ENTONCES SALTA UN ERROR
        print(f"El nombre de usuario '{insert_name}' ya está en uso. Por favor, elige otro.")
    else:
        return True # DEVUELVE TRUE SI NO ESTA EL NOMBRE EN EL JSON """


# FUNCION PARA CREAR USUARIOS Y GUARDARLOS EN JSON
def create_user(user_obj: user):
    user_data = user_obj.to_dict()  # CONVERTIMOS EL OBJETO EN UN DICCIONARIO
    users = leer_archivo()

    # BUCLE PARA SABER SI EL USUARIO YA TENIA UNA CUENTA
    for user_exist in users:
        if user_exist['Email'] == user_obj.email and user_exist['Password'] == user_obj.password:
            # SI ENCUENTRA AL USUARIO CON ESE MAIL Y ESA CONTRASEÑA RETORNA FALSE Y NO SE CREARA LA CUENTA
            return False

    users.append(user_data)  # AGREGAR EL NUEVO USUARIO A LA LISTA

    # ESCRIBIR LA LISTA DE USUARIO EN EL ARCHIVO DE JSON
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)  # Indent para mejor legibilidad
    return True


# FUNCION PARA LOGGEAR USUARIOS
def log_in(user_obj: user):
    user_data = leer_archivo()

    for users in user_data:
        if users['Email'] == user_obj.email and users['Password'] == user_obj.password:
            # SI ENCUENTRA AL USUARIO CON ESE MAIL Y ESA CONTRASEÑA ENTONCES SE PODRA LOGGEAR
            return True

    return False  # SI NO HA ENCONTRADO USUARIO DEVOLVERA FALSE


# FUNCION PARA BUSCAR EL NOMBRE DEL USUARIO A PARTIR DEL EMAIL
def search_name(email):
    list_user = leer_archivo()

    # SE RECORRE LA LISTA PARA ENCONTRAR AL USUARIO Y RETORNAR EL NOMBRE
    for user in list_user:
        if user['Email'] == email:
            return user['Name']


# FUNCION PARA ELIMINAR USUARIO
def delete_user(user_name):
    list_user = leer_archivo()

    for users in list_user:
        # SI EL NOMBRE DE USUARIO ES EL INTRODUCIDO SE ELIMINARA
        if users['Name'] == user_name:
            list_user.remove(users)  # SE ELIMINA EL USUARIO
            break  # SE SALE DEL BUCLE

    with open('users.json', 'w') as file:
        json.dump(list_user, file, indent=4)

    print(f"Usuario '{user_name}' se ha eliminado exitosamente.")


# FUNCION PARA IMPRIMIR TODOS LOS USUARIOS
def list_user():
    list_user_show = leer_archivo()

    # RECORRER LA LISTA Y MOSTRARLOS
    for user in list_user_show:
        print(user.__str__())


# FUNCION PARA IMPRIMIR LA INFO DEL USUARIO
def list_user_only(user_name):
    list_user_show = leer_archivo()  # GUARDAR LOS USUARIOS

    # RECORRER LA LISTA Y MOSTRAR SU INFO
    for user in list_user_show:
        if user['Name'] == user_name:  # SI ES EL NOMBRE DE USUARIO ENTONCES MUESTRA SU INFORMACION
            print(user.__str__())


def modify_user(user_name):
    users = leer_archivo()  # GUARDAR LOS USUARIOS

    # RECORRER LA LISTA
    for users in users:
        if users['Name'] == user_name:
            # MODIFICAR DATOS
            new_name = input("Nombre: ")
            new_mail = input("Email: ")
            new_password = input("Password: ")
            # SETTEAR NUEVOS VALORES
            users['Name'] = new_name
            users['Email'] = new_mail
            users['Password'] = new_password
            break

    # ESCRIBIR LA NUEVA INFORMACION EN EL FICHERO
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)
    print(f"Usuario '{user_name}' se ha modificado exitosamente.")
