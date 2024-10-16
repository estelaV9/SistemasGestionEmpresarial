import json
from json import JSONDecodeError

from model import user

# FUNCION PARA CREAR USUARIOS Y GUARDARLOS EN JSON
def create_user(user_obj: user):
    user_data = user_obj.to_dict() # CONVERTIMOS EL OBJETO EN UN DICCIONARIO

    try:
        with open('users.json', 'r') as file:
            users = json.load(file) # SE LEE PRIMERO EL ARCHIVO Y SE GUARDA EN users (se evita que se sobreescriba)
    except json.JSONDecodeError:
        # SI EL ARCHIVO ESTA VACIO, SE INICIA LA LISTA VACIA (porque si no da error)
        users = []
    except FileNotFoundError:
        # SI NO ESTA CREADO EL ARCHIVO, SE INICIA LA LISTA VACIA
        users = []

    # BUCLE PARA SABER SI EL USUARIO YA TENIA UNA CUENTA
    for user_exist in users:
        if user_exist['Email'] == user_obj.email and user_exist['Password'] == user_obj.password:
            print(" kds fdsafdjksa f sjakf")
            # SI ENCUENTRA AL USUARIO CON ESE MAIL Y ESA CONTRASEÑA RETORNA FALSE Y NO SE CREARA LA CUENTA
            return False

    users.append(user_data) # AGREGAR EL NUEVO USUARIO A LA LISTA

    # ESCRIBIR LA LISTA DE USUARIO EN EL ARCHIVO DE JSON
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)  # Indent para mejor legibilidad
    return True

# FUNCION PARA LOGGEAR USUARIOS
def log_in (user_obj: user):
    with open('users.json', 'r') as file:
        user_data = json.load(file) # SE GUARDA LOS DATOS QUE SE CARGAN DEL JSON

    for users in user_data:
        if users['Email'] == user_obj.email and users['Password'] == user_obj.password:
            # SI ENCUENTRA AL USUARIO CON ESE MAIL Y ESA CONTRASEÑA ENTONCES SE PODRA LOGGEAR
            return True

    return False # SI NO HA ENCONTRADO USUARIO DEVOLVERA FALSE

# FUNCION PARA BUSCAR EL NOMBRE DEL USUARIO A PARTIR DEL EMAIL
def search_name (email):
    with open ('users.json', 'r') as file:
        list_user = json.load(file)

    # SE RECORRE LA LISTA PARA ENCONTRAR AL USUARIO Y RETORNAR EL NOMBRE
    for user in list_user:
        if user['Email'] == email:
            print(user['Name'])
            return user['Name']


# FUNCION PARA ELIMINAR USUARIO
def delete_user(user_name):
    with open('users.json', 'r') as file:
        list_user = json.load(file) # GUARDAR LOS USUARIOS

    for users in list_user:
        # SI EL NOMBRE DE USUARIO ES EL INTRODUCIDO SE ELIMINARA
        if users['Name'] == user_name:
            list_user.remove(users) # SE ELIMINA EL USUARIO
            break # SE SALE DEL BUCLE

    with open('users.json', 'w') as file:
        json.dump(list_user, file, indent=4)

    print(f"Usuario '{user_name}' se ha eliminado exitosamente.")

# FUNCION PARA IMPRIMIR TODOS LOS USUARIOS
def list_user():
    try:
        with open('users.json', 'r') as file:
            list_user_show = json.load(file) # GUARDAR LOS USUARIOS
    except FileNotFoundError:
        # SI NO SE HA ENCONTRADO ARCHIVO, INCIAR LA LISTA EN NULO
        list_user_show = []
    except JSONDecodeError:
        # SI EL JSON ESTA VACIO, INICIAR LA LISTA EN NULO
        list_user_show = []

    # RECORRER LA LISTA Y MOSTRARLOS
    for user in list_user_show:
        print(user.__str__())