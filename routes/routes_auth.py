"""
Rutas de autenticación y login.
"""
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from config.db import SessionLocal
from config.auth import create_access_token
from config.security import verify_password
import crud.crud_user as crud
from schemas.schemaAuth import LoginRequest, TokenResponse
from schemas.schemaUsuario import UserCreate, User


router = APIRouter(
    prefix="/auth",
    tags=["Autenticación"]
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/login", response_model=TokenResponse)
async def login(login_data: LoginRequest, db: Session = Depends(get_db)):
    """
    Inicio de sesión con usuario y contraseña.
    Retorna un token JWT válido por 30 minutos.
    """
    # Buscar el usuario por nombre de usuario o email
    user = crud.get_user_by_username(db, login_data.usuario)
    
    if not user or not user.password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verificar la contraseña
    if not verify_password(login_data.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario o contraseña incorrectos",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Verificar que el usuario esté activo
    if not user.estatus:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Usuario desactivado"
        )
    
    # Crear token JWT
    access_token = create_access_token(data={"sub": user.id})
    
    return TokenResponse(
        access_token=access_token,
        user_id=user.id
    )


@router.post("/register", response_model=User)
async def register(user_data: UserCreate, db: Session = Depends(get_db)):
    """
    Registro de nuevo usuario sin autenticación.
    """
    # Verificar si el usuario ya existe
    user_exist = crud.get_user_by_username(db, user_data.usuario)
    if user_exist:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario ya existe"
        )
    
    # Verificar si el correo ya está registrado
    user_email = crud.get_user_by_email(db, user_data.correo)
    if user_email:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El correo ya está registrado"
        )
    
    # Asignar rol por defecto si no lo especifica
    if not user_data.rol_id:
        user_data.rol_id = 2  # Rol de usuario común (ajusta según tu lógica)
    
    # Crear el usuario
    new_user = crud.create_user(db, user_data)
    
    return new_user
