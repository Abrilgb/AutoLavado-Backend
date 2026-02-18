from datetime import datetime
from pydantic import BaseModel, ConfigDict

class RolBase(BaseModel):
    ro_descripcion: str
    ro_estatus: bool = True
    ro_fecha_registro: datetime | None = None
    ro_fecha_modificacion: datetime | None = None

class RolCreate(RolBase):
    pass

class RolUpdate(RolBase):
    pass

class Rol(RolBase):
    ro_id: int
    model_config = ConfigDict(from_attributes=True)
