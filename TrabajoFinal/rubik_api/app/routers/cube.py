from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schemas.cube import CubeCreate, CubeResponse
from app.crud.cube_crud import create_cube, get_cube, get_cubes, update_cube, delete_cube
from app.routers.auth import get_current_user


router = APIRouter(
    prefix="/cubes",
    tags=["Cubes"],
    # PROTEGER LAS RUTAS DE ESTE ROUTER
    dependencies=[Depends(get_current_user)]
)

# OBTENER TODOS LOS CUBOS
@router.get("/", summary="Obtener todos los cubos", response_model=list[CubeResponse])
def get_all_cubes(db: Session = Depends(get_db)):
    cubes = get_cubes(db)
    return cubes


# OBTENER UN CUBO POR ID
@router.get("/{cube_id}", summary="Obtener un cubo por ID", response_model=CubeResponse)
def get_cube_by_id(cube_id: int, db: Session = Depends(get_db)):
    cube = get_cube(db, cube_id)
    if cube is None:
        raise HTTPException(status_code=404, detail="Cubo no encontrado")
    return cube


# CREAR UN NUEVO CUBO
@router.post("/", summary="Crear un nuevo cubo", response_model=CubeResponse)
def create_new_cube(cube: CubeCreate, db: Session = Depends(get_db)):
    new_cube = create_cube(db, cube)
    return new_cube


# ACTUALIZAR UN CUBO
@router.put("/{cube_id}", summary="Actualizar un cubo", response_model=CubeResponse)
def update_cube_info(cube_id: int, cube: CubeCreate, db: Session = Depends(get_db)):
    updated_cube = update_cube(db, cube_id, cube)
    if updated_cube:
        return updated_cube
    raise HTTPException(status_code=404, detail="Cubo no encontrado")


# ELIMINAR UN CUBO
@router.delete("/{cube_id}", summary="Eliminar un cubo", response_model=CubeResponse)
def delete_cube_info(cube_id: int, db: Session = Depends(get_db)):
    # SE OBTIENE EL CUBO POR SU ID
    cube = get_cube(db, cube_id)
    if cube is None:
        raise HTTPException(status_code=404, detail="Cubo no encontrado")

    try:
        # SE ELIMINA EL CUBO Y SE DEVUELVE EL CUBO ELIMINADO
        deleted_cube = delete_cube(db, cube_id)
        return deleted_cube
    except Exception as e:
        # SI HAY UN ERROR AL ELIMINAR, SE LANZA UNA EXCEPCION
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar el cubo: {str(e)}")
