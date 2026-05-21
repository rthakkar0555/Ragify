"""
Reusable pagination utilities.
"""

from typing import TypeVar

from pydantic import BaseModel, Field

from shared.constants import DEFAULT_PAGE_SIZE, MAX_PAGE_SIZE

T = TypeVar("T")


class PaginationParams(BaseModel):
    """Query parameters for paginated endpoints."""
    page: int = Field(default=1, ge=1)
    page_size: int = Field(default=DEFAULT_PAGE_SIZE, ge=1, le=MAX_PAGE_SIZE)

    @property
    def offset(self) -> int:
        return (self.page - 1) * self.page_size


def paginate(items: list, total: int, params: PaginationParams) -> dict:
    """Build a paginated response dict."""
    return {
        "items": items,
        "total": total,
        "page": params.page,
        "page_size": params.page_size,
        "total_pages": (total + params.page_size - 1) // params.page_size,
    }
