''' Docstring for the routes_servicio_vehiculo module.'''
from fastapi import APIRouter

servicio_vehiculo = APIRouter()


@servicio_vehiculo.get("/servicios-vehiculos/", tags=["Servicios por Vehículo"])
async def read_servicios_vehiculos():
    '''Función para obtener asignaciones de servicios a vehículos'''
    return {"message": "Obteniendo servicios de vehículos"}

