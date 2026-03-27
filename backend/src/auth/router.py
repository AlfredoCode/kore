from src.exceptions import EmailExistsException
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime
from sqlalchemy.orm import Session
from src.database import get_db
from src.employee.models import Employee
from src.employee.schemas import EmployeeResponse
from src.auth import utils
from src.auth.schemas import EmployeeRegister, EmployeeLogin, TokenResponse, RefreshTokenRequest
from src.schemas import GenericResponse
from typing import Optional
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

@router.post("/me", response_model=GenericResponse)
def get_current_user(db: Session = Depends(get_db), token: Optional[str] = Depends(utils.optional_oauth2)):
    """
    Returns current logged-in user info wrapped in GenericResponse.
    Uses OAuth2PasswordBearer for token extraction.
    """
    if not token:
        return GenericResponse(success=False, message="No token provided", data=None)
    try:
        payload = utils.verify_token(token, utils.SECRET_KEY)
        print(payload)
    except Exception:
        return GenericResponse(statusCode=401, message="Invalid or expired token")

    if not payload or payload.get("type") != "access":
        return GenericResponse(statusCode=401, message="Invalid or expired token")
    
    email = payload.get("sub")
    user = db.query(Employee).filter(Employee.Email == email).first()
    if not user:
        return GenericResponse(statusCode=401, message="User not found")
    
    user_data = {
        "email": user.Email,
        "first_name": user.FirstName,
        "second_name": user.SecondName,
        "employee_role_type_id": user.EmployeeRoleTypeId,
        "system_access": user.SystemAccess,
    }

    return GenericResponse(success=True, message="User retrieved successfully", data=user_data)