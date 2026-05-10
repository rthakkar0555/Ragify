"""
Reranker implementations.

All rerankers implement BaseReranker from shared.interfaces.reranker.
"""

from typing import Dict, List
from shared.interfaces.reranker import BaseReranker


class CohereReranker(BaseReranker):
    """Cohere reranker implementation."""

    async def rerank(self, query: str, results: List[Dict], top_k: int = 10) -> List[Dict]:
        # TODO: Implement Cohere rerank API call
        return results[:top_k]


class CrossEncoderReranker(BaseReranker):
    """Local cross-encoder reranker."""

    async def rerank(self, query: str, results: List[Dict], top_k: int = 10) -> List[Dict]:
        # TODO: Implement cross-encoder reranking
        return results[:top_k]
