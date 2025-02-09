from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app.crud.user_crud import update_user, create_user, get_user, delete_user
from app.db.database import get_db
from app.models.user import User
from app.schemas.user import UserResponse, UpdateUser, UserCreate

router = APIRouter(
    prefix="/users",
    tags=["Users"]
)

# OBTENER TODOS LOS USUARIOS
@router.get("/", response_model=List[UserResponse])
def obtener_usuarios(db: Session = Depends(get_db)): # LA RUTA RECIBE LA BD
    data = db.query(User).all()
    return data

# CREAR UN NUEVO USUARIO
@router.post("/", summary="Crear un nuevo usuario", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        db_user = User(username=user.username, email=user.email, password=user.password)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(e)}")


# OBTENER UN USUARIO POR ID
@router.get("/{user_id}", response_model=UserResponse, summary="Obtener un usuario por ID")
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# ACTUALIZAR USUARIO
@router.put("/{user_id}", response_model=UserResponse, summary="Actualizar un usuario")
def update_user_info(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# ELIMINAR UN USUARIO
@router.delete("/{user_id}", summary="Eliminar un usuario", response_model=UserResponse)
def delete_user_info(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")

    try:
        deleted_user = delete_user(db, user_id)
        return deleted_user
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar el usuario: {str(e)}")
