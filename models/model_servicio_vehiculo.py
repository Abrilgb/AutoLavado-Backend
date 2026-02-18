"""
Este módulo define el modelo Autoservicio para la base de datos (r_auto_servicio) y para unir todo.
"""
# pylint: disable=too-few-public-methods
from sqlalchemy import Column, Integer, Boolean, ForeignKey, DateTime, Float, Time, String
from sqlalchemy.sql import func
from config.db import Base
from enum import Enum

class SolicitudServicio:
    '''Clase que representa los estados de solicitud de servicio.
    '''
    Programada = "Programada"
    En_Proceso = "En Proceso"
    Completada = "Completada"
    Cancelada = "Cancelada"

class Autoservicio(Base):
    """
    Clase que representa la tabla tbd_servicio_vehiculo en la base de datos.
    """
    __tablename__ = "tbd_servicio_vehiculo"

    as_id = Column(Integer, primary_key=True, index=True)
    vehiculo_id = Column(Integer, ForeignKey("tbb_vehiculo.au_id"))
    servicio_id = Column(Integer, ForeignKey("tbb_servicio_id"))
    operativo_id = Column(Integer, ForeignKey("tbb_usuario.id"))
    cajero_id = Column(Integer, ForeignKey("tbb_usuario.id"))
    # pylint: disable=not-callable
    as_fecha = Column(DateTime, default=func.now())
    as_pagado = Column(Boolean, default=False, nullable=False)
    as_monto = Column(Float, nullable=False)
    as_aprobado = Column(Boolean, default=False, nullable=False)
    as_hora = Column(Time, default=func.now())
    as_estado = Column(String(45), nullable=True)
    as_estatus = Column(String(45), nullable=True)
