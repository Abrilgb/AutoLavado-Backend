''' Doctsring de la clase SchemaServicios '''
from datetime import datetime as datatime
from pydantic import BaseModel
from typing import Optional as optional

class ServicioBase(BaseModel):
    '''Clase base para el schema de servicio'''
    fecha: datatime
    monto: int 
    aprobado: bool
    pagado: int 
    hora: datatime

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


