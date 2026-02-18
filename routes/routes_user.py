''' Docstring for the routes_user module '''
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"]
)


@router.get("/")
async def read_users():
    return {"message": "Obteniendo usuarios"}


@router.post("/")
async def create_user():
    return {"message": "Creando usuario"}


@router.get("/{user_id}")
async def read_user(user_id: int):
    return {"message": f"Obteniendo usuario con ID {user_id}"}


@router.put("/{user_id}")
async def update_user(user_id: int):
    return {"message": f"Actualizando usuario con ID {user_id}"}


@router.delete("/{user_id}")
async def delete_user(user_id: int):
    return {"message": f"Eliminando usuario con ID {user_id}"}
