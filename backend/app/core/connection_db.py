# app/core/db_connection.py

from fastapi import Depends
from collections.abc import Generator
from typing import Annotated
from sqlmodel import create_engine, Session
from app.core.config import settings

# Crear el engine con SQLModel
engine = create_engine(str(settings.DATABASE_URL), echo=True)

# Función para obtener una sesión
def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]