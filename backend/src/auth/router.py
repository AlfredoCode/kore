from src.exceptions import EmailExistsException
from fastapi import APIRouter, Depends, HTTPException, status
from datetime import datetime
from sqlalchemy.orm import Session
from src.database import get_db
from src.employee.models import Employee
from src.auth import utils
from src.auth.schemas import EmployeeRegister, EmployeeLogin, TokenResponse, RefreshTokenRequest
from src.schemas import GenericResponse
router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/register", status_code=201)
def register(user: EmployeeRegister, db: Session = Depends(get_db)):
    if not all([
        user.first_name.strip(),
        user.second_name.strip(),
        user.password.strip(),
        user.email.strip(),
    ]): raise HTTPException(status_code=400, detail="Invalid input")

    existing_user = utils.get_user_by_email(db, user.email)
    if existing_user:
        raise EmailExistsException()

    hashed_password = utils.get_password_hash(user.password)

    new_user = Employee(
        Email=user.email,
        PassHash=hashed_password,
        FirstName=user.first_name,
        SecondName=user.second_name,
        EmployeeRoleTypeId=user.employee_role_type_id,
        SystemAccess=True,
        CreatedDate=datetime.now(),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return GenericResponse(
        message="User created successfully."
    )

@router.post("/login", response_model=TokenResponse)
def login(user: EmployeeLogin, db: Session = Depends(get_db)):
    db_user = utils.get_user_by_email(db, user.email)
    if not db_user or not utils.verify_password(user.password, db_user.PassHash):
        raise HTTPException(status_code=401, detail="Invalid email or password")

    access_token = utils.create_access_token({"sub": db_user.Email})
    refresh_token = utils.create_refresh_token({"sub": db_user.Email})

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)

@router.post("/refresh", response_model=TokenResponse)
def refresh_token(data: RefreshTokenRequest, db: Session = Depends(get_db)):
    payload = utils.verify_token(data.refresh_token, utils.REFRESH_SECRET_KEY)
    if not payload or payload.get("type") != "refresh":
        raise HTTPException(status_code=401, detail="Invalid refresh token")

    email = payload.get("sub")
    user = utils.get_user_by_email(db, email)
    if not user:
        raise HTTPException(status_code=401, detail="User not found")

    access_token = utils.create_access_token({"sub": email})
    refresh_token = utils.create_refresh_token({"sub": email})

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)
