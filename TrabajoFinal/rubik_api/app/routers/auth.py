from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from app.db.database import get_db
from app.models.user import User
from app.security.security import verify_password, create_access_token, verify_token

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

# CONFIGURACION DE OAUTH2 PARA GESTIONAR TOKENS JWT
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")  # RUTA PARA EL LOGIN


# FUNCION PARA OBTENER EL USUARIO AUTENTICADO A PARTIR DEL TOKEN
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    token_data = verify_token(token)
    # SI LOS DATOS DEL TOKEN NO SON VALIDOS O ESTAN VACIOS, SALTA UNA EXCEPCION
    if token_data is None:
        raise HTTPException(status_code=401, detail="Token invalido o expirado")

    # SE BUSCA EL USUARIO EN LA BD UTILIZANDO EL ID DEL TOKEN
    user = db.query(User).filter(User.id == token_data.get("sub")).first()
    # SI NO SE ENCUENTRA EL USUARIO, SE LANZA UNA EXCEPCION
    if user is None:
        raise HTTPException(status_code=404, detail="Usuario no encontrado")
    return user # RETORNA EL USUARIO SITODO HA SALIDO BIEN


# INICIAR SESION Y OBTENER EL TOKEN JWT
@router.post("/login", summary="Iniciar sesion para obtener el token JWT")
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # BUSCAR EL USUARIO POR NOMBRE DE USUARIO
    user = db.query(User).filter(User.username == form_data.username).first()

    # SI NO SE ENCUENTA, SE LANZA UNA EXCEPCION
    if not user:
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    # VERIFICAR LA CONTRASEÑA CON LA ALMACENADA EN LA BD
    # (la función 'verify_password' sirve para comparar la contraseña)
    if not verify_password(form_data.password, user.password):
        raise HTTPException(status_code=400, detail="Credenciales incorrectas")

    # SI LAS CREDENCIALES SSON VALIDAS, SE CREA EL TOKEN JWT PARA AUTENTICAR AL USUARIO
    # CON EL ID DEL USUARIO  COMO 'sub' (SUBJECT)
    access_token = create_access_token(data={"sub": user.id})

    # SE RETORNA EL TOKEN JWT GENERADO JUNTO CON EL TIPO DE TOKEN
    return {"access_token": access_token, "token_type": "bearer"}


# RUTA PROTEGIDA (SOLO ACCESIBLE CON TOKEN VALIDO)
@router.get("/protected", summary="Ruta protegida solo para usuarios autenticados")
def protected_route(current_user: User = Depends(get_current_user)):
    return {"message": f"¡Hola {current_user.username}!."}