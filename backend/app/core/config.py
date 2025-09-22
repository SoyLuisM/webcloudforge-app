from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic_core import MultiHostUrl
from pydantic import(
    PostgresDsn,
    computed_field
)


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        # Use top level .env file (one level above ./backend/)
        env_file=".env",
        env_ignore_empty=True,
        extra="ignore",
    )
    PROJECT_NAME: str = "webcloudforge.com-backend"
    PROJECT_VERSION: str = "0.0.1"
    PREFIX_API: str= "/api"

    DB_GESTOR:str 
    DB_USER:str 
    DB_PASSWORD:str 
    DB_HOST:str 
    DB_PORT:int 
    DB_NAME:str 

    @computed_field  # type: ignore[prop-decorator]
    @property
    def DATABASE_URL(self)->PostgresDsn:
        return MultiHostUrl.build(
            scheme=self.DB_GESTOR,
            username=self.DB_USER,
            password=self.DB_PASSWORD,
            host=self.DB_HOST,
            port=int(self.DB_PORT),
            path=self.DB_NAME
        )
    
settings = Settings()