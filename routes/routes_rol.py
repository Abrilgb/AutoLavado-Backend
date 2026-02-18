''' Docstring for the routes_rol module '''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_rols as crud
import schemas.schemaRols as schemas
from config.db import SessionLocal

router = APIRouter(
    prefix="/roles",
    tags=["Roles"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Rol])
def read_roles(db: Session = Depends(get_db)):
    return crud.get_rol(db)


@router.post("/", response_model=schemas.Rol)
def create_role(
    rol: schemas.RolCreate,
    db: Session = Depends(get_db)
):
    return crud.create_rol(db, rol)


@router.get("/{rol_id}", response_model=schemas.Rol)
def read_role(rol_id: int, db: Session = Depends(get_db)):
    db_rol = crud.get_rol_by_id(db, rol_id)
    if not db_rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol


@router.put("/{rol_id}", response_model=schemas.Rol)
def update_role(
    rol_id: int,
    rol: schemas.RolUpdate,
    db: Session = Depends(get_db)
):
    db_rol = crud.update_rol(db, rol_id, rol)
    if not db_rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol


@router.delete("/{rol_id}", response_model=schemas.Rol)
def delete_role(rol_id: int, db: Session = Depends(get_db)):
    db_rol = crud.delete_rol(db, rol_id)
    if not db_rol:
        raise HTTPException(status_code=404, detail="Rol no encontrado")
    return db_rol
