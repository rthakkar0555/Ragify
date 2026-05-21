"""
Standard API response schemas shared across all endpoints.
"""

from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar("T")


class ResponseSchema(BaseModel, Generic[T]):
    """Standard API response envelope."""
    success: bool = True
    data: T | None = None
    message: str | None = None


class PaginatedResponse(BaseModel, Generic[T]):
    """Paginated API response."""
    items: list[T]
    total: int
    page: int
    page_size: int
    total_pages: int


class ErrorResponse(BaseModel):
    """Standard error response."""
    success: bool = False
    error: str
    detail: Any | None = None
    error_code: str | None = None
