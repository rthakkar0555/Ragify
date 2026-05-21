"""
Chunk domain models.
"""

from sqlalchemy import JSON, Column, ForeignKey, Integer, String, Text
from sqlalchemy.dialects.postgresql import UUID

from shared.models.base import Base, TimestampMixin, UUIDMixin


class Chunk(Base, UUIDMixin, TimestampMixin):
    """Represents a text chunk derived from a document."""

    __tablename__ = "chunks"

    document_id = Column(UUID(as_uuid=True), ForeignKey("documents.id"), nullable=False)
    content = Column(Text, nullable=False)
    chunk_index = Column(Integer, nullable=False)
    token_count = Column(Integer, nullable=True)
    metadata = Column(JSON, default=dict)
    embedding_id = Column(String(255), nullable=True)  # Reference to vector store ID
