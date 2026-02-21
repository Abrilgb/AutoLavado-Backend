''' Docstring for the routes_user module '''
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud.crud_user as crud
import schemas.schemaUsuario as schemas
from config.db import SessionLocal

router = APIRouter(
    prefix="/users",
    tags=["Usuarios"]
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/", response_model=list[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = crud.get_user(db)
    return users


@router.post("/", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db, user)


@router.get("/{user_id}", response_model=schemas.User)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    user = crud.get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user


@router.put("/{user_id}", response_model=schemas.User)
async def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    updated = crud.update_user(db, user_id, user)
    if updated is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return updated


@router.delete("/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted = crud.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return {"message": "Usuario eliminado correctamente"}
