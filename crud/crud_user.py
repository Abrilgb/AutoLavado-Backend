''' Docstring for the crud_user module.'''
from datetime import datetime

from models.modelUser import User
from schemas.schemaUsuario import UserCreate, UserUpdate
from sqlalchemy.orm import Session


def get_user(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        nombre=user.nombre,
        papellido=user.papellido,
        sapellido=user.sapellido,
        usuario=user.usuario,
        direccion=user.direccion,
        correo=user.correo,
        telefono=user.telefono,
        password=user.password,
        estatus=user.estatus,
        rol_id=user.rol_id,
        fecha_registro=user.fecha_registro or datetime.utcnow(),
        fecha_modificacion=user.fecha_modificacion or datetime.utcnow(),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return True
    return False


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.nombre = user.nombre
        db_user.papellido = user.papellido
        db_user.sapellido = user.sapellido
        db_user.usuario = user.usuario
        db_user.direccion = user.direccion
        db_user.correo = user.correo
        db_user.telefono = user.telefono
        db_user.password = user.password
        db_user.estatus = user.estatus
        db_user.rol_id = user.rol_id
        db_user.fecha_modificacion = user.fecha_modificacion or datetime.utcnow()
        if user.fecha_registro is not None:
            db_user.fecha_registro = user.fecha_registro
        db.commit()
        db.refresh(db_user)
        return db_user
    return None


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

