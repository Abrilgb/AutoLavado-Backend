''' Docstring for the routes_servicio module. '''
from fastapi import APIRouter

router = APIRouter(
    prefix="/servicios",
    tags=["Servicios"]
)


@router.get("/")
async def read_servicios():
    '''Función para obtener todos los servicios'''
    return {"message": "Obteniendo servicios"}


@router.post("/")
async def create_servicio():
    '''Función para crear un nuevo servicio'''
    return {"message": "Creando servicio"}


@router.get("/{id}")
async def read_servicio(id: int):
    '''Función para obtener un servicio por su ID'''
    return {"message": f"Obteniendo servicio con ID {id}"}


@router.put("/{id}")
async def update_servicio(id: int):
    '''Función para actualizar un servicio por su ID'''
    return {"message": f"Actualizando servicio con ID {id}"}


@router.delete("/{id}")
async def delete_servicio(id: int):
    '''Función para eliminar un servicio por su ID'''
    return {"message": f"Eliminando servicio con ID {id}"}
