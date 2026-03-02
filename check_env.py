import os
from dotenv import load_dotenv
from pathlib import Path

# Cargar .env
env_path = Path(".env")
load_dotenv(dotenv_path=env_path)

secret = os.getenv("SECRET_KEY", "").strip()
print(f"SECRET_KEY cargado: {secret}")
print(f"Longitud: {len(secret)}")
