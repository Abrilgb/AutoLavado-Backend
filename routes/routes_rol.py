''' Docstring for the routes_rol module.'''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import config.db, models.modelsRols, schemas.schemaRols, crud.crud_rols
from typing import List

rol = APIRouter()

''' para crear la tabla en la base de datos'''
models.modelsRols.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    '''Función para obtener la sesión de la base de datos'''
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@rol.get("/roles/", response_model=list[schemas.schemaRols.Rol],tags=["Roles"])
async def read_roles(skip: int=0, limit: int=10, db: Session=Depends(get_db)):
    '''Función para obtener todos los roles'''
    roles = crud.crud_rols.get_rol(db, skip=skip, limit=limit)
    return roles

