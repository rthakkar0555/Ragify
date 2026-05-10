"""
Embedding provider implementations.

All providers implement BaseEmbeddingProvider from shared.interfaces.embedding.
"""

from typing import List
from shared.interfaces.embedding import BaseEmbeddingProvider


class OpenAIEmbeddingProvider(BaseEmbeddingProvider):
    """OpenAI text-embedding provider."""

    def __init__(self, model: str = "text-embedding-3-small", api_key: str = None):
        self._model = model
        self._api_key = api_key

    async def embed(self, texts: List[str]) -> List[List[float]]:
        # TODO: Implement OpenAI API call with batching
        return []

    @property
    def dimension(self) -> int:
        dimensions = {
            "text-embedding-3-small": 1536,
            "text-embedding-3-large": 3072,
            "text-embedding-ada-002": 1536,
        }
        return dimensions.get(self._model, 1536)


class CohereEmbeddingProvider(BaseEmbeddingProvider):
    """Cohere embedding provider."""

    async def embed(self, texts: List[str]) -> List[List[float]]:
        # TODO: Implement Cohere API call
        return []

    @property
    def dimension(self) -> int:
        return 1024


class LocalEmbeddingProvider(BaseEmbeddingProvider):
    """Local model embedding provider (e.g., sentence-transformers)."""

    async def embed(self, texts: List[str]) -> List[List[float]]:
        # TODO: Implement local model inference
        return []

    @property
    def dimension(self) -> int:
        return 384
