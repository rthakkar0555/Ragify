"""
Ingestion domain models.
"""

from sqlalchemy import Column, String, Enum, Integer, JSON, Text
from shared.models.base import Base, UUIDMixin, TimestampMixin
from shared.enums import DocumentStatus, DocumentType


class Document(Base, UUIDMixin, TimestampMixin):
    """Represents an ingested document in the system."""

    __tablename__ = "documents"

    name = Column(String(512), nullable=False)
    source_url = Column(Text, nullable=True)
    document_type = Column(Enum(DocumentType), nullable=False)
    status = Column(Enum(DocumentStatus), default=DocumentStatus.PENDING, nullable=False)
    file_path = Column(Text, nullable=True)
    file_size_bytes = Column(Integer, nullable=True)
    mime_type = Column(String(128), nullable=True)
    metadata = Column(JSON, default=dict)
    chunk_count = Column(Integer, default=0)
    collection_id = Column(String(255), nullable=True)
    tenant_id = Column(String(255), nullable=False)
    error_message = Column(Text, nullable=True)
