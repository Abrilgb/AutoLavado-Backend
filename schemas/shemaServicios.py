''' Doctsring de la clase SchemaServicios '''
from datetime import datetime as datatime
from typing import Optional as optional
from pydantic import BaseModel


class ServicioBase(BaseModel):
    '''Clase base para el schema de servicio'''
    nombre: str
    descripcion: optional[str] = None
    costo: float
    estatus: optional[str] = None
    fecha_registro: datatime
    fecha_modificacion: datatime


#pylint: disable=too-few-public-methods

class ServicioCreate(ServicioBase):
    '''Esta clase se utiliza para crear un nuevo servicio'''

class ServicioUpdate(ServicioBase):
    '''Esta clase se utiliza para actualizar un servicio existente'''

class Servicio(ServicioBase):
    '''Esta clase se utiliza para representar un servicio en la respuesta de la API'''
    id: int
    class Config:
        '''Configuración para permitir la conversión de objetos ORM a modelos Pydantic'''
        orm_mode = True