''' Docstring for the routes_servicio module.'''
from fastapi import APIRouter

servicio = APIRouter()


@servicio.get("/servicios/", tags=["Servicios"])
async def read_servicios():
    '''Función para obtener todos los servicios'''
    return {"message": "Obteniendo servicios"}

