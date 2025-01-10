from fastapi import FastAPI
import uvicorn

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# DEFINIR pydantic PARA TRABAJAR CON LOS DATOS
""" ********** USER MODEL *************** """


class User(BaseModel):  # Schema
    id: int
    nombre: str
    apellido: str
    direccion: Optional[str]  # PARAMETRO OPCIONAL
    telefono: int
    creacion_user: datetime = datetime.now()  # FECHA POR DEFECTO


# MODELO CUYO CONTENIDO SERA EL ID DE USUARIO
class UserId(BaseModel):
    id: int


# CREAMOS UNA INSTANCIA DE FASTAPI
app = FastAPI()
listaUsuarios = []  # LISTA USUARIOS


# PETICION GET QUE DEVUELVE UN MENSAJE
@app.get("/ruta1")
def ruta1():
    return {"mensaje": "Hemos creado nuestra primera API!!!"}


# PETICION GET QUE DEVUELVE LOS USUARIOS
@app.get("/user")
def obtener_usuarios():
    return listaUsuarios


# PETICION GET QUE DEVUELVE UN USUARIO EN CONCRETO
@app.get("/user/{user_id}")
def obtener_usuario(user_id: int):
    for user in listaUsuarios:
        # ACCEDER AL ID DE USER Y COMPARAR CON EL ID QUE SE PASA COMO QUERY
        if user["id"] == user_id:
            return {"usuario": user}
    # SI SE PASA UN ID DE UN USUARIO QUE NO EXISTE
    return {"Respuesta": "Usuario no encontrado"}


# PETICION POST PARA INSERTAR USUARIO E IMPRIMIRLO POR CONSOLA
@app.post("/user")
# INDICAR QUE EL USUARIO QUE VA A RECIBIR SERA IGUAL AL MODELO QUE HEMOS CREADO
def crear_usuario(user: User):
    # ASIGNAMOS EL DICCIONARIO A UNA VARIABLE
    usuarioDiccionario = user.model_dump()  # CONVERTIR EN UN DICIONARIO
    """ EL USUARIO QUE ENVIAMOS POR Swagger SE AÑADE A LA LISTA DE USUARIOS """
    listaUsuarios.append(usuarioDiccionario)
    print(usuarioDiccionario)  # IMPRIMIR EL DICCIONARIO
    return {"Respuesta": "Usuario creado!"}


# PETICION POST PARA OBTENER UN USUARIO MEDIANTE UN "BODY" DE JSON
@app.post("/userjson")
def obtener_usuario_json(user_id: UserId):
    for user in listaUsuarios:
        # ACCEDER AL ID DE USER Y COMPARAR CON EL ID DE user_id QUE SE PASA COMO JSON
        if user["id"] == user_id.id:
            return {"usuario": user}
    # SI SE PASA UN ID DE USUARIO QUE NO EXISTE
    return {"respuesta": "Usuario no encontrado"}


# PETICION DELETE PARA ELIMINAR USUARIO POR ID
@app.delete("/user/{user_id}")
def eliminar_usuario(user_id: int):
    # NECESITAMOS SABER EL INDICE Y EL VALOR PARA VER SI EL user_id = AL QUE ESTAMOS RECORRIENDO
    for index, user in enumerate(listaUsuarios):
        if user["id"] == user_id:
            listaUsuarios.pop(index)
            return {"Respuesta": "Usuario eliminado correctamente"}
    return {"Respuesta": "Usuario NO encontrado"}


# PETICION PUT PARA MODIFICAR POR ID
@app.put("/user/{user_id}")
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


""" DOCUMENTACION AUTOMATICA DE FASTAPI
    DESDE EL EXPLORADOR, INDICAMOS LA DIRECCION /docs PARA VER LA DOCUMENTACION
    DE LA API QUE SE HA CREADO DE FORMA AUTOMATICA. 
    AL PROBARLO, PODEMOS HACER CLIC EN "EXECUTE" PARA PROBAR LAS RUTAS. """

if __name__ == "__main__":
    # EJECUTAMOS EL SERVIDOR UVICORN EN EL PUERTO 8000 CON LA OPCION RELOAD ACTIVADA
    uvicorn.run("main:app", port=8000, reload=True)

# EL PARAMETRO "RELOAD" PERMITE RECARGAR EL CONTEXTO DEL SERVIDOR CADA VEZ QUE
# SE CAMBIE ALGO EN EL ARCHIVO main.py (CUANDO PULSEMOS CTRL+S).
