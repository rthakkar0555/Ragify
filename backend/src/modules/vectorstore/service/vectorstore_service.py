"""
Vector store service — abstract interface to vector databases.
"""

from core.logging import get_logger

logger = get_logger(__name__)


class VectorStoreService:
    """Manages vector storage and search operations across adapters."""

    def __init__(self, adapter=None):
        self._adapter = adapter

    async def create_collection(self, name: str, dimension: int, **kwargs) -> bool:
        """Create a new vector collection."""
        return await self._adapter.create_collection(name, dimension, **kwargs)

    async def upsert(
        self,
        collection: str,
        ids: list[str],
        vectors: list[list[float]],
        payloads: list[dict] | None = None,
    ) -> bool:
        """Upsert vectors into a collection."""
        logger.info("upserting_vectors", collection=collection, count=len(ids))
        return await self._adapter.upsert(collection, ids, vectors, payloads)

    async def search(
        self,
        collection: str,
        query_vector: list[float],
        top_k: int = 10,
        filters: dict | None = None,
    ) -> list[dict]:
        """Search for nearest neighbors."""
        return await self._adapter.search(collection, query_vector, top_k, filters)

    async def delete(self, collection: str, ids: list[str]) -> bool:
        """Delete vectors by ID."""
        return await self._adapter.delete(collection, ids)
