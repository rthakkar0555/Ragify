"""
API Router — Aggregates all module endpoint routers.
"""

from fastapi import APIRouter

from modules.ingestion.api.routes import router as ingestion_router
from modules.retrieval.api.routes import router as retrieval_router
from modules.query.api.routes import router as query_router
from modules.auth.api.routes import router as auth_router

router = APIRouter()

router.include_router(auth_router, prefix="/auth", tags=["Authentication"])
router.include_router(ingestion_router, prefix="/ingestion", tags=["Ingestion"])
router.include_router(retrieval_router, prefix="/retrieval", tags=["Retrieval"])
router.include_router(query_router, prefix="/query", tags=["Query"])
