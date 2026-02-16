''' Docstring for the crud_rols module.'''
import models.modelsRols
import schemas.schemaRols
from sqlalchemy.orm import Session

#pylint: disable=too-few-public-methods
def get_rol(db: Session, skip: int=0, limit: int=10):
    return db.query(models.modelsRols.Rol).offset(skip).limit(limit).all()

def create_rol(db: Session, rol: models.modelsRols.Rol):
    db_rol = models.modelsRols.Rol(
        ro_nombre=rol.ro_nombre,
        ro_descripcion=rol.ro_descripcion,
        ro_fecha_actualizacion=rol.ro_fecha_actualizacion
    )
    db.add(db_rol)
    db.commit()
    db.refresh(db_rol)
    return db_rol

def delete_rol(db: Session, rol_id: int):
    db_rol = db.query(models.modelsRols.Rol).filter(models.modelsRols.Rol.ro_id == rol_id).first()
    if db_rol:
        db.delete(db_rol)
        db.commit()
        return True
    return False

def update_rol(db: Session, rol_id: int, rol: models.modelsRols.Rol):
    db_rol = db.query(models.modelsRols.Rol).filter(models.modelsRols.Rol.ro_id == rol_id).first()
    if db_rol:
        db_rol.ro_nombre = rol.ro_nombre
        db_rol.ro_descripcion = rol.ro_descripcion
        db_rol.ro_fecha_actualizacion = rol.ro_fecha_actualizacion
        db.commit()
        db.refresh(db_rol)
        return db_rol
    return None

def get_rol_by_id(db: Session, rol_id: int):
    return db.query(models.modelsRols.Rol).filter(models.modelsRols.Rol.ro_id == rol_id).first()