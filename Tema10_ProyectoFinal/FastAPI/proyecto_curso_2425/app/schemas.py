from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# DEFINIR pydantic PARA TRABAJAR CON LOS DATOS
""" ********** USER MODEL *************** """
class User(BaseModel):  # Schema
    username: str
    password: str
    nombre: str
    apellido: str
    direccion: Optional[str]  # PARAMETRO OPCIONAL
    telefono: int
    correo: str
    creacion_user: datetime = datetime.now()  # FECHA POR DEFECTO


""""# MODELO CUYO CONTENIDO SERA EL ID DE USUARIO
class UserId(BaseModel):
    id: int"""

# MODELO ShowUser PARA DEVOLVER DATOS DE UN USUARIO
class ShowUser(BaseModel):
    username:str
    nombre:str
    correo:str

# USER MODEL PARA UPDATE
class UpdateUser(BaseModel):  # Schema
    username: str = None
    password: str = None
    nombre: str = None
    apellido: str = None
    direccion: str = None # PARAMETRO OPCIONAL
    telefono: int = None
    correo: str = None