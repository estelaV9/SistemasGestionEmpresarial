from sqlalchemy.orm import Session
from app.models.user import User
from app.schemas.user import UpdateUser, UserCreate

# CREAR UN NUEVO USUARIO
def create_user(db: Session, user: UserCreate):
    db_user = User(username=user.username, email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# OBTENER UN USUARIO POR ID
def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()

# ACTUALIZAR UN USUARIO
def update_user(db: Session, user_id: int, user: UpdateUser):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        if user.username:
            db_user.username = user.username
        if user.password:
            db_user.password = user.password
        if user.email:
            db_user.email = user.email
        db.commit()
        db.refresh(db_user)
        return db_user
    return None

# ELIMINAR UN USUARIO
def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        return None
    db.delete(user)
    db.commit()
    return user
