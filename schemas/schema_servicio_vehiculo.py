'''Doctstring for the schema_servicio_vehiculo module.'''
from datetime import datetime as datatime
from typing import Optional as optional
from pydantic import BaseModel

class ServicioVehiculoBase(BaseModel):
    '''Clase base para el esquema de servicio de vehículo'''
    vehiculo_id:str 
    servicio:str
    operativo_id:str 
    cajero_id:str
    as_fecha:datatime
    as_pagado:bool = False
    as_monto:float
    as_aprobado:bool = False
    as_hora:datatime
    as_estado:optional[str] = None
    as_estatus:optional[str] = None

#pylint: disable=too-few-public-methods
class ServicioVehiculoCreate(ServicioVehiculoBase):
    '''Esta clase se utiliza para crear un nuevo servicio de vehículo'''
    pass

class ServicioVehiculoUpdate(ServicioVehiculoBase):
    '''Esta clase se utiliza para actualizar un servicio de vehículo existente'''
    pass

class ServicioVehiculo(ServicioVehiculoBase):
    '''Esta clase se utiliza para representar un servicio de vehículo en la respuesta de la API'''
    id: int
    class Config:
        '''Configuración para permitir la conversión de objetos ORM a modelos Pydantic'''
        orm_mode = True
