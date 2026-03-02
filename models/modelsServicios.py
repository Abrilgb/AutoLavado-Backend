"""
Este módulo define el modelo Autoservicio para la base de datos (r_auto_servicio).
"""
# pylint: disable=too-few-public-methods
from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, Float, Time, String
from sqlalchemy.sql import func
from config.db import Base


class Servicios(Base):
    """
    Clase que representa la tabla tbc_servicio en la base de datos.
    """
    __tablename__ = "tbc_servicio"
    
    servicio_id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(45), nullable=True)
    costo = Column(Float, nullable=False)
    duracion = Column(Integer, nullable=True)
    estatus = Column(String(45), nullable=True)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_modificacion = Column(DateTime, default=func.now(), onupdate=func.now())

    
