"""
Esquemas para autenticación y tokens.
"""
from pydantic import BaseModel
from typing import Optional


class TokenResponse(BaseModel):
    """Respuesta con el token de acceso."""
    access_token: str
    token_type: str = "bearer"
    user_id: int


class TokenData(BaseModel):
    """Datos del token."""
    user_id: int


class LoginRequest(BaseModel):
    """Esquema para solicitud de login."""
    usuario: str
    password: str
    local_kw: Optional[str] = None
