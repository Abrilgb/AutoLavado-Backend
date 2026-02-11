''' Docstring for the routes_vehiculo module.'''
from fastapi import APIRouter

vehiculo = APIRouter()


@vehiculo.get("/vehiculos/", tags=["Vehículos"])
async def read_vehiculos():
    '''Función para obtener todos los vehículos'''
    return {"message": "Obteniendo vehículos"}

