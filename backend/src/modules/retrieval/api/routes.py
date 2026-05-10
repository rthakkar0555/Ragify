"""
Retrieval API routes — thin HTTP layer that delegates to services.
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/search")
async def search():
    """Execute a retrieval search query."""
    # TODO: Wire up RetrievalService
    return {"message": "Retrieval search endpoint"}


@router.post("/hybrid-search")
async def hybrid_search():
    """Execute a hybrid (vector + keyword) search."""
    # TODO: Wire up RetrievalService with hybrid=True
    return {"message": "Hybrid search endpoint"}
