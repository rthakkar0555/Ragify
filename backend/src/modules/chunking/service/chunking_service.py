"""
Chunking service — orchestrates text splitting strategies.
"""

from typing import List, Optional
from core.logging import get_logger

logger = get_logger(__name__)


class ChunkingService:
    """Applies configurable chunking strategies to document content."""

    def __init__(self, strategy=None):
        self._strategy = strategy

    async def chunk_document(
        self,
        content: str,
        strategy: str = "recursive",
        chunk_size: int = 512,
        chunk_overlap: int = 50,
        metadata: Optional[dict] = None,
    ) -> List[dict]:
        """Split document content into chunks using the specified strategy."""
        logger.info("chunking_document", strategy=strategy, chunk_size=chunk_size)
        # TODO: Delegate to strategy implementation
        return []
