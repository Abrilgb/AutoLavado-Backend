from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

import crud.crud_servicio_vehiculo as crud
import schemas.schema_servicio_vehiculo as schemas
from config.db import SessionLocal

router = APIRouter(
    prefix="/servicio-vehiculo",
    tags=["Servicio-Vehículo"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/", response_model=list[schemas.ServicioVehiculo])
async def read_servicio_vehiculo(db: Session = Depends(get_db)):
    return crud.get_servicio_vehiculo(db)


@router.post("/", response_model=schemas.ServicioVehiculo)
async def create_servicio_vehiculo(
    servicio_vehiculo: schemas.ServicioVehiculoCreate,
    db: Session = Depends(get_db)
):
    try:
        return crud.create_servicio_vehiculo(db, servicio_vehiculo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except IntegrityError:
        raise HTTPException(
            status_code=400,
            detail="Datos de referencia inválidos: verifique que el vehículo, servicio, operativo y cajero existan."
        )


@router.get("/{as_id}", response_model=schemas.ServicioVehiculo)
async def read_servicio_vehiculo_by_id(
    as_id: int,
    db: Session = Depends(get_db)
):
    servicio = crud.get_servicio_vehiculo_by_id(db, as_id)
    if not servicio:
        raise HTTPException(status_code=404, detail="ServicioVehiculo no encontrado")
    return servicio


@router.put("/{as_id}", response_model=schemas.ServicioVehiculo)
async def update_servicio_vehiculo(
    as_id: int,
    servicio_vehiculo: schemas.ServicioVehiculoUpdate,
    db: Session = Depends(get_db)
):
    try:
        updated = crud.update_servicio_vehiculo(db, as_id, servicio_vehiculo)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    if not updated:
        raise HTTPException(status_code=404, detail="ServicioVehiculo no encontrado")
    return updated


@router.delete("/{as_id}")
async def delete_servicio_vehiculo(
    as_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_servicio_vehiculo(db, as_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="ServicioVehiculo no encontrado")
    return {"detail": "ServicioVehiculo eliminado correctamente"}
