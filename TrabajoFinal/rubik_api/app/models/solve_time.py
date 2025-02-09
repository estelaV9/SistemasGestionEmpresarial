from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from app.db.database import Base

# MODELO DE LOS TIEMPOS
class SolveTime(Base):
    __tablename__ = "solve_times"  # NOMBRE DE LA TABLA EN LA BASE DE DATOS

    # COLUMNAS DE LA TABLA SOLVE_TIMES
    id = Column(Integer, primary_key=True, index=True)  # ID UNICO DEL TIEMPO
    time_seconds = Column(Float, nullable=False)  # TIEMPO EN SEGUNDOS
    date = Column(DateTime, default=datetime.utcnow)  # FECHA DEL REGISTRO

    # CLAVES FORANEAS PARA RELACIONAR EL CUBO Y EL USUARIO
    cube_id = Column(Integer, ForeignKey("cubes.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    # RELACIONES CON EL CUBO Y EL USUAIRO
    cube = relationship("Cube", back_populates="solve_times")
    user = relationship("User", back_populates="solve_times")
