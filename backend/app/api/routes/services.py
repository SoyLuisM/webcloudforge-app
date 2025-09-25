from typing import Annotated
from fastapi import APIRouter, Depends

from app.models import UsersAccounts
from app.repositories.AuthRepository import get_current_user

router = APIRouter(prefix='/services')


@router.get("/")
def read_user_me(
    current_user: Annotated[UsersAccounts, Depends(get_current_user)]
) :
    """
    ruta de prueba
    """
    return {'message': 'hola autenticado'}