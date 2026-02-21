"""
Utilidades para hashear y verificar contraseñas.
Usa bcrypt directamente (evita incompatibilidades con passlib).
"""
import hashlib

import bcrypt

# bcrypt tiene límite de 72 bytes; pre-hasheamos con SHA256 para soportar contraseñas largas
BCRYPT_MAX_LENGTH = 72


def hash_password(password: str) -> str:
    """Convierte una contraseña en texto plano a hash bcrypt."""
    pwd_bytes = password.encode("utf-8")
    if len(pwd_bytes) > BCRYPT_MAX_LENGTH:
        pwd_bytes = hashlib.sha256(pwd_bytes).digest()
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(pwd_bytes, salt)
    return hashed.decode("utf-8")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """Verifica que la contraseña en texto plano coincida con el hash."""
    pwd_bytes = plain_password.encode("utf-8")
    if len(pwd_bytes) > BCRYPT_MAX_LENGTH:
        pwd_bytes = hashlib.sha256(pwd_bytes).digest()
    hashed_bytes = hashed_password.encode("utf-8")
    return bcrypt.checkpw(pwd_bytes, hashed_bytes)
