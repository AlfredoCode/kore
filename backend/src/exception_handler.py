# src/exception_handlers.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from src.schemas import GenericResponse
from src.exceptions import DatabaseException, EmailExistsException

def register_exception_handlers(app: FastAPI):
    @app.exception_handler(DatabaseException)
    async def database_exception_handler(request: Request, exc: DatabaseException):
        return JSONResponse(
            status_code=500,
            content=GenericResponse(
                statusCode=500,
                message=exc.detail
            ).dict()
        )

    @app.exception_handler(EmailExistsException)
    async def email_exists_exception_handler(request: Request, exc: EmailExistsException):
        return JSONResponse(
            status_code=409,
            content=GenericResponse(
                statusCode=409,
                message=exc.detail
            ).dict()
        )