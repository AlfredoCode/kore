from fastapi.responses import JSONResponse
from src.schemas import GenericResponse

class DatabaseException(Exception):
    def __init__(self, detail: str = "Could not perform database operation"):
        self.detail = detail

class EmailExistsException(Exception):
    def __init__(self, detail: str = "Employee with this email already exists"):
        self.detail = detail

def Unauthorized(msg: str):
    return JSONResponse(
        status_code=401,
        content=GenericResponse(statusCode=401, message=msg).model_dump()
    )