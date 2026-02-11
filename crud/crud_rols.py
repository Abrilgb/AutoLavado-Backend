''' Docstring for the crud_rols module.'''
import models.modelsRols
import schemas.schemaRols
from sqlalchemy.orm import Session

#pylint: disable=too-few-public-methods
def get_rol(db: Session, skip: int=0, limit: int=10):
    return db.query(models.modelsRols.Rol).offset(skip).limit(limit).all()