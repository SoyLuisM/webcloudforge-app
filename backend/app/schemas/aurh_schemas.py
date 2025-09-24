from sqlmodel import SQLModel


class token(SQLModel):
    access_token: str
    token_type: str = "bearer"