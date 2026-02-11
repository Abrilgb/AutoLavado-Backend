"""
Este módulo define el modelo Autoservicio para la base de datos (r_auto_servicio).
"""
# pylint: disable=too-few-public-methods
from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, Float, Time
from sqlalchemy.sql import func
from config.db import Base


class Servico(Base):
    """
    Clase que representa la tabla tbd_servicio_vehiculo en la base de datos.
    """
    __tablename__ = "tbb_servicio_"
    
    Id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(45), nullable=False)
    descripcion = Column(String(45), nullable=True)
    costo = Column(Float, nullable=False)
    estatus = Column(String(45), nullable=True)
    fecha_registro = Column(DateTime, default=func.now())
    fecha_modificacion = Column(DateTime, default=func.now(), onupdate=func.now())

    
