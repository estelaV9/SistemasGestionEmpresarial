from pydantic import BaseModel
from datetime import datetime

# DEFINIR pydantic PARA TRABAJAR CON LOS DATOS
""" ********** SOLVE TIME MODEL *************** """
class SolveTimeCreate(BaseModel):
    time_seconds: float
    cube_id: int
    user_id: int


# MODELO SolveTimeResponse PARA DEVOLVER DATOS DE UN TIEMPO
class SolveTimeResponse(BaseModel):
    id: int
    time_seconds: float
    date: datetime
    cube_id: int
    user_id: int