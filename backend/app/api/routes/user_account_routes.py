from fastapi import APIRouter, HTTPException,status

from app.core.connection_db import SessionDep
from app.repositories.AccountRepository import AccountRepository
from app.schemas.account_schemas import CreateAccount, PublicAccount, AccountByEmail

router = APIRouter(prefix='/account')

@router.get('/', response_model=PublicAccount)
async def get_account(session: SessionDep,account: AccountByEmail):
    repo = AccountRepository(session)
    account = repo.get_account_by_email(account.email)
    if not account:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="account not found")
    return account

# @router.post('/create', response_model=PublicAccount)
# async def create_account(session: SessionDep, account_in:CreateAccount ):
#     repo = AccountRepository(session)
#     try:
#         new_account= repo.create_account(account_in=account_in)
#     except Exception as e:
#         print(e)
#         raise HTTPException(
#             status_code=status.HTTP_409_CONFLICT,
#             detail="el usuario ya existe"
#         )
#     return new_account