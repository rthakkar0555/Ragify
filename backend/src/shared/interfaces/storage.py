"""
File storage contract.

All storage backends (local filesystem, S3, GCS) must implement
this interface. Consumed by the ingestion module and infrastructure layer.
"""

from abc import ABC, abstractmethod


class BaseStorage(ABC):
    """Abstract file storage interface."""

    @abstractmethod
    async def store(self, content: bytes, filename: str, tenant_id: str) -> str:
        """Store file and return the storage path/URL."""
        ...

    @abstractmethod
    async def retrieve(self, path: str) -> bytes:
        """Retrieve file content by path."""
        ...

    @abstractmethod
    async def delete(self, path: str) -> bool:
        """Delete a file by path."""
        ...
