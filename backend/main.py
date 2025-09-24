from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import login, user_account_routes as user_routes
from app.core.connection_db import create_initial_super_user


@asynccontextmanager
async def lifespan(app: FastAPI):
    """inicializa al superuser al inicar el sistema"""
    create_initial_super_user()
    yield


app = FastAPI(
    title=settings.PROJECT_NAME, 
    version= settings.PROJECT_VERSION,
    root_path=settings.PREFIX_API,
    lifespan=lifespan
)


@app.get("/")
async def root():
    return {"message": "hola mundo"}

app.include_router(user_routes.router)
app.include_router(login.router)
