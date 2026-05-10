"""
Alembic configuration for database migrations.
"""

from logging.config import fileConfig
from sqlalchemy import pool
from alembic import context

# Import all models for auto-generation
from shared.models.base import Base
from modules.ingestion.domain.models import Document
from modules.chunking.domain.models import Chunk
from modules.auth.domain.models import User, APIKey

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    # TODO: Configure offline migration
    pass


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # TODO: Configure online migration with async engine
    pass
