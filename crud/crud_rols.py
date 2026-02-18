from sqlalchemy.orm import Session
from datetime import datetime

from models.modelsRols import Rol
from schemas.schemaRols import RolCreate, RolUpdate

def get_roles(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Rol).offset(skip).limit(limit).all()

def get_rol_by_id(db: Session, rol_id: int):
    return db.query(Rol).filter(Rol.ro_id == rol_id).first()

def create_rol(db: Session, rol: RolCreate):
    db_rol = Rol(
        ro_descripcion=rol.ro_descripcion,
        ro_estatus=rol.ro_estatus,
        ro_fecha_registro=rol.ro_fecha_registro or datetime.now(),
        ro_fecha_modificacion=rol.ro_fecha_modificacion or datetime.now()
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def update_rol(db: Session, rol_id: int, rol: RolUpdate):
    db_rol = get_rol_by_id(db, rol_id)
    if not db_rol:
        return None

    db_rol.ro_descripcion = rol.ro_descripcion
    db_rol.ro_estatus = rol.ro_estatus
    db_rol.ro_fecha_modificacion = datetime.now()

    db.commit()
    db.refresh(db_rol)
    return db_rol

def delete_rol(db: Session, rol_id: int):
    db_rol = get_rol_by_id(db, rol_id)
    if not db_rol:
        return None

    db.delete(db_rol)
    db.commit()
    return db_rol
