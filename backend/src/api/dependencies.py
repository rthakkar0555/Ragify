"""
FastAPI dependency injection — auth and database session providers.
"""

from collections.abc import AsyncGenerator

from fastapi import Depends, HTTPException, Security, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.ext.asyncio import AsyncSession

from core.security import decode_access_token
from infrastructure.database import async_session_factory

security = HTTPBearer()


# --- Auth Dependencies ---

async def get_current_user(
    credentials: HTTPAuthorizationCredentials = Security(security),
) -> dict:
    """Extract and validate the current user from the JWT token."""
    try:
        payload = decode_access_token(credentials.credentials)
        user_id = payload.get("sub")
        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token",
            )
        return {"user_id": user_id}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
        )


async def get_current_active_user(
    current_user: dict = Depends(get_current_user),
) -> dict:
    """Ensure the current user is active."""
    # TODO: Check user status in database
    return current_user


# --- Database Dependencies ---

async def get_db() -> AsyncGenerator[AsyncSession, None]:
    """Provide an async database session per request."""
    async with async_session_factory() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
