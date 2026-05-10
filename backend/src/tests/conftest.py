"""
Pytest configuration and shared fixtures.
"""

import pytest
import pytest_asyncio
from httpx import ASGITransport, AsyncClient

from main import app


@pytest_asyncio.fixture
async def client():
    """Async HTTP client for API testing."""
    async with AsyncClient(
        transport=ASGITransport(app=app),
        base_url="http://test",
    ) as ac:
        yield ac


@pytest.fixture
def sample_document_payload():
    """Sample document upload payload for testing."""
    return {
        "name": "test_document.pdf",
        "document_type": "pdf",
        "collection_id": "test-collection",
    }
