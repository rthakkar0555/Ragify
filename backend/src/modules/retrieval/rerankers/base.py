"""
Reranker implementations.

All rerankers implement BaseReranker from shared.interfaces.reranker.
"""

from shared.interfaces.reranker import BaseReranker


class CohereReranker(BaseReranker):
    """Cohere reranker implementation."""

    async def rerank(self, query: str, results: list[dict], top_k: int = 10) -> list[dict]:
        # TODO: Implement Cohere rerank API call
        return results[:top_k]


class CrossEncoderReranker(BaseReranker):
    """Local cross-encoder reranker."""

    async def rerank(self, query: str, results: list[dict], top_k: int = 10) -> list[dict]:
        # TODO: Implement cross-encoder reranking
        return results[:top_k]
