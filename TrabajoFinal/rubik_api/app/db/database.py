# PERMITE ESTABLECER LA CONEXION CON UNA BD ESPECIFICANDO LA URL DE CONEXION
from sqlalchemy import create_engine

# CLASE BASE PARA DEFINIR MODELOS DE TABLAS DE BD EN SQLAlchemy
from sqlalchemy.orm import declarative_base

# CLASE QUE CREA OBJETOS PARA MANEJAR SESIONES CON LA BD
from sqlalchemy.orm import sessionmaker

# URL DE LA BASE DE DATOS
""" - postgresql: El tipo de base de datos.
    - odoo:odoo: Las credenciales de usuario (usuario: odoo, contraseña: odoo).
    - localhost:5342: Dirección del servidor de base de datos (localhost y puerto 5342).
    - fastapi-database: Nombre de la base de datos. """
SQLALCHEMY_DATABASE_URL = "postgresql://odoo:odoo@localhost:5342/rubikapi-database"

# CREAR MOTOR DE CONEXION QUE INTERACTUARA CON LA BD UTILIZANDO LA URL
engine = create_engine(SQLALCHEMY_DATABASE_URL)
# CONFIGURA UN GENERADOR DE SESIONS
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# CREAR BASE PARA DEFINIR LOS MODELOS DE LA TABLA BD
Base = declarative_base()  # LOS MODELOS HEREDAN DE ESTA CLASE

# FUNCION QUE GESTIONA EL CICLO DE VIDA DE UNA SESION
def get_db():
    db = SessionLocal()  # CREAR UNA NUEVA SESION
    try:
        yield db  # DEVUELVE LA SESION PARA SU USO
    finally:
        db.close()  # CIERRA LA SESION DESPUES DE USARLA
