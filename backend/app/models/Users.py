from typing import List
import uuid
from sqlmodel import Field,SQLModel, Relationship

from app.models.Services import UsersCatTecnoLink


class Users(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    nombre: str = Field(max_length=255, min_length=1)
    a_paterno: str = Field(max_length=255, min_length=1)
    a_materno: str = Field(max_length=255, min_length=1)
    account_id: uuid.UUID = Field(foreign_key='usersaccounts.id', unique=True) 
    profesion: str = Field(max_length=255, min_length=1)
    usersaccount: "UsersAccounts" = Relationship(back_populates="user") 

    # Relaciones 1:N (Un Users tiene muchos de estos)
    servicios: List["Servicios"] = Relationship(back_populates="user")
    proyectos: List["Proyectos"] = Relationship(back_populates="user")
    contactos: List["Contactos"] = Relationship(back_populates="user")
    experiencia: List["Experiencia"] = Relationship(back_populates="user")
    educacion: List["Educacion"] = Relationship(back_populates="user")

    # Relación M:N con CatTecnologia
    tecnologias: List["CatTecnologia"] = Relationship(
        back_populates="usuarios", link_model=UsersCatTecnoLink
    )

