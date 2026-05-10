"""
Reranker contract.

All reranking models (Cohere, cross-encoder, etc.) must implement
this interface. Consumed by the retrieval pipeline.
"""

from abc import ABC, abstractmethod
from typing import Dict, List


class BaseReranker(ABC):
    """Abstract base for reranking models."""

    @abstractmethod
    async def rerank(self, query: str, results: List[Dict], top_k: int = 10) -> List[Dict]:
        """Rerank search results based on relevance to query."""
        ...
