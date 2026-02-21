from models.model_servicio_vehiculo import Autoservicio
from models.modelsVehiculos import Vehiculo
from models.modelsServicios import Servicios
from models.modelUser import User
from schemas.schema_servicio_vehiculo import ServicioVehiculoCreate, ServicioVehiculoUpdate
from sqlalchemy.orm import Session


def get_servicio_vehiculo(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Autoservicio).offset(skip).limit(limit).all()


def _validar_referencias(db: Session, vehiculo_id: int, servicio_id: int, operativo_id: int, cajero_id: int) -> None:
    """Comprueba que existan vehículo, servicio y usuarios. Lanza ValueError si no."""
    if db.query(Vehiculo).filter(Vehiculo.au_id == vehiculo_id).first() is None:
        raise ValueError(f"Vehículo con ID {vehiculo_id} no encontrado.")
    if db.query(Servicios).filter(Servicios.servicio_id == servicio_id).first() is None:
        raise ValueError(f"Servicio con ID {servicio_id} no encontrado.")
    if db.query(User).filter(User.id == operativo_id).first() is None:
        raise ValueError(f"Operativo (usuario) con ID {operativo_id} no encontrado.")
    if db.query(User).filter(User.id == cajero_id).first() is None:
        raise ValueError(f"Cajero (usuario) con ID {cajero_id} no encontrado.")


def create_servicio_vehiculo(db: Session, servicio_vehiculo: ServicioVehiculoCreate):
    _validar_referencias(
        db,
        servicio_vehiculo.vehiculo_id,
        servicio_vehiculo.servicio_id,
        servicio_vehiculo.operativo_id,
        servicio_vehiculo.cajero_id,
    )
    db_servicio_vehiculo = Autoservicio(
        vehiculo_id=servicio_vehiculo.vehiculo_id,
        servicio_id=servicio_vehiculo.servicio_id,
        operativo_id=servicio_vehiculo.operativo_id,
        cajero_id=servicio_vehiculo.cajero_id,
        as_fecha=servicio_vehiculo.as_fecha,
        as_pagado=servicio_vehiculo.as_pagado,
        as_monto=servicio_vehiculo.as_monto,
        as_aprobado=servicio_vehiculo.as_aprobado,
        as_hora=servicio_vehiculo.as_hora,
    )
    db.add(db_servicio_vehiculo)
    db.commit()
    db.refresh(db_servicio_vehiculo)
    return db_servicio_vehiculo


def delete_servicio_vehiculo(db: Session, servicio_vehiculo_id: int):
    db_servicio_vehiculo = db.query(Autoservicio).filter(
        Autoservicio.as_id == servicio_vehiculo_id
    ).first()

    if db_servicio_vehiculo:
        db.delete(db_servicio_vehiculo)
        db.commit()
        return True

    return False


def update_servicio_vehiculo(db: Session, as_id: int, servicio_vehiculo: ServicioVehiculoUpdate):
    _validar_referencias(
        db,
        servicio_vehiculo.vehiculo_id,
        servicio_vehiculo.servicio_id,
        servicio_vehiculo.operativo_id,
        servicio_vehiculo.cajero_id,
    )
    db_servicio_vehiculo = get_servicio_vehiculo_by_id(db, as_id)

    if db_servicio_vehiculo:
        db_servicio_vehiculo.vehiculo_id = servicio_vehiculo.vehiculo_id
        db_servicio_vehiculo.servicio_id = servicio_vehiculo.servicio_id
        db_servicio_vehiculo.operativo_id = servicio_vehiculo.operativo_id
        db_servicio_vehiculo.cajero_id = servicio_vehiculo.cajero_id
        db_servicio_vehiculo.as_fecha = servicio_vehiculo.as_fecha
        db_servicio_vehiculo.as_pagado = servicio_vehiculo.as_pagado
        db_servicio_vehiculo.as_monto = servicio_vehiculo.as_monto
        db_servicio_vehiculo.as_aprobado = servicio_vehiculo.as_aprobado
        db_servicio_vehiculo.as_hora = servicio_vehiculo.as_hora
        db_servicio_vehiculo.as_estado = servicio_vehiculo.as_estado
        db_servicio_vehiculo.as_estatus = servicio_vehiculo.as_estatus

        db.commit()
        db.refresh(db_servicio_vehiculo)
        return db_servicio_vehiculo

    return None


def get_servicio_vehiculo_by_id(db: Session, as_id: int):
    return db.query(Autoservicio).filter(
        Autoservicio.as_id == as_id
    ).first()
