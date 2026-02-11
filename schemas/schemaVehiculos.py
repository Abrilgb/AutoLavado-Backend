''' Docstring for the schema_vehiculos module.'''
from datetime import datetime as datatime
from pydantic import BaseModel
from typing import Optional as optional

class VehiculoBase(BaseModel):
    '''Clase base para el esquema de vehículo'''
    modelo: str
    matricula: int 
    color: optional[str] = None
    tipo: optional[str] = None

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

