from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.db.database import Base


# MODELO DE USUARIO
class User(Base):
    __tablename__ = "users"  # NOMBRE DE LA TABLA EN LA BASE DE DATOS

    # COLUMNAS DE LA TABLA USERS
    id = Column(Integer, primary_key=True, index=True)  # ID UNICO DEL USUARIO
    username = Column(String, unique=True, index=True, nullable=False)  # NOMBRE DE USUARIO UNICO
    email = Column(String, unique=True, index=True, nullable=False)  # EMAIL UNICO
    password = Column(String, nullable=False)  # CONTRASEÑA

    # RELACIONES
    # UN USUARIO PUEDE TENER VARIOS CUBOS
    cubes = relationship("Cube", back_populates="owner")
    # UN USUARIO PUEDE REGISTRAR VARIOS TIEMPOS
    solve_times = relationship("SolveTime", back_populates="user")
