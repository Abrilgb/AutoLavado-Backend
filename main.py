from fastapi import FastAPI
import config.db

# Importar los modelos
import models.modelUser
import models.modelsRols
import models.modelsVehiculos
import models.modelsServicios
import models.model_servicio_vehiculo

# Importar las rutas
from routes.routes_rol import rol
from routes.routes_vehiculo import vehiculo
from routes.routes_servicio import servicio
from routes.routes_servicio_vehiculo import servicio_vehiculo
from routes.routes_user import users


app = FastAPI(
    title="Sisema de control de autolavado ",
    description="Sstema de creación y almacenamiento de información de vehículos, servicios y asignaciones de servicios a vehículos en un autolavado.",
)

# Crear las tablas en la base de datos
models.modelsRols.Base.metadata.create_all(bind=config.db.engine)
models.modelUser.Base.metadata.create_all(bind=config.db.engine)
models.modelsVehiculos.Base.metadata.create_all(bind=config.db.engine)
models.modelsServicios.Base.metadata.create_all(bind=config.db.engine)
models.model_servicio_vehiculo.Base.metadata.create_all(bind=config.db.engine)

app.include_router(rol)
app.include_router(vehiculo)
app.include_router(servicio)
app.include_router(servicio_vehiculo)
app.include_router(users)