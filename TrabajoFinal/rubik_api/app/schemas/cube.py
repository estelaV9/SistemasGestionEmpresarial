from pydantic import BaseModel, EmailStr
from typing import Optional

# DEFINIR pydantic PARA TRABAJAR CON LOS DATOS
""" ********** CUBE MODEL *************** """
class CubeCreate(BaseModel):
    type: str
    owner_id: int


# MODELO CubeResponse PARA DEVOLVER DATOS DE UN CUBO
class CubeResponse(BaseModel):
    id: int
    type: str
    owner_id: int

# CUBE MODEL PARA UPDATE
class UpdateCube(BaseModel):  # Schema
    # SE PONE OPCIONAL PARA QUE NO SEA OBLIGATORIO ACTUALIZARTODO
    id: Optional[str] = None
    type: Optional[str] = None
    owner_id: Optional[EmailStr] = None