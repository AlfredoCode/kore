from pydantic import BaseModel, EmailStr

class EmployeeRegister(BaseModel):
    email: EmailStr
    password: str
    first_name: str
    second_name: str
    employee_role_type_id: int

class EmployeeLogin(BaseModel):
    email: EmailStr
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class RefreshTokenRequest(BaseModel):
    refresh_token: str
