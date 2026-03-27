from pydantic import BaseModel
from typing import Optional, Generic, TypeVar

T = TypeVar("T")

class GenericResponse(BaseModel, Generic[T]):
    statusCode: int = 200
    message: Optional[str] = None
    data: Optional[T] = None