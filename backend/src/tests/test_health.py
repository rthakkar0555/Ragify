import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_health_check(client: AsyncClient):
    """Test that the basic health check returns 200 and success status."""
    response = await client.get("/api/v1/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy", "service": "ragify-api"}


@pytest.mark.asyncio
async def test_readiness_check(client: AsyncClient):
    """Test that the readiness check returns 200 and ready status."""
    response = await client.get("/api/v1/readiness")
    assert response.status_code == 200
    assert response.json() == {"status": "ready"}
