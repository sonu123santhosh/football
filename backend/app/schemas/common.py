"""
Common Pydantic Schemas & Standardized JSON Response Envelope
"""

from typing import Generic, TypeVar, Optional, Any
from pydantic import BaseModel

T = TypeVar("T")

class APIResponse(BaseModel, Generic[T]):
    success: bool = True
    data: Optional[T] = None
    message: Optional[str] = "Success"

class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    code: Optional[int] = 400
    details: Optional[Any] = None

class PaginatedMeta(BaseModel):
    total: int
    page: int
    limit: int
    total_pages: int
