from typing import Optional
import uuid
from pydantic import EmailStr
from sqlmodel import Field, Relationship, SQLModel


class UsersAccounts(SQLModel, table= True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    email: EmailStr = Field(default=None, max_length=255, unique=True)
    hashed_password: str
    is_active: bool = Field(default=False)
    is_admin: bool = Field(default=False)
    user: Optional["Users"] = Relationship(back_populates="usersaccount")