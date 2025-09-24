from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.api.utilities.manager_password import create_access_token, verify_password
from app.core.connection_db import SessionDep
from app.repositories.AccountRepository import AccountRepository
from app.schemas.aurh_schemas import token

router = APIRouter(prefix='/login')

@router.post("/access-token")
def login_access_token(session: SessionDep, form_data: Annotated[OAuth2PasswordRequestForm, Depends()])->token:
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