from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from typing import List
from app.crud.user_crud import update_user, get_user, delete_user
from app.db.database import get_db
from app.models.user import User
from app.routers.auth import get_current_user
from app.schemas.user import UserResponse, UpdateUser, UserCreate
from app.security.security import verify_password, hash_password, create_access_token

router = APIRouter(
    prefix="/users",
    tags=["Users"],
    # PROTEGER LAS RUTAS DE ESTE ROUTER
)

# OBTENER TODOS LOS USUARIOS
@router.get("/", response_model=List[UserResponse], dependencies=[Depends(get_current_user)])
def obtener_usuarios(db: Session = Depends(get_db)): # LA RUTA RECIBE LA BD
    data = db.query(User).all()
    return data

# SE PONE , dependencies=[] PARA NO TENER QEU AUTENTIFICARSE
@router.post("/login", summary="Iniciar sesion para obtener el token JWT", dependencies=[])
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(User).filter(User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password):  # VERIFICA LA CONTRASEÑA
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")
    access_token = create_access_token(data={"sub": user.id})
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/register", summary="Registrar un nuevo usuario")
def register(user_data: UserCreate, db: Session = Depends(get_db)):
    try:
        # VERIFICA SI EL NOMBRE DE USUARIO YA EXISTE
        existing_user = db.query(User).filter(User.username == user_data.username).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="El nombre de usuario ya esta en uso")

        # HASH DE LA CONTRASEÑA ANTES DE ALMANCENARLA
        hashed_password = hash_password(user_data.password)

        # CREAR NUEVO USUARIO
        new_user = User(username=user_data.username, email=user_data.email, password=hashed_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        # DEVOLVER MENSAJE DE EXISTO
        return {"message": "Usuario creado correctamente", "user_id": new_user.id}

    except Exception as e:
        # SI FALLA, SE HACE UN ROLLBACK
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al crear el usuario: {str(e)}")


# CREAR UN NUEVO USUARIO
@router.post("/", summary="Crear un nuevo usuario", response_model=UserResponse, dependencies=[Depends(get_current_user)])
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
@router.get("/{user_id}", response_model=UserResponse, summary="Obtener un usuario por ID", dependencies=[Depends(get_current_user)])
def get_user_by_id(user_id: int, db: Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user

# ACTUALIZAR USUARIO
@router.put("/{user_id}", response_model=UserResponse, summary="Actualizar un usuario", dependencies=[Depends(get_current_user)])
def update_user_info(user_id: int, user: UpdateUser, db: Session = Depends(get_db)):
    db_user = update_user(db, user_id, user)
    if db_user:
        return db_user
    raise HTTPException(status_code=404, detail="Usuario no encontrado")


# ELIMINAR UN USUARIO
@router.delete("/{user_id}", summary="Eliminar un usuario", response_model=UserResponse, dependencies=[Depends(get_current_user)])
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
