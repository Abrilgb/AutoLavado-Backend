''' Docstring for the routes_vehiculo module.'''
from fastapi import APIRouter

users = APIRouter()


@users.get("/user/", tags=["Users"])
async def read_vehiculos():
    '''Función para obtener todos los usuarios'''
    return {"message": "Obteniendo usuarios"}

