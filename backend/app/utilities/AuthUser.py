from datetime import datetime, timedelta, timezone
import jwt
from jwt.exceptions import PyJWTError

class AuthUser():
    
    secret_key: str
    algorithm: str
    encode:str

    def __init__(self,secret_key:str, algorithm: str,encode: str):
        self.secret_key = secret_key
        self.algorithm = algorithm
        self.encode = encode

    def create_acces_token(self, data: dict, expires_delta: timedelta = timedelta(minutes=15))->str:
        to_encode = data.copy
        expire = datetime.now(timezone.utc) + (expires_delta) 
        to_encode.update({"exp": expire})
        return jwt.encode(to_encode,self.secret_key, algorithm= self.algorithm)
    
    def decode_token(self,token: str)->str:
        try: 
            payload = jwt.decode(token, self.secret_key,algorithms=self.algorithm)
            return payload
        except PyJWTError as e:
            raise Exception(f'Tokenn invalido: {e}')
        
    def get_password(self, password: str)->str:
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode(self.encode,salt))
        return hashed
    
    def verify_password(self, password: str,hash:str)->bool:
        result = bcrypt.checkpw(password=password.encode(self.encode),hashed_password=hash)
        return result