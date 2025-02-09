from sqlalchemy.orm import Session
from app.models.cube import Cube
from app.schemas.cube import CubeCreate

# CREAR UN NUEVO CUBO
def create_cube(db: Session, cube: CubeCreate):
    db_cube = Cube(type=cube.type, owner_id=cube.owner_id)
    db.add(db_cube)
    db.commit()
    db.refresh(db_cube)
    return db_cube

# OBTENER UN CUBO POR ID
def get_cube(db: Session, cube_id: int):
    return db.query(Cube).filter(Cube.id == cube_id).first()

# OBTENER TODOS LOS CUBOS
def get_cubes(db: Session):
    return db.query(Cube).all()

# ACTUALIZAR UN CUBO
def update_cube(db: Session, cube_id: int, cube: CubeCreate):
    db_cube = db.query(Cube).filter(Cube.id == cube_id).first()
    if db_cube:
        db_cube.type = cube.type
        db_cube.owner_id = cube.owner_id
        db.commit()
        db.refresh(db_cube)
        return db_cube
    return None


# ELIMINAR UN CUBO
def delete_cube(db: Session, cube_id: int):
    cube = db.query(Cube).filter(Cube.id == cube_id).first()
    if not cube:
        return None
    db.delete(cube)
    db.commit()
    return cube

