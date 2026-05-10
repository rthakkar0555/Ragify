"""
Chunking strategy implementations.

All strategies implement BaseChunkingStrategy from shared.interfaces.chunker.
"""

from shared.interfaces.chunker import BaseChunkingStrategy
from typing import List


class RecursiveChunkingStrategy(BaseChunkingStrategy):
    """Recursively splits text using multiple separators."""

    def chunk(self, text: str, chunk_size: int = 512, chunk_overlap: int = 50) -> List[str]:
        # TODO: Implement recursive character text splitting
        return []


class SemanticChunkingStrategy(BaseChunkingStrategy):
    """Splits text based on semantic similarity between sentences."""

    def chunk(self, text: str, chunk_size: int = 512, chunk_overlap: int = 50) -> List[str]:
        # TODO: Implement semantic chunking using embeddings
        return []


class SentenceChunkingStrategy(BaseChunkingStrategy):
    """Splits text at sentence boundaries."""

    def chunk(self, text: str, chunk_size: int = 512, chunk_overlap: int = 50) -> List[str]:
        # TODO: Implement sentence-level splitting
        return []
