from sqlalchemy.orm import Session
from app.models.solve_time import SolveTime
from app.schemas.solve_time import SolveTimeCreate

# CREAR UN NUEVO TIEMPO
def create_solve_time(db: Session, solve_time: SolveTimeCreate):
    db_solve_time = SolveTime(time_seconds=solve_time.time_seconds,
                               date=solve_time.date,
                               cube_id=solve_time.cube_id,
                               user_id=solve_time.user_id)
    db.add(db_solve_time)
    db.commit()
    db.refresh(db_solve_time)
    return db_solve_time

# OBTENER UN TIEMPO POR ID
def get_solve_time(db: Session, solve_time_id: int):
    return db.query(SolveTime).filter(SolveTime.id == solve_time_id).first()

# OBTENER TODOS LOS TIEMPOS
def get_solve_times(db: Session):
    return db.query(SolveTime).all()

# ACTUALIZAR UN TIEMPO
def update_solve_time(db: Session, solve_time_id: int, solve_time: SolveTimeCreate):
    db_solve_time = db.query(SolveTime).filter(SolveTime.id == solve_time_id).first()
    if db_solve_time:
        db_solve_time.time_seconds = solve_time.time_seconds
        db_solve_time.date = solve_time.date
        db_solve_time.cube_id = solve_time.cube_id
        db_solve_time.user_id = solve_time.user_id
        db.commit()
        db.refresh(db_solve_time)
        return db_solve_time
    return None

# ELIMINAR UN TIEMPO
def delete_solve_time(db: Session, solve_time_id: int):
    solve_time = db.query(SolveTime).filter(SolveTime.id == solve_time_id).first()
    if not solve_time:
        return None
    db.delete(solve_time)
    db.commit()
    return solve_time
