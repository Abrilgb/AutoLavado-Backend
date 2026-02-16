''' Docstring for the crud_rols module.'''
import models.model_servicio_vehiculo
import schemas.schema_servicio_vehiculo
from sqlalchemy.orm import Session

#pylint: disable=too-few-public-methods
def get_servicio_vehiculo(db: Session, skip: int=0, limit: int=10):
    return db.query(models.model_servicio_vehiculo.servicio_vehiculo).offset(skip).limit(limit).all()

def create_servicio_vehiculo(db: Session, servicio_vehiculo: models.model_servicio_vehiculo.servicio_vehiculo):
    db_servicio_vehiculo = models.model_servicio_vehiculo.servicio_vehiculo(
        vehiculo_id=servicio_vehiculo.vehiculo_id,
        servicio=servicio_vehiculo.servicio,
        operativo_id=servicio_vehiculo.operativo_id,
        cajero_id=servicio_vehiculo.cajero_id,
        as_fecha=servicio_vehiculo.as_fecha,
        as_pagado=servicio_vehiculo.as_pagado
    )
    db.add(db_servicio_vehiculo)
    db.commit()
    db.refresh(db_servicio_vehiculo)
    return db_servicio_vehiculo

def delete_servicio_vehiculo(db: Session, servicio_vehiculo_id: int):
    db_servicio_vehiculo = db.query(models.model_servicio_vehiculo.servicio_vehiculo).filter(models.model_servicio_vehiculo.servicio_vehiculo.as_id == servicio_vehiculo_id).first()
    if db_servicio_vehiculo:
        db.delete(db_servicio_vehiculo)
        db.commit()
        return True
    return False

def update_servicio_vehiculo(db: Session, servicio_vehiculo_id: int, servicio_vehiculo: models.model_servicio_vehiculo.servicio_vehiculo):
    db_servicio_vehiculo = db.query(models.model_servicio_vehiculo.servicio_vehiculo).filter(models.model_servicio_vehiculo.servicio_vehiculo.as_id == servicio_vehiculo_id).first()
    if db_servicio_vehiculo:
        db_servicio_vehiculo.vehiculo_id = servicio_vehiculo.vehiculo_id
        db_servicio_vehiculo.servicio = servicio_vehiculo.servicio
        db_servicio_vehiculo.operativo_id = servicio_vehiculo.operativo_id
        db_servicio_vehiculo.cajero_id = servicio_vehiculo.cajero_id
        db_servicio_vehiculo.as_fecha = servicio_vehiculo.as_fecha
        db_servicio_vehiculo.as_pagado = servicio_vehiculo.as_pagado
        db.commit()
        db.refresh(db_servicio_vehiculo)
        return db_servicio_vehiculo
    return None

def get_servicio_vehiculo_by_id(db: Session, servicio_vehiculo_id: int):
    return db.query(models.model_servicio_vehiculo.servicio_vehiculo).filter(models.model_servicio_vehiculo.servicio_vehiculo.as_id == servicio_vehiculo_id).first()
