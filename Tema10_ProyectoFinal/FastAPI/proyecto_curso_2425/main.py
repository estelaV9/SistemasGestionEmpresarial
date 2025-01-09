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


# CREAMOS UNA INSTANCIA DE FASTAPI
app = FastAPI()

# PETICION GET QUE DEVUELVE UN MENSAJE
@app.get("/ruta1")
def ruta1():
    return {"mensaje": "Hemos creado nuestra primera API!!!"}


# PETICION POST PARA INSERTAR USUARIO E IMPRIMIRLO POR CONSOLA
@app.post("/ruta2")
# INDICAR QUE EL USUARIO QUE VA A RECIBIR SERA IGUAL AL MODELO QUE HEMOS CREADO
def ruta2(user: User):
    print(user) # IMPRIMIR EL USUARIO CUANDO SE EJECUTA
    print(user.nombre) # IMPRIMIR EL NOMBRE
    return True


""" DOCUMENTACION AUTOMATICA DE FASTAPI
    DESDE EL EXPLORADOR, INDICAMOS LA DIRECCION /docs PARA VER LA DOCUMENTACION
    DE LA API QUE SE HA CREADO DE FORMA AUTOMATICA. 
    AL PROBARLO, PODEMOS HACER CLIC EN "EXECUTE" PARA PROBAR LAS RUTAS. """

if __name__ == "__main__":
    # EJECUTAMOS EL SERVIDOR UVICORN EN EL PUERTO 8000 CON LA OPCION RELOAD ACTIVADA
    uvicorn.run("main:app", port=8000, reload=True)

# EL PARAMETRO "RELOAD" PERMITE RECARGAR EL CONTEXTO DEL SERVIDOR CADA VEZ QUE
# SE CAMBIE ALGO EN EL ARCHIVO main.py (CUANDO PULSEMOS CTRL+S).
