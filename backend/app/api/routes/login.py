from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from app.api.utilities.manager_password import create_access_token, verify_password
from app.core.connection_db import SessionDep
from app.models import UsersAccounts
from app.repositories.AccountRepository import AccountRepository
from app.repositories.AuthRepository import get_current_user
from app.schemas.account_schemas import PublicAccount
from app.schemas.aurh_schemas import token

router = APIRouter(prefix='/login')

@router.post("/access-token",response_model=token)
def login_access_token(session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
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
    return token(access_token=new_token)


@router.post("/refresh-token", response_model=token)
def refresh_token(
    current_user: Annotated[UsersAccounts, Depends(get_current_user)]
):
    """
    Refresca un token de acceso válido por uno nuevo.
    """
      
    new_token = create_access_token(subject=current_user.id)
    
    

    return token(access_token=new_token)

@router.get("/users/me", response_model=PublicAccount)
def read_user_me(
    current_user: Annotated[UsersAccounts, Depends(get_current_user)]
) -> PublicAccount:
    """
    Obtiene el usuario actual a partir del token JWT.
    """
    return current_user