# app/core/db_connection.py

from fastapi import Depends, HTTPException, status
from collections.abc import Generator
from typing import Annotated
from sqlmodel import create_engine, Session
from app.core.config import settings
from sqlalchemy.exc import OperationalError, DBAPIError

from app.repositories.AccountRepository import AccountRepository
from app.schemas.account_schemas import CreateAccount

from app.models.UsersAccounts import UsersAccounts
from app.models.Users import Users
# from app.models.Services import UsersCatTecnoLink


# Crear el engine con SQLModel
engine = create_engine(str(settings.DATABASE_URL), echo=True)

# Función para obtener una sesión
def get_db() -> Generator[Session, None, None]:
    try:
        with Session(engine) as session:
            yield session
    except (OperationalError, DBAPIError) as e:
        # Si la conexión falla, lanza una excepción HTTPException
        print(f"Error al conectar con la base de datos: {e}")
        
        # Puedes personalizar el mensaje de error o el código de estado
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="No se pudo conectar a la base de datos. Intente más tarde."
        )



SessionDep = Annotated[Session, Depends(get_db)]


def create_initial_super_user():
    """Verifica si existe un admin y lo crea si no existe."""
    try:
       
        with Session(engine) as session:
            repo = AccountRepository(session)

           
            admin_data = CreateAccount(
                email=settings.ADMIN_EMAIL,
                password=settings.ADMIN_PASSWORD,
                
            )

            # Llama al método que verifica y crea el superusuario
            success = repo.create_super_user(admin_data)

            if success:
                print("Superusuario creado exitosamente.")
            else:
                print("Superusuario ya existe, no se realizaron cambios.")
                
    except Exception as e:
        # Captura cualquier error de conexión o base de datos que pudiera ocurrir
        print(f" Error al intentar inicializar el Superusuario: {e}")