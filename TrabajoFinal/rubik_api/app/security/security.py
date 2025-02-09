from datetime import datetime, timedelta
from jose import JWTError, jwt
from passlib.context import CryptContext

SECRET_KEY = "hola"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # TIEMPO DE EXPIRACION DEL TOKEN (1 HORA)

# CONTEXTO PARA HASHEAR Y VERIFICAR CONTRASEÑAS CON BCRYPT
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


# HASHEAR LA CONTRASEÑA ANTES DE GUARDARLA EN LA BD
def hash_password(password: str) -> str:
    return pwd_context.hash(password)


# VERIFICAR SI LA CONTRASEÑA PROPORCIONADA ES CORRECTA
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)


# CREAR EL TOKEN JWT
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})  # AÑADIMOS FECHA DE EXPIRACIoN AL TOKEN
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# DECODIFICAR EL TOKEN JWT Y VERIFICAR SU VALIDEZ
def verify_token(token: str):
    try:
        token_data = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return token_data  # SI ES VALIDO, DEVUELVE EL CONTENIDO DEL TOKEN
    except JWTError:
        return None
