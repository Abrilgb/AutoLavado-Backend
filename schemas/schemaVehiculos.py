# pylint: disable=invalid-name
''' Docstring for the schema_vehiculos module.'''
from datetime import datetime as datatime
from typing import Optional as optional
from pydantic import BaseModel

class VehiculoBase(BaseModel):
    '''Clase base para el esquema de vehículo'''
    au_modelo:str
    au_serie:str
    au_color:str
    au_estado:str
    au_placa:optional[str] = None
    au_tipo: str
    au_anio:datatime
    au_fecha_actualizacion:datatime

#pylint: disable=too-few-public-methods

class VehiculoCreate(VehiculoBase):
    '''Esta clase se utiliza para crear un nuevo vehículo'''

class VehiculoUpdate(VehiculoBase):
    '''Esta clase se utiliza para actualizar un vehículo existente'''

class Vehiculo(VehiculoBase):
    '''Esta clase se utiliza para representar un vehículo en la respuesta de la API'''
    id: int
    class Config:
        '''Configuración para permitir la conversión de objetos ORM a modelos Pydantic'''
        orm_mode = True

