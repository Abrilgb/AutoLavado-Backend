''' Docstring for the routes_servicio_vehiculo module. '''
from fastapi import APIRouter

router = APIRouter(
    prefix="/servicio-vehiculo",
    tags=["Servicio-Vehículo"]
)


@router.get("/")
async def read_servicio_vehiculo():
    return {"message": "Obteniendo servicios por vehículo"}


@router.post("/")
async def create_servicio_vehiculo():
    return {"message": "Asignando servicio a vehículo"}


@router.get("/{id}")
async def read_servicio_vehiculo_by_id(id: int):
    return {"message": f"Obteniendo asignación con ID {id}"}


@router.put("/{id}")
async def update_servicio_vehiculo(id: int):
    return {"message": f"Actualizando asignación con ID {id}"}


@router.delete("/{id}")
async def delete_servicio_vehiculo(id: int):
    return {"message": f"Eliminando asignación con ID {id}"}
