''' Docstring for the crud_rols module.'''
import models.modelUser
import schemas.schemaUsuario
from sqlalchemy.orm import Session

#pylint: disable=too-few-public-methods
def get_user(db: Session, skip: int=0, limit: int=10):
    return db.query(models.modelUser.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: models.modelUser.User):
    db_user = models.modelUser.User(
        us_nombre=user.us_nombre,
        us_email=user.us_email,
        us_contrasena=user.us_contrasena,
        us_fecha_actualizacion=user.us_fecha_actualizacion,
        ro_id=user.ro_id
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.modelUser.User).filter(models.modelUser.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False

def update_user(db: Session, user_id: int, user: models.modelUser.User):
    db_user = db.query(models.modelUser.User).filter(models.modelUser.User.id == user_id).first()
    if db_user:
        db_user.us_nombre = user.us_nombre
        db_user.us_email = user.us_email
        db_user.us_contrasena = user.us_contrasena
        db_user.us_fecha_actualizacion = user.us_fecha_actualizacion
        db_user.ro_id = user.ro_id
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

def get_user_by_id(db: Session, user_id: int):
    return db.query(models.modelUser.User).filter(models.modelUser.User.id == user_id).first()

