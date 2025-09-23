from passlib.context import CryptContext
from app.core.config import settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password:str)->str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed_passwd:str)->str:
    return pwd_context.verify(password,hashed_passwd)
