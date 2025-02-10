from pydantic import BaseModel, EmailStr
from typing import Optional

# DEFINIR pydantic PARA TRABAJAR CON LOS DATOS
""" ********** USER MODEL *************** """
class UserCreate(BaseModel):  # Schema
    username: str
    # CORREO VALIDADO COMO DIRECCION DE CORREO
    email: EmailStr
    password: str

# MODELO UserResponse PARA DEVOLVER DATOS DE UN USUARIO
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr

# USER MODEL PARA UPDATE
class UpdateUser(BaseModel):  # Schema
    # SE PONE OPCIONAL PARA QUE NO SEA OBLIGATORIO ACTUALIZARTODO
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None