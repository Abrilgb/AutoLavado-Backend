''' Docstring  for the schema_clientes module.'''
from datetime import datetime as datatime
from pydantic import BaseModel
from typing import Optional as optional

class ClienteBase(BaseModel):
    '''Clase base para el esquema de cliente'''
    nombre: str
    papellido: str
    sapellido: str
    direccion: str
    correo: str
    telefono: str
    estatus: bool
    fecha_registro: datatime
    fecha_modificacion: datatime

#pylint: disable=too-few-public-methods
class ClienteCreate(ClienteBase):
    '''Esta clase se utiliza para crear un nuevo cliente'''

class ClienteUpdate(ClienteBase):
    '''Esta clase se utiliza para actualizar un cliente existente'''

class Cliente(ClienteBase):
    '''Esta clase se utiliza para representar un cliente en la respuesta de la API'''
    id: int
    class Config:
        '''Configuración para permitir la conversión de objetos ORM a modelos Pydantic'''
        orm_mode = True

class ClienteLogin(BaseModel):
    '''Clase para el esquema de inicio de sesión de cliente'''
    telefono: optional[str] = None
    correo: optional[str] = None
    contrasena: str