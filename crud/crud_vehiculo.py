from sqlalchemy.orm import Session
from datetime import datetime
from models.modelsVehiculos import Vehiculo
from schemas.schemaVehiculos import VehiculoCreate, VehiculoUpdate

def get_vehiculos(db: Session):
    return db.query(Vehiculo).all()

def get_vehiculo_by_id(db: Session, vehiculo_id: int):
    return db.query(Vehiculo).filter(Vehiculo.au_id == vehiculo_id).first()

def create_vehiculo(db: Session, vehiculo: VehiculoCreate):
    db_vehiculo = Vehiculo(
        au_modelo=vehiculo.au_modelo,
        au_serie=vehiculo.au_serie,
        au_color=vehiculo.au_color,
        au_estado=vehiculo.au_estado,
        au_placa=vehiculo.au_placa,
        au_tipo=vehiculo.au_tipo,
        au_anio=vehiculo.au_anio,
        au_fecha_actualizacion=datetime.now()
    )
    db.add(db_vehiculo)
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def update_vehiculo(db: Session, vehiculo_id: int, vehiculo: VehiculoUpdate):
    db_vehiculo = get_vehiculo_by_id(db, vehiculo_id)
    if not db_vehiculo:
        return None

    for key, value in vehiculo.model_dump().items():
        setattr(db_vehiculo, key, value)

    db_vehiculo.au_fecha_actualizacion = datetime.now()
    db.commit()
    db.refresh(db_vehiculo)
    return db_vehiculo

def delete_vehiculo(db: Session, vehiculo_id: int):
    db_vehiculo = get_vehiculo_by_id(db, vehiculo_id)
    if not db_vehiculo:
        return None

    db.delete(db_vehiculo)
    db.commit()
    return db_vehiculo
