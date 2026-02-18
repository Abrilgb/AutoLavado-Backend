from fastapi import FastAPI
import config.db

# Importar modelos (solo para que SQLAlchemy los registre)
import models.modelUser
import models.modelsRols
import models.modelsVehiculos
import models.modelsServicios
import models.model_servicio_vehiculo

# Importar routers (TODOS se llaman router)
from routes.routes_rol import router as rol_router
from routes.routes_vehiculo import router as vehiculo_router
from routes.routes_servicio import router as servicio_router
from routes.routes_servicio_vehiculo import router as servicio_vehiculo_router
from routes.routes_user import router as user_router


app = FastAPI(
    title="Sistema de control de autolavado",
    description="Sistema de creación y almacenamiento de información de vehículos, servicios y asignaciones.",
)

# Crear tablas (una sola vez al arrancar)
models.modelsRols.Base.metadata.create_all(bind=config.db.engine)
models.modelUser.Base.metadata.create_all(bind=config.db.engine)
models.modelsVehiculos.Base.metadata.create_all(bind=config.db.engine)
models.modelsServicios.Base.metadata.create_all(bind=config.db.engine)
models.model_servicio_vehiculo.Base.metadata.create_all(bind=config.db.engine)

# Registrar routers
app.include_router(rol_router)
app.include_router(vehiculo_router)
app.include_router(servicio_router)
app.include_router(servicio_vehiculo_router)
app.include_router(user_router)
