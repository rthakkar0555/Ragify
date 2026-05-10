"""
Health check and system status endpoints.
"""

from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
async def health_check():
    """Basic health check endpoint."""
    return {"status": "healthy", "service": "ragify-api"}


@router.get("/readiness")
async def readiness_check():
    """Readiness probe — checks database and critical service connectivity."""
    # TODO: Check PostgreSQL, Redis, Qdrant connectivity
    return {"status": "ready"}
