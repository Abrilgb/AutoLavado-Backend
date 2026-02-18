from sqlalchemy import Column, Integer, String, Boolean, DateTime
from config.db import Base
from datetime import datetime

class Rol(Base):
    __tablename__ = "tbc_rol"

    ro_id = Column(Integer, primary_key=True, index=True)
    ro_descripcion = Column(String(100), nullable=False)
    ro_estatus = Column(Boolean, default=True)
    ro_fecha_registro = Column(DateTime, default=datetime.utcnow)
    ro_fecha_modificacion = Column(DateTime, default=datetime.utcnow)
