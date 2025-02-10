from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.routers.auth import get_current_user
from app.schemas.solve_time import SolveTimeCreate, SolveTimeResponse
from app.crud.solve_time_crud import create_solve_time, get_solve_time, get_solve_times, update_solve_time, \
    delete_solve_time

router = APIRouter(
    prefix="/solve-times",
    tags=["SolveTimes"],
    # PROTEGER LAS RUTAS DE ESTE ROUTER
    dependencies=[Depends(get_current_user)]
)

# OBTENER TODOS LOS TIEMPOS
@router.get("/", summary="Obtener todos los tiempos", response_model=list[SolveTimeResponse])
def get_all_solve_times(db: Session = Depends(get_db)):
    solve_times = get_solve_times(db)
    return solve_times

# OBTENER UN TIEMPO POR ID
@router.get("/{solve_time_id}", summary="Obtener un tiempo por ID", response_model=SolveTimeResponse)
def get_solve_time_by_id(solve_time_id: int, db: Session = Depends(get_db)):
    solve_time = get_solve_time(db, solve_time_id)
    if solve_time is None:
        raise HTTPException(status_code=404, detail="Tiempo no encontrado")
    return solve_time

# CREAR UN NUEVO TIEMPO
@router.post("/", summary="Crear un nuevo tiempo", response_model=SolveTimeResponse)
def create_new_solve_time(solve_time: SolveTimeCreate, db: Session = Depends(get_db)):
    new_solve_time = create_solve_time(db, solve_time)
    return new_solve_time

# ACTUALIZAR UN TIEMPO
@router.put("/{solve_time_id}", summary="Actualizar un tiempo", response_model=SolveTimeResponse)
def update_solve_time_info(solve_time_id: int, solve_time: SolveTimeCreate, db: Session = Depends(get_db)):
    updated_solve_time = update_solve_time(db, solve_time_id, solve_time)
    if updated_solve_time:
        return updated_solve_time
    raise HTTPException(status_code=404, detail="Tiempo no encontrado")


# ELIMINAR UN TIEMPO
@router.delete("/{solve_time_id}", summary="Eliminar un tiempo", response_model=SolveTimeResponse)
def delete_solve_time_info(solve_time_id: int, db: Session = Depends(get_db)):
    # SE OBTIENE EL TIEMPO POR SU ID
    solve_time = get_solve_time(db, solve_time_id)
    if solve_time is None:
        raise HTTPException(status_code=404, detail="Tiempo no encontrado")

    try:
        # SE ELIMINA EL TIEMPO Y lLO DEVUELVE
        deleted_solve_time = delete_solve_time(db, solve_time_id)
        return deleted_solve_time
    except Exception as e:
        # SI HAY UN ERROR AL ELIMINAR, SE LANZA UNA EXCEPCION
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al eliminar el tiempo: {str(e)}")