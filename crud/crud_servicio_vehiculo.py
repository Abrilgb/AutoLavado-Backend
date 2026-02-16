''' Docstring for the crud_rols module.'''
import models.model_servicio_vehiculo
import schemas.schema_servicio_vehiculo
from sqlalchemy.orm import Session

#pylint: disable=too-few-public-methods
def get_rol(db: Session, skip: int=0, limit: int=10):
    return db.query(models.model_servicio_vehiculo.servicio_vehiculo).offset(skip).limit(limit).all()