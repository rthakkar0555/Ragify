"""
Chunking strategy contract.

All chunking strategies (recursive, semantic, sentence) must implement
this interface. Consumed by the chunking module service.
"""

from abc import ABC, abstractmethod
from typing import List


class BaseChunkingStrategy(ABC):
    """Abstract base class for chunking strategies."""

    @abstractmethod
    def chunk(self, text: str, chunk_size: int, chunk_overlap: int) -> List[str]:
        """Split text into chunks."""
        ...
