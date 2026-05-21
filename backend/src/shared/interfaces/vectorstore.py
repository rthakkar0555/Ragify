"""
Vector store adapter contract.

All vector database adapters (Qdrant, Pinecone, Weaviate) must implement
this interface. Consumed by the vectorstore module and retrieval pipeline.
"""

from abc import ABC, abstractmethod


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
        ids: list[str],
        vectors: list[list[float]],
        payloads: list[dict] | None = None,
    ) -> bool:
        """Upsert vectors into a collection."""
        ...

    @abstractmethod
    async def search(
        self,
        collection: str,
        query_vector: list[float],
        top_k: int = 10,
        filters: dict | None = None,
    ) -> list[dict]:
        """Search for nearest neighbors."""
        ...

    @abstractmethod
    async def delete(self, collection: str, ids: list[str]) -> bool:
        """Delete vectors by ID."""
        ...
