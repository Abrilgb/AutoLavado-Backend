''' Docstring for the routes_servicio module. '''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_servicios as crud
import schemas.schemaServicios as schemas
from config.db import SessionLocal

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"]
)
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.Servicio])
def read_servicios(db: Session = Depends(get_db)):
    return crud.get_servicio(db)


@router.post("/", response_model=schemas.Servicio)
def create_servicio(servicio: schemas.ServiciosCreate, db: Session = Depends(get_db)):
    return crud.create_servicio(db, servicio)



@router.get("/{id}", response_model=schemas.Servicio)
def read_servicio(id: int, db: Session = Depends(get_db)):
    servicio = crud.get_servicio_by_id(db, id)
    if not servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return servicio


@router.put("/{id}", response_model=schemas.Servicio)
def update_servicio(id: int, servicio: schemas.ServiciosUpdate, db: Session = Depends(get_db)):
    updated_servicio = crud.update_servicio(db, id, servicio)
    if not updated_servicio:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return updated_servicio


@router.delete("/{id}")
def delete_servicio(id: int, db: Session = Depends(get_db)):
    success = crud.delete_servicio(db, id)
    if not success:
        raise HTTPException(status_code=404, detail="Servicio no encontrado")
    return {"detail": "Servicio eliminado exitosamente"}