''' Docstring for the crud_rols module.'''
import models.modelsVehiculos
import schemas.schemaVehiculos
from sqlalchemy.orm import Session

#pylint: disable=too-few-public-methods
def get_vehiculo(db: Session, skip: int=0, limit: int=10):
    return db.query(models.modelsVehiculos.Vehiculos).offset(skip).limit(limit).all()

def create_vehiculo(db: Session, vehiculo: models.modelsVehiculos.Vehiculos):
    db_vehiculo = models.modelsVehiculos.Vehiculos(
        au_marca=vehiculo.au_marca,
        au_modelo=vehiculo.au_modelo,
        au_tipo=vehiculo.au_tipo,
        au_anio=vehiculo.au_anio,
        au_fecha_actualizacion=vehiculo.au_fecha_actualizacion,
        cl_id=vehiculo.cl_id
    )
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def delete_vehiculo(db: Session, vehiculo_id: int):
    db_vehiculo = db.query(models.modelsVehiculos.Vehiculos).filter(models.modelsVehiculos.Vehiculos.au_id == vehiculo_id).first()
    if db_vehiculo:
        db.delete(db_vehiculo)
        db.commit()
        return True
    return False

def update_vehiculo(db: Session, vehiculo_id: int, vehiculo: models.modelsVehiculos.Vehiculos):
    db_vehiculo = db.query(models.modelsVehiculos.Vehiculos).filter(models.modelsVehiculos.Vehiculos.au_id == vehiculo_id).first()
    if db_vehiculo:
        db_vehiculo.au_marca = vehiculo.au_marca
        db_vehiculo.au_modelo = vehiculo.au_modelo
        db_vehiculo.au_tipo = vehiculo.au_tipo
        db_vehiculo.au_anio = vehiculo.au_anio
        db_vehiculo.au_fecha_actualizacion = vehiculo.au_fecha_actualizacion
        db_vehiculo.cl_id = vehiculo.cl_id
        db.commit()
        db.refresh(db_vehiculo)
        return db_vehiculo
    return None

def get_vehiculo_by_id(db: Session, vehiculo_id: int):
    return db.query(models.modelsVehiculos.Vehiculos).filter(models.modelsVehiculos.Vehiculos.au_id == vehiculo_id).first()

