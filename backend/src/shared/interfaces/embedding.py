"""
Embedding provider contract.

All embedding providers (OpenAI, Cohere, local models) must implement
this interface. Consumed by the embedding module and retrieval pipeline.
"""

from abc import ABC, abstractmethod


class BaseEmbeddingProvider(ABC):
    """Abstract base for embedding providers."""

    @abstractmethod
    async def embed(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for a batch of texts."""
        ...

    @property
    @abstractmethod
    def dimension(self) -> int:
        """Return the embedding dimension."""
        ...
