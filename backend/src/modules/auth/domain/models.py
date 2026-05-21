"""
Auth domain models.
"""

from sqlalchemy import Boolean, Column, DateTime, String

from shared.models.base import Base, TimestampMixin, UUIDMixin


class User(Base, UUIDMixin, TimestampMixin):
    """Application user."""

    __tablename__ = "users"

    email = Column(String(255), unique=True, nullable=False, index=True)
    hashed_password = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    is_active = Column(Boolean, default=True)
    tenant_id = Column(String(255), nullable=False)


class APIKey(Base, UUIDMixin, TimestampMixin):
    """API key for programmatic access."""

    __tablename__ = "api_keys"

    name = Column(String(255), nullable=False)
    key_hash = Column(String(255), nullable=False, unique=True)
    prefix = Column(String(8), nullable=False)  # First 8 chars for identification
    tenant_id = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    last_used_at = Column(DateTime(timezone=True), nullable=True)
