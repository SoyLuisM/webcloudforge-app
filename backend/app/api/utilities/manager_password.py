from datetime import datetime, timedelta, timezone
from typing import Any
# from fastapi.security import OAuth2PasswordBearer
import jwt
from passlib.context import CryptContext
from sqlmodel import Session
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.PREFIX_API}/login/access-token")

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_passwd:str)->bool:
    return pwd_context.verify(password,hashed_passwd)

def create_access_token(subject: str | Any) -> str:
    expires_delta= timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    print(f"el tiempo es de :{expires_delta}")
    expire = datetime.now(timezone.utc) + expires_delta
    to_encode = {"exp": expire, "sub": str(subject)}
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.PASSWD_ALGORITHM)
    return encoded_jwt

def decode_access_token():
    pass