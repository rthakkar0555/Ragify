"""
RAGify — FastAPI Application Entry Point

This module bootstraps the FastAPI application, registers routers,
middleware, event handlers, and exception handlers.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings
from core.lifespan import lifespan
from api.router import router


def create_app() -> FastAPI:
    """Application factory for RAGify."""

    app = FastAPI(
        title=settings.PROJECT_NAME,
        version=settings.VERSION,
        description="RAGify — Modular RAG-as-a-Service Platform",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        lifespan=lifespan,
    )

    # --- Middleware ---
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.CORS_ORIGINS,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    # --- Routers ---
    app.include_router(router, prefix=settings.API_V1_PREFIX)

    return app


app = create_app()
