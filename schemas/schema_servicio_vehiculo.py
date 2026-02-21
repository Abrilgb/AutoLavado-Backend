from datetime import datetime, time
from typing import Optional
from pydantic import BaseModel


class ServicioVehiculoBase(BaseModel):
    vehiculo_id: int
    servicio_id: int
    operativo_id: int
    cajero_id: int
    as_fecha: datetime
    as_pagado: bool = False
    as_monto: float
    as_aprobado: bool = False
    as_hora: time
    as_estado: Optional[str] = None
    as_estatus: Optional[str] = None


class ServicioVehiculoCreate(ServicioVehiculoBase):
    pass


class ServicioVehiculoUpdate(ServicioVehiculoBase):
    pass


class ServicioVehiculo(ServicioVehiculoBase):
    as_id: int

    model_config = {"from_attributes": True}
