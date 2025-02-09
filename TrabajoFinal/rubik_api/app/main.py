from fastapi import FastAPI
import uvicorn
from app.routers import user, cube, solve_time
from app.db.database import Base, engine

# FUNCION PARA CREAR LAS TABLAS DEFINIDAS EN LOS MODELOS
def create_tables():
    Base.metadata.create_all(bind=engine)  # CREA LAS TABLAS SI NO EXISTEN

# LLAMADA A LA FUNCIÓN PARA ASEGURARSE DE QUE LAS TABLAS SE CREAN AL INICIAR LA API
create_tables()

# INSTANCIA PRINCIPAL DE LA API
app = FastAPI(
    title="Rubik API",
    description="API para gestionar usuarios, cubos de Rubik y tiempos de resolución",
    version="1.0.0"
)

# INCLUIMOS LAS RUTAS DE USUARIO, CUBOS Y TIEMPOS
app.include_router(user.router)
app.include_router(cube.router)
app.include_router(solve_time.router)

# DOCUMENTACIÓN AUTOMÁTICA DISPONIBLE EN /docs Y /redoc
# /docs = Swagger UI | /redoc = Redoc UI

# PUNTO DE ENTRADA PRINCIPAL
if __name__ == "__main__":
    # EJECUTAMOS EL SERVIDOR UVICORN EN EL PUERTO 8000 CON RECARGA AUTOMÁTICA
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)

# EL PARÁMETRO "reload=True" HACE QUE EL SERVIDOR SE ACTUALICE AUTOMÁTICAMENTE CUANDO GUARDAS CAMBIOS
