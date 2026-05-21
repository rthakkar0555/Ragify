"""
Pydantic schemas for the ingestion module.
"""

from uuid import UUID

from pydantic import BaseModel


class DocumentUploadRequest(BaseModel):
    collection_id: str | None = None
    metadata: dict | None = None


class DocumentResponse(BaseModel):
    id: UUID
    name: str
    document_type: str
    status: str
    file_size_bytes: int | None = None
    chunk_count: int = 0
    collection_id: str | None = None

    model_config = {"from_attributes": True}


class DocumentStatusResponse(BaseModel):
    id: UUID
    status: str
    chunk_count: int = 0
    error_message: str | None = None
