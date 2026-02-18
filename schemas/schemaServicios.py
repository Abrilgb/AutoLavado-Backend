''' Docstring de la clase SchemaServicios '''
from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class ServicioBase(BaseModel):
    '''Clase base para el schema de servicio'''
    nombre: str
    descripcion: Optional[str] = None
    costo: float
    estatus: Optional[str] = None
    fecha_registro: datetime
    fecha_modificacion: datetime

class ServiciosCreate(ServicioBase):  # ← Cambié a ServiciosCreate (con 's')
    '''Esta clase se utiliza para crear un nuevo servicio'''
    pass

class ServiciosUpdate(ServicioBase):  # ← También con 's' para consistencia
    '''Esta clase se utiliza para actualizar un servicio existente'''
    pass

class Servicio(ServicioBase):
    '''Esta clase se utiliza para representar un servicio en la respuesta de la API'''
    servicio_id: int
    
    model_config = {"from_attributes": True}  # ✅ Pydantic v2