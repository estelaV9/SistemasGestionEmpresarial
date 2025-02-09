from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.database import Base

# MODELO DE CUBO DE RUBIK
class Cube(Base):
    __tablename__ = "cubes"  # NOMBRE DE LA TABLA EN LA BASE DE DATOS

    # COLUMNAS DE LA TABLA CUBES
    id = Column(Integer, primary_key=True, index=True)  # ID UNICO DEL CUBO
    type = Column(String, nullable=False)  # TIPO DE CUBO

    # CLAVE FORANEA QUE RELACIONA EL CUBO CON UN USUARIO
    owner_id = Column(Integer, ForeignKey("users.id"))

    # RELACIONES CON OTRAS TABLAS
    # EL USUARIO ASOCIADO
    owner = relationship("User", back_populates="cubes")
    # TIEMPOS DE RESOLUCION ASOCIADOS AL CUBO
    solve_times = relationship("SolveTime", back_populates="cube")