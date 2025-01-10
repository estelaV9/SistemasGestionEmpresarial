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