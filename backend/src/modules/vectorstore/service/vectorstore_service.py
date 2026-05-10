"""
Vector store service — abstract interface to vector databases.
"""

from typing import Dict, List, Optional
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
        ids: List[str],
        vectors: List[List[float]],
        payloads: Optional[List[Dict]] = None,
    ) -> bool:
        """Upsert vectors into a collection."""
        logger.info("upserting_vectors", collection=collection, count=len(ids))
        return await self._adapter.upsert(collection, ids, vectors, payloads)

    async def search(
        self,
        collection: str,
        query_vector: List[float],
        top_k: int = 10,
        filters: Optional[Dict] = None,
    ) -> List[Dict]:
        """Search for nearest neighbors."""
        return await self._adapter.search(collection, query_vector, top_k, filters)

    async def delete(self, collection: str, ids: List[str]) -> bool:
        """Delete vectors by ID."""
        return await self._adapter.delete(collection, ids)
