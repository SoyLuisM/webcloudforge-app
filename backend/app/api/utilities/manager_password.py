from datetime import datetime, timedelta, timezone
from typing import Any
# from fastapi.security import OAuth2PasswordBearer
from fastapi import HTTPException,status
import jwt
from passlib.context import CryptContext
from pydantic import ValidationError
from sqlmodel import Session
from app.core.config import settings
from app.schemas.aurh_schemas import token

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# 

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_passwd:str)->bool:
    return pwd_context.verify(password,hashed_passwd)

def create_access_token(subject: str | Any) -> str:
    expires_delta= timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.PASSWD_ALGORITHM)
    return encoded_jwt



def decode_access_token(token:str)->str:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.PASSWD_ALGORITHM]
        )
        print(payload)
        token_id: str = payload.get('sub')
    except (jwt.InvalidTokenError, ValidationError):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return token_id

