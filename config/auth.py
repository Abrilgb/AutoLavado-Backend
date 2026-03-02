"""
Configuración de autenticación JWT.
"""
import os
from datetime import datetime, timedelta
from typing import Optional
from pathlib import Path

from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status, Query
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.orm import Session
from dotenv import load_dotenv

# Cargar .env desde la ruta correcta
env_path = Path(__file__).parent.parent / ".env"
load_dotenv(dotenv_path=env_path)

from config.db import SessionLocal
import crud.crud_user as crud

SECRET_KEY = os.getenv("SECRET_KEY", "").strip()
if not SECRET_KEY:
    raise ValueError("SECRET_KEY no está configurado en el archivo .env")

ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

security = HTTPBearer(auto_error=False)  # No lanzar error automático


def create_access_token(data: dict, expires_delta: Optional[timedelta] = None) -> str:
    to_encode = data.copy()
    expire = datetime.utcnow() + (
        expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)


def verify_token(
    local_kw: Optional[str] = Query(None),
    auth_header: Optional[HTTPAuthorizationCredentials] = Depends(security)
) -> dict:
    """
    Verifica el token JWT desde dos fuentes:
    1. Header Authorization: Bearer <token>
    2. Parámetro de query: ?local_kw=<token>
    """
    token = None
    
    # Intentar obtener el token del parámetro de query
    if local_kw:
        token = local_kw
    # Si no está en query, intentar desde el header
    elif auth_header:
        token = auth_header.credentials
    
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token no proporcionado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(status_code=401, detail="Token inválido")
        return payload
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(
    token_data: dict = Depends(verify_token),
    db: Session = Depends(SessionLocal)
):
    user_id = token_data.get("sub")

    user = crud.get_user_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=401, detail="Usuario no encontrado")

    if not user.estatus:
        raise HTTPException(status_code=403, detail="Usuario desactivado")

    return user


def require_role(allowed_roles: list[str]):
    """
    Verifica que el usuario tenga uno de los roles permitidos.
    """
    def check_role(current_user=Depends(get_current_user)):
        if not hasattr(current_user, "rol"):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="El usuario no tiene rol asignado"
            )

        if current_user.rol.ro_descripcion not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail=f"Se requiere uno de los siguientes roles: {', '.join(allowed_roles)}"
            )

        return current_user

    return check_role