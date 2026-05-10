"""
Pydantic schemas for the ingestion module.
"""

from typing import Dict, Optional
from uuid import UUID
from pydantic import BaseModel


class DocumentUploadRequest(BaseModel):
    collection_id: Optional[str] = None
    metadata: Optional[Dict] = None


class DocumentResponse(BaseModel):
    id: UUID
    name: str
    document_type: str
    status: str
    file_size_bytes: Optional[int] = None
    chunk_count: int = 0
    collection_id: Optional[str] = None

    model_config = {"from_attributes": True}


class DocumentStatusResponse(BaseModel):
    id: UUID
    status: str
    chunk_count: int = 0
    error_message: Optional[str] = None
