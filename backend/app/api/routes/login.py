from typing import Annotated
from fastapi import APIRouter, Cookie, Depends, HTTPException, Response, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.utilities.manager_password import create_access_token, create_refresh_token, decode_access_token, verify_password
from app.core.connection_db import SessionDep
from app.models import UsersAccounts
from app.repositories.AccountRepository import AccountRepository
from app.repositories.AuthRepository import get_current_user
from app.schemas.account_schemas import PublicAccount
from app.schemas.aurh_schemas import token
from app.core.config import settings

router = APIRouter(prefix='/login')


@router.post("/access-token",response_model=token)
def login_access_token(session: SessionDep,response: Response, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    #este flujo de datos permite el paso de cualquier valor para el email, y cuqlquier longitud del password
    #eso es algo que no deberia de pasar, se debe de actualizar para lanzar un error en cuanto detecta contraseñas 
    #muy cortas, email con formato no valido, y por seguridad extra limpiar los parametros de signos de puntuacion
    #como ; '' "" -- : , . etc 
    repo = AccountRepository(session)
    user = repo.get_account_by_email(email=form_data.username)
    if not user:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    verify_account = verify_password(password=form_data.password,hashed_passwd=user.hashed_password)

    if not verify_account:
        raise HTTPException(status_code=400, detail="Incorrect email or password")
    # para versiones posteriores considerar que el usuario esté activo
    new_token=create_access_token(subject=user.id)
    refresh_token = create_refresh_token(subject=user.id)

    response.set_cookie(
        key="refresh_token",
        value=refresh_token,
        httponly=True,  # ¡Clave! El JS del frontend no puede leerla
        secure=False,    # Solo enviar por HTTPS (True en producción)
        samesite="lax", # O 'strict'
        max_age=settings.REFRESH_TOKEN_EXPIRE_DAYS * 24 * 60 * 60 # ej. 7 días
    )


    return token(access_token=new_token)


@router.post("/refresh-token", response_model=token)
def refresh_token(
    session: SessionDep,
    refresh_token: Annotated[str | None, Cookie()] = None
):
    """
    Refresca un token de acceso válido por uno nuevo.
    """
    if not refresh_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="No refresh token found"
        )
      
    try:
        # Decodifica el token. Asegúrate de que usas la SECRET_KEY correcta
        # (podrías usar una clave distinta para refresh tokens si quieres)
        user_id  = decode_access_token(refresh_token) 
        
        if not user_id:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid refresh token"
            )
            
        # Opcional pero recomendado:
        # Verifica que el usuario todavía exista y esté activo
        repo = AccountRepository(session)
        user = repo.get_account_by_id(id=user_id) # Asumiendo que tienes este método
        if not user or not user.is_active:
             raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found or inactive"
            )

    except Exception: # (Captura JWTError específico si es posible)
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid or expired refresh token"
        )
    
    # Si el refresh token es válido, emite un NUEVO access token
    new_access_token = create_access_token(subject=user_id)
    
    

    return token(access_token=new_access_token)



@router.get("/users/me", response_model=PublicAccount)
def read_user_me(
    current_user: Annotated[UsersAccounts, Depends(get_current_user)]
) -> PublicAccount:
    """
    Obtiene el usuario actual a partir del token JWT.
    """
    return current_user