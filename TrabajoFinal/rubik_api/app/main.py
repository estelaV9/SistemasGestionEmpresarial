from fastapi import FastAPI
import uvicorn
from app.routers import user, cube, solve_time, auth
from app.db.database import Base, engine

# FUNCION PARA CREAR LAS TABLAS DEFINIDAS EN LOS MODELOS
def create_tables():
    Base.metadata.create_all(bind=engine)  # CREA LAS TABLAS SI NO EXISTEN

# CREAR TABLAS AL INICIAR LA API
create_tables()

# INSTANCIA PRINCIPAL DE LA API
app = FastAPI(
    title="Rubik API",
    description="API para gestionar usuarios, cubos de Rubik y tiempos de resolución",
    version="1.0.0"
)

# INCLUIMOS LAS RUTAS DE USUARIO, CUBOS Y TIEMPOS
app.include_router(auth.router)
app.include_router(user.router)
app.include_router(cube.router)
app.include_router(solve_time.router)


# PUNTO DE ENTRADA PRINCIPAL
if __name__ == "__main__":
    # EJECUTAMOS EL SERVIDOR UVICORN EN EL PUERTO 8000 CON RECARGA AUTOMATICA
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)
