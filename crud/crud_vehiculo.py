''' Docstring for the crud_rols module.'''
import models.modelsVehiculos
from sqlalchemy.orm import Session

#pylint: disable=too-few-public-methods
def get_rol(db: Session, skip: int=0, limit: int=10):
    return db.query(models.modelsVehiculos.Vehiculos).offset(skip).limit(limit).all()