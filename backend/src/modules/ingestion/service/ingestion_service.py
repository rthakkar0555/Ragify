"""
Ingestion service — orchestrates document intake pipeline.
"""

from uuid import UUID

from core.logging import get_logger
from shared.events import DOCUMENT_INGESTED, publish

logger = get_logger(__name__)


class IngestionService:
    """Coordinates document upload, validation, storage, and pipeline dispatch."""

    def __init__(self, repository, storage, task_queue):
        self._repository = repository
        self._storage = storage
        self._task_queue = task_queue

    async def ingest_document(
        self,
        file_content: bytes,
        filename: str,
        document_type: str,
        tenant_id: str,
        collection_id: str | None = None,
        metadata: dict | None = None,
    ) -> dict:
        """Ingest a new document into the system."""
        logger.info("ingesting_document", filename=filename, tenant_id=tenant_id)

        # 1. Store raw file
        file_path = await self._storage.store(file_content, filename, tenant_id)

        # 2. Create document record
        document = await self._repository.create(
            name=filename,
            document_type=document_type,
            file_path=file_path,
            file_size_bytes=len(file_content),
            tenant_id=tenant_id,
            collection_id=collection_id,
            metadata=metadata or {},
        )

        # 3. Dispatch async processing pipeline
        self._task_queue.send_task(
            "workers.tasks.ingestion.process_document",
            args=[str(document.id)],
        )

        # 4. Publish domain event
        await publish(DOCUMENT_INGESTED, {"document_id": str(document.id)})

        return {"document_id": str(document.id), "status": "processing"}

    async def get_document(self, document_id: UUID, tenant_id: str) -> dict:
        """Retrieve document metadata by ID."""
        return await self._repository.get_by_id(document_id, tenant_id)

    async def list_documents(
        self, tenant_id: str, page: int = 1, page_size: int = 20
    ) -> dict:
        """List documents for a tenant with pagination."""
        return await self._repository.list_paginated(tenant_id, page, page_size)

    async def delete_document(self, document_id: UUID, tenant_id: str) -> bool:
        """Delete a document and its associated chunks/embeddings."""
        logger.info("deleting_document", document_id=str(document_id))
        # TODO: Delete from vector store, storage, and database
        return await self._repository.delete(document_id, tenant_id)
