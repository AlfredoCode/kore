from pydantic import BaseModel, EmailStr

class EmployeeResponse(BaseModel):
    email: EmailStr
    first_name: str
    second_name: str
    employee_role_type_id: int
    system_access: bool

    class Config:
        orm_mode = True