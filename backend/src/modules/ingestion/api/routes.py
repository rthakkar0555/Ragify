"""
Ingestion API routes.
"""

from fastapi import APIRouter, Depends, UploadFile, File, Form
from typing import Optional

router = APIRouter()


@router.post("/documents")
async def upload_document(
    file: UploadFile = File(...),
    collection_id: Optional[str] = Form(None),
    # current_user: dict = Depends(get_current_user),
):
    """Upload a document for ingestion."""
    # TODO: Wire up IngestionService
    return {"message": "Document upload endpoint", "filename": file.filename}


@router.get("/documents")
async def list_documents(
    page: int = 1,
    page_size: int = 20,
):
    """List all documents for the current tenant."""
    # TODO: Wire up IngestionService
    return {"message": "Document list endpoint"}


@router.get("/documents/{document_id}")
async def get_document(document_id: str):
    """Get document details by ID."""
    # TODO: Wire up IngestionService
    return {"message": "Document detail endpoint", "document_id": document_id}


@router.delete("/documents/{document_id}")
async def delete_document(document_id: str):
    """Delete a document and all associated data."""
    # TODO: Wire up IngestionService
    return {"message": "Document deleted", "document_id": document_id}


@router.post("/documents/{document_id}/reprocess")
async def reprocess_document(document_id: str):
    """Re-run the ingestion pipeline for a document."""
    # TODO: Wire up IngestionService
    return {"message": "Document reprocessing started", "document_id": document_id}
