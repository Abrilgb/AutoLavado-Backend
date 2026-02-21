from sqlalchemy.orm import Session
import models.modelsServicios
from schemas.schemaServicios import ServiciosCreate


def get_servicio(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.modelsServicios.Servicios)\
             .offset(skip).limit(limit).all()


def create_servicio(db: Session, servicio: ServiciosCreate):
    db_servicio = models.modelsServicios.Servicios(
        nombre=servicio.nombre,
        descripcion=servicio.descripcion,
        costo=servicio.costo,
        estatus=servicio.estatus,
        fecha_registro=servicio.fecha_registro,
        fecha_modificacion=servicio.fecha_modificacion
    )
    db.add(db_servicio)
    db.commit()
    db.refresh(db_servicio)
    return db_servicio


def delete_servicio(db: Session, servicio_id: int):
    db_servicio = db.query(models.modelsServicios.Servicios).filter(
        models.modelsServicios.Servicios.servicio_id == servicio_id
    ).first()

    if db_servicio:
        db.delete(db_servicio)
        db.commit()
        return True
    return False


def update_servicio(db: Session, servicio_id: int, servicio: ServiciosCreate):
    db_servicio = db.query(models.modelsServicios.Servicios).filter(
        models.modelsServicios.Servicios.servicio_id == servicio_id
    ).first()

    if db_servicio:
        db_servicio.nombre = servicio.nombre
        db_servicio.descripcion = servicio.descripcion
        db_servicio.costo = servicio.costo
        db_servicio.estatus = servicio.estatus
        db_servicio.fecha_registro = servicio.fecha_registro
        db_servicio.fecha_modificacion = servicio.fecha_modificacion

        db.commit()
        db.refresh(db_servicio)
        return db_servicio

    return None


def get_servicio_by_id(db: Session, servicio_id: int):
    return db.query(models.modelsServicios.Servicios).filter(
        models.modelsServicios.Servicios.servicio_id == servicio_id
    ).first()
