"""
Vector store adapter contract.

All vector database adapters (Qdrant, Pinecone, Weaviate) must implement
this interface. Consumed by the vectorstore module and retrieval pipeline.
"""

from abc import ABC, abstractmethod
from typing import Dict, List, Optional


class BaseVectorStoreAdapter(ABC):
    """Abstract adapter for vector database operations."""

    @abstractmethod
    async def create_collection(self, name: str, dimension: int, **kwargs) -> bool:
        """Create a new vector collection."""
        ...

    @abstractmethod
    async def upsert(
        self,
        collection: str,
        ids: List[str],
        vectors: List[List[float]],
        payloads: Optional[List[Dict]] = None,
    ) -> bool:
        """Upsert vectors into a collection."""
        ...

    @abstractmethod
    async def search(
        self,
        collection: str,
        query_vector: List[float],
        top_k: int = 10,
        filters: Optional[Dict] = None,
    ) -> List[Dict]:
        """Search for nearest neighbors."""
        ...

    @abstractmethod
    async def delete(self, collection: str, ids: List[str]) -> bool:
        """Delete vectors by ID."""
        ...
