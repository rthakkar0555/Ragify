"""
Embedding service — generates vector embeddings via pluggable providers.
"""

from core.logging import get_logger

logger = get_logger(__name__)


class EmbeddingService:
    """Generates embeddings using configurable providers."""

    def __init__(self, provider=None):
        self._provider = provider

    async def embed_texts(self, texts: list[str]) -> list[list[float]]:
        """Generate embeddings for a list of texts."""
        logger.info("embedding_texts", count=len(texts))
        return await self._provider.embed(texts)

    async def embed_query(self, query: str) -> list[float]:
        """Generate embedding for a single query string."""
        results = await self.embed_texts([query])
        return results[0]
