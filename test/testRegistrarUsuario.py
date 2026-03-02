import sys
from pathlib import Path

# Agregar la carpeta raíz al path de Python
sys.path.insert(0, str(Path(__file__).parent.parent))

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def obtener_token():
    """Hace login y devuelve un token JWT válido"""
    # Primero, registrar un usuario
    user_data = {
        "usuario": "testuser",
        "correo": "test@example.com",
        "password": "testpass123",
        "nombre": "Test",
        "papellido": "User",
        "sapellido": "Test",
        "rol_id": 1
    }
    
    # Registrar el usuario
    response = client.post("/auth/register", json=user_data)
    
    # Si ya existe, eso está bien
    if response.status_code != 200 and response.status_code != 400:
        raise Exception(f"Error al registrar: {response.text}")
    
    # Ahora hacer login
    response = client.post(
        "/auth/login",
        json={
            "usuario": "testuser",
            "password": "testpass123"
        }
    )
    assert response.status_code == 200, f"Login failed: {response.text}"
    return response.json()["access_token"]


def test_crear_usuario():
    token = obtener_token()
    print(f"\nToken obtenido: {token[:20]}...")

    payload = {
        "rol_id": 1,
        "nombre": "Test User",
        "papellido": "Apellido Test",
        "sapellido": "Apellido Test 2",
        "usuario": "testuser",
        "direccion": "Calle Test 123",
        "correo": "testuser@example.com",
        "telefono": "1234567890",
        "contrasena": "testpassword",
        "estatus": True
    }

    response = client.post(
        "/users/",
        json=payload,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )
    
    print(f"\nResponse status: {response.status_code}")
    print(f"Response body: {response.text}")

    assert response.status_code in (200, 201)

    data = response.json()
    assert data["correo"] == payload["correo"]
    assert data["Nombre"] == "Test User"
    assert "contrasena" not in data


def test_crear_usuario_invalido():
    token = obtener_token()

    payload_invalido = {
        "rol_id": "no-es-un-numero",
        "Nombre": ""
    }

    response = client.post(
        "/users/",
        json=payload_invalido,
        headers={
            "Authorization": f"Bearer {token}"
        }
    )

    assert response.status_code == 422