from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from config.db import SessionLocal
import crud.crud_vehiculo as crud
import schemas.schemaVehiculos as schemas

router = APIRouter(
    prefix="/vehiculos",
    tags=["Vehículos"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.Vehiculo])
def read_vehiculos(db: Session = Depends(get_db)):
    return crud.get_vehiculos(db)

@router.post("/", response_model=schemas.Vehiculo)
def create_vehiculo(vehiculo: schemas.VehiculoCreate, db: Session = Depends(get_db)):
    return crud.create_vehiculo(db, vehiculo)

@router.get("/{vehiculo_id}", response_model=schemas.Vehiculo)
def read_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = crud.get_vehiculo_by_id(db, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo

@router.put("/{vehiculo_id}", response_model=schemas.Vehiculo)
def update_vehiculo(
    vehiculo_id: int,
    vehiculo: schemas.VehiculoUpdate,
    db: Session = Depends(get_db)
):
    vehiculo_db = crud.update_vehiculo(db, vehiculo_id, vehiculo)
    if not vehiculo_db:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo_db

@router.delete("/{vehiculo_id}", response_model=schemas.Vehiculo)
def delete_vehiculo(vehiculo_id: int, db: Session = Depends(get_db)):
    vehiculo = crud.delete_vehiculo(db, vehiculo_id)
    if not vehiculo:
        raise HTTPException(status_code=404, detail="Vehículo no encontrado")
    return vehiculo