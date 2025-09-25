from typing import Annotated
import uuid

from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer

from app.api.utilities.manager_password import decode_access_token
from app.core.config import settings
from app.core.connection_db import SessionDep
from app.repositories.AccountRepository import AccountRepository

reusable_oauth2 = OAuth2PasswordBearer(tokenUrl=f"{settings.PREFIX_API}/login/access-token")

def get_current_user_id(token: Annotated[str, Depends(reusable_oauth2)]) -> uuid.UUID:
    """
    Dependencia que valida el token y devuelve el ID del usuario.
    
    Lanza HTTPException 401 si:
    1. El token no está presente (Dependencia OAuth2PasswordBearer).
    2. El token es inválido (firma, expiración).
    """
    
    user_id_str = decode_access_token(token)

    # 1. Verificación de validez y expiración
    if user_id_str is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido o expirado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    try:
        # Convierte el string del token a UUID (o el tipo de tu ID)
        return uuid.UUID(user_id_str)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Formato de ID de usuario inválido en el token",
            headers={"WWW-Authenticate": "Bearer"},
        )


def get_current_user(
    session: SessionDep,
    current_user_id: Annotated[uuid.UUID, Depends(get_current_user_id)]
):
    """
    Dependencia que toma el ID validado y devuelve el objeto UserAccounts.
    """
    repo = AccountRepository(session)
    user = repo.get_account_by_id(current_user_id) 
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuario inactivo o no encontrado",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    # Aquí sedeben añadir validaciones extra, como el is_active
   

    return user
