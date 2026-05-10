"""
Observability — OpenTelemetry tracing and Prometheus metrics.
"""

# --- Tracing ---
# TODO: Initialize OpenTelemetry with OTLP exporter
# - Configure trace provider
# - Instrument FastAPI
# - Instrument SQLAlchemy
# - Instrument httpx/aiohttp
# - Custom spans for RAG pipeline stages

# --- Metrics ---
# TODO: Define custom Prometheus metrics
# - ragify_documents_ingested_total (counter)
# - ragify_queries_total (counter)
# - ragify_retrieval_latency_seconds (histogram)
# - ragify_embedding_latency_seconds (histogram)
# - ragify_active_workers (gauge)
