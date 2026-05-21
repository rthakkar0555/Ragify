"""
Reranker contract.

All reranking models (Cohere, cross-encoder, etc.) must implement
this interface. Consumed by the retrieval pipeline.
"""

from abc import ABC, abstractmethod


class BaseReranker(ABC):
    """Abstract base for reranking models."""

    @abstractmethod
    async def rerank(self, query: str, results: list[dict], top_k: int = 10) -> list[dict]:
        """Rerank search results based on relevance to query."""
        ...
