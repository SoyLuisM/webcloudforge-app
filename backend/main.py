from fastapi import FastAPI
from app.core.config import settings
from app.api.routes import user_account_routes as user_routes


app = FastAPI(
    title=settings.PROJECT_NAME, 
    version= settings.PROJECT_VERSION,
    root_path=settings.PREFIX_API
)



@app.get("/")
async def root():
    return {"message": "hola mundo"}

app.include_router(user_routes.router)