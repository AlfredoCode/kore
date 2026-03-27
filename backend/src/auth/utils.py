from argon2 import PasswordHasher
from argon2.exceptions import VerifyMismatchError
from datetime import datetime, timedelta, timezone
from fastapi import Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.security.utils import get_authorization_scheme_param
from src.employee.models import Employee
from sqlalchemy.orm import Session
from typing import Optional
import jwt
import os

# Initialize the argon2id password hasher
ph = PasswordHasher(time_cost=2, memory_cost=102400, parallelism=8, hash_len=32, salt_len=16)

SECRET_KEY = os.getenv("JWT_SECRET_KEY")
REFRESH_SECRET_KEY = os.getenv("JWT_REFRESH_SECRET_KEY")
ALGORITHM = os.getenv("JWT_ALGORITHM")
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("JWT_ACCESS_TOKEN_EXPIRE_MINUTES", 60))
REFRESH_TOKEN_EXPIRE_DAYS = int(os.getenv("JWT_REFRESH_TOKEN_EXPIRE_DAYS", 7))

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


def get_user_by_email(db: Session, email: str):
    return db.query(Employee).filter(Employee.Email == email).first()

def get_password_hash(password: str) -> str:
    return ph.hash(password)

def verify_password(plain_password: str, hashed_password: str) -> bool:
    try:
        return ph.verify(hashed_password, plain_password)
    except VerifyMismatchError:
        return False

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "type": "access"})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def create_refresh_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.now() + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expire, "type": "refresh"})
    encoded_jwt = jwt.encode(to_encode, REFRESH_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_token(token: str, secret_key: str):
    import jwt
    try:
        payload = jwt.decode(token, secret_key, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        return None
    except jwt.InvalidTokenError:
        return None
    
def optional_oauth2(request: Request) -> Optional[str]:
    """
    Extracts token from the Authorization header.
    Returns None if no token is provided.
    """
    auth: str = request.headers.get("Authorization")
    if not auth:
        return None
    scheme, token = get_authorization_scheme_param(auth)
    if scheme.lower() != "bearer":
        return None
    return token