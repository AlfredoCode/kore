from fastapi import HTTPException

class EmailExistsException(HTTPException):
    def __init__(self, detail: str = "Employee with this email already exists"):
        super().__init__(status_code=409, detail=detail)
