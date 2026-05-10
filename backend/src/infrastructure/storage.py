"""
File storage implementations — local filesystem and S3.

Implements the BaseStorage interface from shared.interfaces.storage.
"""

from shared.interfaces.storage import BaseStorage


class LocalStorage(BaseStorage):
    """Local filesystem storage for development."""

    def __init__(self, base_path: str = "./storage"):
        self._base_path = base_path

    async def store(self, content: bytes, filename: str, tenant_id: str) -> str:
        # TODO: Implement local file storage
        return ""

    async def retrieve(self, path: str) -> bytes:
        # TODO: Implement local file retrieval
        return b""

    async def delete(self, path: str) -> bool:
        # TODO: Implement local file deletion
        return True


class S3Storage(BaseStorage):
    """AWS S3 storage for production."""

    def __init__(self, bucket: str, region: str):
        self._bucket = bucket
        self._region = region

    async def store(self, content: bytes, filename: str, tenant_id: str) -> str:
        # TODO: Implement S3 upload
        return ""

    async def retrieve(self, path: str) -> bytes:
        # TODO: Implement S3 download
        return b""

    async def delete(self, path: str) -> bool:
        # TODO: Implement S3 delete
        return True
