"""
Query API routes — public-facing query endpoints for SDK consumers.
"""

from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def execute_query():
    """Execute a RAG query against indexed documents."""
    # TODO: Wire up QueryService → RetrievalService → LLM
    return {"message": "Query execution endpoint"}


@router.post("/stream")
async def stream_query():
    """Execute a RAG query with streaming response."""
    # TODO: Implement SSE streaming response
    return {"message": "Streaming query endpoint"}
