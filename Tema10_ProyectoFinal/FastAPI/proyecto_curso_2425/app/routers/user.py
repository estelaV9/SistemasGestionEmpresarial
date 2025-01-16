from fastapi import APIRouter, Depends
# IMPORTAR LOS ESQUEMAS PARA PODER USARLOS
from app.schemas import User, UserId
from app.db.database import get_db
from sqlalchemy.orm import Session
from app import models

listaUsuarios = []  # LISTA USUARIOS

""" APIRouter ES UN CLASE QUE SE UTILIZA PARA ORGANIZAR Y ESTRUCTURAR
RUTAS DE API """
router = APIRouter(
    # ENRUTADOR. LAS RUTAS DEFINIDAS DENTRO, ESTARAN PRECEDIDAS POR "/user"
    prefix="/user",
    # LOS TAGS SE UTILIZAN PARA ORGANIZAR Y DOCUMENTAR RUTAS
    tags=["Users"]
)


# PETICION GET QUE DEVUELVE UN MENSAJE
@router.get("/ruta1")
def ruta1():
    return {"mensaje": "Hemos creado nuestra primera API!!!"}


# PETICION GET QUE DEVUELVE LOS USUARIOS
@router.get("/")
def obtener_usuarios(db: Session = Depends(get_db)): # LA RUTA RECIBE LA BD
    data = db.query(models.User).all()
    print(data)
    return listaUsuarios


# PETICION GET QUE DEVUELVE UN USUARIO EN CONCRETO
@router.get("/{user_id}")
def obtener_usuario(user_id: int):
    for user in listaUsuarios:
        # ACCEDER AL ID DE USER Y COMPARAR CON EL ID QUE SE PASA COMO QUERY
        if user["id"] == user_id:
            return {"usuario": user}
    # SI SE PASA UN ID DE UN USUARIO QUE NO EXISTE
    return {"Respuesta": "Usuario no encontrado"}


# PETICION POST PARA INSERTAR USUARIO E IMPRIMIRLO POR CONSOLA
@router.post("/")
# INDICAR QUE EL USUARIO QUE VA A RECIBIR SERA IGUAL AL MODELO QUE HEMOS CREADO
def crear_usuario(user: User, db:Session=Depends(get_db)):
    # ASIGNAMOS EL DICCIONARIO A UNA VARIABLE
    usuarioDiccionario = user.model_dump()  # CONVERTIR EN UN DICIONARIO

    # USER E SLO QUE LLEGA MEIDANTE EL ESQUEMA DEL BODY usuario.append(usuario)
    nuevo_usuario = models.User(
        username = usuarioDiccionario["username"],
        password = usuarioDiccionario["password"],
        nombre = usuarioDiccionario["nombre"],
        apellido = usuarioDiccionario["apellido"],
        direccion = usuarioDiccionario["direccion"],
        telefono = usuarioDiccionario["telefono"],
        correo = usuarioDiccionario["correo"],
    )
    db.add(nuevo_usuario)
    db.commit()
    db.refresh(nuevo_usuario)

    """ EL USUARIO QUE ENVIAMOS POR Swagger SE AÑADE A LA LISTA DE USUARIOS 
    listaUsuarios.routerend(usuarioDiccionario)
    print(usuarioDiccionario)  # IMPRIMIR EL DICCIONARIO """
    return {"Respuesta": "Usuario creado!"}


# PETICION POST PARA OBTENER UN USUARIO MEDIANTE UN "BODY" DE JSON
@router.post("/userjson")
def obtener_usuario_json(user_id: UserId):
    for user in listaUsuarios:
        # ACCEDER AL ID DE USER Y COMPARAR CON EL ID DE user_id QUE SE PASA COMO JSON
        if user["id"] == user_id.id:
            return {"usuario": user}
    # SI SE PASA UN ID DE USUARIO QUE NO EXISTE
    return {"respuesta": "Usuario no encontrado"}


# PETICION DELETE PARA ELIMINAR USUARIO POR ID
@router.delete("/{user_id}")
def eliminar_usuario(user_id: int):
    # NECESITAMOS SABER EL INDICE Y EL VALOR PARA VER SI EL user_id = AL QUE ESTAMOS RECORRIENDO
    for index, user in enumerate(listaUsuarios):
        if user["id"] == user_id:
            listaUsuarios.pop(index)
            return {"Respuesta": "Usuario eliminado correctamente"}
    return {"Respuesta": "Usuario NO encontrado"}


# PETICION PUT PARA MODIFICAR POR ID
@router.put("/{user_id}")
def actualizar_usuario(user_id: int, updateUser: User):
    # NECESITAMOS SABER EL INDICE Y EL VALOR PARA VER SI EL user_id ES = AL QUE ESTAMOS RECORREINDO
    for index, user in enumerate(listaUsuarios):
        if user["id"] == user_id:
            listaUsuarios[index]["id"] = updateUser.model_dump()["id"]
            listaUsuarios[index]["nombre"] = updateUser.model_dump()["nombre"]
            listaUsuarios[index]["apellido"] = updateUser.model_dump()["apellido"]
            listaUsuarios[index]["direccion"] = updateUser.model_dump()["direccion"]
            listaUsuarios[index]["telefono"] = updateUser.model_dump()["telefono"]
            return {"Respuesta": "Usuario NO encontrado"}
    return {"Respuesta": "Usuario actualizado correctamente"}
