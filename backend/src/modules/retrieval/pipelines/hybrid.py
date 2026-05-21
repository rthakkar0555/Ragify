"""
Hybrid retrieval pipeline — combines vector search with keyword/BM25 search.

This module contains pure orchestration logic, not HTTP routes.
"""



async def hybrid_retrieve(
    query: str,
    collection: str,
    embedding_service,
    vectorstore_service,
    top_k: int = 10,
    vector_weight: float = 0.7,
    keyword_weight: float = 0.3,
    filters: dict | None = None,
) -> list[dict]:
    """
    Execute hybrid retrieval: vector search + keyword search, then merge.
    
    Reciprocal Rank Fusion (RRF) is used to combine result lists.
    """
    # 1. Embed query
    query_vector = await embedding_service.embed_query(query)

    # 2. Vector search
    vector_results = await vectorstore_service.search(
        collection=collection,
        query_vector=query_vector,
        top_k=top_k * 2,
        filters=filters,
    )

    # 3. Keyword search (BM25)
    # TODO: Implement BM25/full-text search via PostgreSQL or Elasticsearch
    keyword_results = []

    # 4. Merge using Reciprocal Rank Fusion
    # TODO: Implement RRF scoring
    merged = vector_results  # Placeholder: use vector results only for now

    return merged[:top_k]
