# DEFINIR TODOS LOS MODELOS DE LA BASE DE DATOS
from app.db.database import Base
# IMPORTA LOS TIPOS DE DATOS Y LA CLASE COLUMN
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from datetime import datetime
from sqlalchemy.schema import ForeignKey
from sqlalchemy.orm import relationship

""" TABLA USER """
class User(Base):
    __tablename__ = "usuario"
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    nombre = Column(String)
    apellido = Column(String)
    direccion = Column(String)
    telefono = Column(Integer)
    correo = Column(String, unique=True)
    creacion = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    estado = Column(Boolean, default=False)
    venta = relationship("Venta", backref="usuario", cascade="delete,merge")


""" TABLA VENTA """
class Venta(Base):
    __tablename__ = "venta"
    id = Column(Integer, primary_key=True, autoincrement=True)
    usuario_id = Column(Integer, ForeignKey("usuario.id", ondelete="CASCADE"))
    venta = Column(Integer)
    ventas_productos = Column(Integer)
