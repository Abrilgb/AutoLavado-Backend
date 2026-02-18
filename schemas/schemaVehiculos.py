from datetime import datetime
from typing import Optional
from pydantic import BaseModel, ConfigDict

class VehiculoBase(BaseModel):
    au_modelo: str
    au_serie: str
    au_color: str
    au_estado: str
    au_placa: Optional[str] = None
    au_tipo: str
    au_anio: datetime

class VehiculoCreate(VehiculoBase):
    pass

class VehiculoUpdate(VehiculoBase):
    pass

class Vehiculo(VehiculoBase):
    id: int
    au_fecha_actualizacion: datetime

    model_config = ConfigDict(from_attributes=True)
