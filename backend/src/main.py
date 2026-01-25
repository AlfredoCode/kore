from fastapi import FastAPI, APIRouter
from src.auth.router import router as auth_router

app = FastAPI(
    title="Kore Backend API",
    description="API for Kore project management",
    version="1.0.0",
)

api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Kore API"}
