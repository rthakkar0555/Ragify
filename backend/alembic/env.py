"""
Alembic configuration for database migrations.
"""


# Import all models for auto-generation
from shared.models.base import Base

target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Run migrations in 'offline' mode."""
    # TODO: Configure offline migration
    pass


def run_migrations_online() -> None:
    """Run migrations in 'online' mode."""
    # TODO: Configure online migration with async engine
    pass
