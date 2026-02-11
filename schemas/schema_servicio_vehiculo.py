'''Doctstring for the schema_servicio_vehiculo module.'''
from datetime import datetime as datatime
from pydantic import BaseModel
from typing import Optional as optional

class ServicioVehiculoBase(BaseModel):
    '''Clase base para el esquema de servicio de vehículo'''
    au_id: int
    se_id: int
    us_id: int
    as_fecha: datatime
    as_pagado: bool
    as_monto: float
    as_aprobado: bool
    as_hora: datatime

#pylint: disable=too-few-public-methods
class ServicioVehiculoCreate(ServicioVehiculoBase):
    '''Esta clase se utiliza para crear un nuevo servicio de vehículo'''

class ServicioVehiculoUpdate(ServicioVehiculoBase):
    '''Esta clase se utiliza para actualizar un servicio de vehículo existente'''

class ServicioVehiculo(ServicioVehiculoBase):
    '''Esta clase se utiliza para representar un servicio de vehículo en la respuesta de la API'''
    id: int
    class Config:
        '''Configuración para permitir la conversión de objetos ORM a modelos Pydantic'''
        orm_mode = True

