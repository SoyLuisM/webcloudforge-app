from sqlmodel import Session, select
from pydantic import EmailStr
from app.api.utilities.manager_password import get_password_hash
from app.models.UsersAccounts import UsersAccounts
from app.schemas.account_schemas import CreateAccount, PublicAccount



class AccountRepository():
    session: Session

    def __init__(self, session: Session):
        self.session= session
        
    def get_account_by_email(self,email:EmailStr)->PublicAccount:
        query = select(UsersAccounts).where(UsersAccounts.email == email)
        account = self.session.exec(query).first()
        return account

    def create_account(self, account_in: CreateAccount)->PublicAccount:
        account = self.get_account_by_email(account_in.email)

        if account:
            raise Exception('El usuario ya existe')
        
        new_acount = UsersAccounts.model_validate(
            account_in,
            update={'hashed_password': get_password_hash(account_in.password) }
        )

        self.session.add(new_acount)
        self.session.commit()
        self.session.refresh(new_acount)
        return new_acount
    
    def verify_admin(self)->bool:
        query = select(UsersAccounts).where(UsersAccounts.is_admin == True)
        account = self.session.exec(query).first()
        return True if account else False

    def create_super_user(self, account_in: CreateAccount)->bool:
        if self.verify_admin():
            return False
        new_acount = UsersAccounts.model_validate(
            account_in,
            update={ 
                'hashed_password': get_password_hash(account_in.password),
                'is_active': True,
                'is_admin':True
            }
        )

        self.session.add(new_acount)
        self.session.commit()
        self.session.refresh(new_acount)
        return True