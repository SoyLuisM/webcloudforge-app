import uuid
from pydantic import EmailStr
from sqlmodel import Field, SQLModel


class CreateAccount(SQLModel):
    """Define los datos necesarios minimos para crear una cuenta"""
    email: EmailStr = Field(default=None, max_length=255, unique=True)
    password: str = Field(min_length=8, max_length=40)

class PublicAccount(SQLModel):
    """estos son los datos que se devuelven como respuesta a la consulta de una cuenta"""
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(default=None, max_length=255, unique=True)

class AccountByEmail(SQLModel):
    email: EmailStr = Field(default=None, max_length=255, unique=True)