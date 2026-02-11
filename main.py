from fastapi import FastAPI
from routes.routes_rol import rol
from routes.routes_vehiculo import vehiculo
from routes.routes_servicio import servicio
from routes.routes_servicio_vehiculo import servicio_vehiculo

app = FastAPI(
    title="Sisema de control de autolavado ",
    description="Sstema de creación y almacenamiento de información de vehículos, servicios y asignaciones de servicios a vehículos en un autolavado.",
)

app.include_router(rol)
app.include_router(vehiculo)
app.include_router(servicio)
app.include_router(servicio_vehiculo)