'''
    Docstring for the schema_user module.
'''
from datetime import datetime as datatime
from typing import Optional as optional

from pydantic import BaseModel, Field

class UserBase(BaseModel):
    '''Clase base para el esquema de usuario'''
    nombre: optional[str] = None
    papellido: optional[str] = None
    sapellido: optional[str] = None
    usuario: optional[str] = None
    direccion: optional[str] = None
    correo: optional[str] = None
    telefono: optional[str] = None
    password: optional[str] = None
    estatus: bool = True
    rol_id: optional[int] = None
    fecha_registro: optional[datatime] = None
    fecha_modificacion: optional[datatime] = None

#pylint: disable=too-few-public-methods
class UserCreate(UserBase):
    '''Esta clase se utiliza para crear un nuevo usuario'''

class UserUpdate(UserBase):
    '''Esta clase se utiliza para actualizar un usuario existente'''

class User(UserBase):
    '''Esta clase se utiliza para representar un usuario en la respuesta de la API'''
    id: int
    password: optional[str] = Field(default=None, exclude=True)  # No exponer el hash en la API

    model_config = {"from_attributes": True}

class UserLogin(BaseModel):
    '''Clase para el esquema de inicio de sesión de usuario'''
    telefono: optional[str] = None
    correo: optional[str] = None
    contrasena: str
