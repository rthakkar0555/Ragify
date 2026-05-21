"""
Shared enums used across multiple modules.

Extracted from domain models to prevent cross-module imports
and provide a single source of truth for status/type values.
"""

import enum


class DocumentStatus(enum.StrEnum):
    PENDING = "pending"
    PROCESSING = "processing"
    CHUNKED = "chunked"
    EMBEDDED = "embedded"
    INDEXED = "indexed"
    FAILED = "failed"


class DocumentType(enum.StrEnum):
    PDF = "pdf"
    TEXT = "text"
    MARKDOWN = "markdown"
    HTML = "html"
    DOCX = "docx"
    CSV = "csv"
    AUDIO = "audio"
    VIDEO = "video"
    IMAGE = "image"
    WEBSITE = "website"
