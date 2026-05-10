"""
RAGify exception hierarchy.

All domain exceptions inherit from RAGifyError to enable
centralized exception handling at the API layer.
"""


class RAGifyError(Exception):
    """Base exception for all RAGify errors."""

    def __init__(self, message: str, error_code: str = "RAGIFY_ERROR"):
        self.message = message
        self.error_code = error_code
        super().__init__(self.message)


class DocumentNotFoundError(RAGifyError):
    def __init__(self, document_id: str):
        super().__init__(
            message=f"Document not found: {document_id}",
            error_code="DOCUMENT_NOT_FOUND",
        )


class IngestionError(RAGifyError):
    def __init__(self, message: str):
        super().__init__(message=message, error_code="INGESTION_ERROR")


class ChunkingError(RAGifyError):
    def __init__(self, message: str):
        super().__init__(message=message, error_code="CHUNKING_ERROR")


class EmbeddingError(RAGifyError):
    def __init__(self, message: str):
        super().__init__(message=message, error_code="EMBEDDING_ERROR")


class VectorStoreError(RAGifyError):
    def __init__(self, message: str):
        super().__init__(message=message, error_code="VECTORSTORE_ERROR")


class RetrievalError(RAGifyError):
    def __init__(self, message: str):
        super().__init__(message=message, error_code="RETRIEVAL_ERROR")


class AuthenticationError(RAGifyError):
    def __init__(self, message: str = "Authentication failed"):
        super().__init__(message=message, error_code="AUTH_ERROR")


class AuthorizationError(RAGifyError):
    def __init__(self, message: str = "Insufficient permissions"):
        super().__init__(message=message, error_code="AUTHORIZATION_ERROR")


class RateLimitExceededError(RAGifyError):
    def __init__(self, message: str = "Rate limit exceeded"):
        super().__init__(message=message, error_code="RATE_LIMIT_EXCEEDED")


class QuotaExceededError(RAGifyError):
    def __init__(self, message: str = "Quota exceeded"):
        super().__init__(message=message, error_code="QUOTA_EXCEEDED")
