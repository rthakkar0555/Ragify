"""
Multimodal content processor contract.

All modality processors (PDF, audio, video, image, website) must implement
this interface. Consumed by the multimodal module and ingestion pipeline.
"""

from abc import ABC, abstractmethod
from typing import Dict, Optional


class BaseProcessor(ABC):
    """Abstract processor for multimodal content."""

    @abstractmethod
    async def process(self, file_path: str, metadata: Optional[Dict] = None) -> Dict:
        """Process a file and return extracted text + metadata."""
        ...
