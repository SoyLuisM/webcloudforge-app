import uuid
from sqlmodel import Field,SQLModel, Relationship


class Users(SQLModel, table=True):
    id: uuid.UUID = Field(default_factory=uuid.uuid4, primary_key=True)
    nombre: str = Field(max_length=255, min_length=1)
    a_paterno: str = Field(max_length=255, min_length=1)
    a_materno: str = Field(max_length=255, min_length=1)
    account_id: uuid.UUID = Field(foreign_key='usersaccounts.id', unique=True) 
    usersaccount: "UsersAccounts" = Relationship(back_populates="user") 


