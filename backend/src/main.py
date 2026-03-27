from fastapi import FastAPI, APIRouter
from src.auth.router import router as auth_router
from src.exception_handler import register_exception_handlers
app = FastAPI(
    title="Kore Backend API",
    description="API for Kore project management",
    version="1.0.0",
)

register_exception_handlers(app)

api_router = APIRouter(prefix="/api")
api_router.include_router(auth_router)

app.include_router(api_router)

@app.get("/")
async def root():
    return {"message": "Welcome to Kore API"}
