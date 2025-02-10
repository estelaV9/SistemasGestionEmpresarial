import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from app.db.database import Base, get_db
from app.main import app
from app.models.user import User
from app.security.security import hash_password

# BASE DE DATOS EN MEMORIA PARA LAS PRUEBAS
SQLALCHEMY_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# FIXTURE PARA LA BASE DE DATOS (se crea una sola vez para la sesión de test)
@pytest.fixture(scope="session")
def db():
    # CREAR LA BASE DE DATOS DE PRUEBA
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()

# FIXTURE PARA EL CLIENTE DE PRUEBAS
@pytest.fixture(scope="module")
def client(db):
    def override_get_db():
        try:
            yield db
        finally:
            # SE CIERRA LA SESIONE
            pass
    app.dependency_overrides[get_db] = override_get_db
    client = TestClient(app)
    yield client

# FUNCIIN AUXILIAR PARA CREAR UN USUARIO DE PRUEBA
def create_test_user(db):
    test_user = User(
        username="testuser",
        email="test@example.com",
        password=hash_password("testpassword")
    )
    db.add(test_user)
    db.commit()
    db.refresh(test_user)
    return test_user

# PRUEBA: LOGIN EXITOSO
def test_login_success(client, db):
    # SE CREA UN USUARIO DE PRUEBA
    create_test_user(db)
    # DATOS DEL LOGIN
    login_data = {"username": "testuser", "password": "testpassword"}
    response = client.post("/auth/login", data=login_data)
    # SE ESPERA UN CODIGO DE 200 Y QUE INCLUYA EL access_token NE LA REPSUNTA
    assert "access_token" in response.json()
