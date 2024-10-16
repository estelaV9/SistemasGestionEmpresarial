import json

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
        user = []

    users.append(user_data) # AGREGAR EL NUEVO USUARIO A LA LISTA

    # ESCRIBIR LA LISTA DE USUARIO EN EL ARCHIVO DE JSON
    with open('users.json', 'w') as file:
        json.dump(users, file, indent=4)  # Indent para mejor legibilidad

def log_in (user_obj: user):
    with open('users.json', 'r') as file:
        user_data = json.load(file) # SE GUARDA LOS DATOS QUE SE CARGAN DEL JSON

    for users in user_data:
        if users['Email'] == user_obj.email and users['Password'] == user_obj.password:
            # SI ENCUENTRA AL USUARIO CON ESE MAIL Y ESA CONTRASEÑA ENTONCES SE PODRA LOGGEAR
            print("fdskfldsa")
            return True

    print("jkfnsjf")
    return False # SI NO HA ENCONTRADO USUARIO DEVOLVERA FALSE