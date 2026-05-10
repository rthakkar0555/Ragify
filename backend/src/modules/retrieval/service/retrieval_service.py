"""
Retrieval service — orchestrates the complete retrieval pipeline.
"""

from typing import Dict, List, Optional
from core.logging import get_logger

logger = get_logger(__name__)


class RetrievalService:
    """Orchestrates embedding, vector search, and reranking into a pipeline."""

    def __init__(self, embedding_service, vectorstore_service, reranker=None):
        self._embedding_service = embedding_service
        self._vectorstore_service = vectorstore_service
        self._reranker = reranker

    async def retrieve(
        self,
        query: str,
        collection: str,
        top_k: int = 10,
        filters: Optional[Dict] = None,
        rerank: bool = False,
        hybrid: bool = False,
    ) -> List[Dict]:
        """Execute the retrieval pipeline: embed → search → (rerank)."""
        logger.info("retrieving", query_length=len(query), collection=collection)

        # 1. Embed query
        query_vector = await self._embedding_service.embed_query(query)

        # 2. Vector search
        results = await self._vectorstore_service.search(
            collection=collection,
            query_vector=query_vector,
            top_k=top_k * 3 if rerank else top_k,  # Overfetch for reranking
            filters=filters,
        )

        # 3. Optional hybrid search
        if hybrid:
            # TODO: Combine with BM25/keyword search results
            pass

        # 4. Optional reranking
        if rerank and self._reranker:
            results = await self._reranker.rerank(query, results, top_k=top_k)

        return results[:top_k]
