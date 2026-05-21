"""
RAGify Python SDK Client.
"""

from typing import Dict, List
import httpx


class RAGifyClient:
    """Python client for the RAGify API."""

    def __init__(self, api_key: str, base_url: str = "https://api.ragify.dev/v1"):
        self._api_key = api_key
        self._base_url = base_url
        self._client = httpx.Client(
            base_url=base_url,
            headers={"Authorization": f"Bearer {api_key}"},
            timeout=30.0,
        )

    def ingest(self, file_path: str, collection: str = "default", **kwargs) -> Dict:
        """Upload and ingest a document."""
        # TODO: Implement file upload
        pass

    def query(self, query: str, collection: str = "default", top_k: int = 10, **kwargs) -> Dict:
        """Execute a RAG query."""
        response = self._client.post(
            "/query",
            json={"query": query, "collection": collection, "top_k": top_k, **kwargs},
        )
        response.raise_for_status()
        return response.json()

    def search(self, query: str, collection: str = "default", top_k: int = 10) -> List[Dict]:
        """Search for similar documents."""
        response = self._client.post(
            "/retrieval/search",
            json={"query": query, "collection": collection, "top_k": top_k},
        )
        response.raise_for_status()
        return response.json()

    def list_documents(self, collection: str = "default") -> List[Dict]:
        """List all documents in a collection."""
        response = self._client.get("/ingestion/documents", params={"collection": collection})
        response.raise_for_status()
        return response.json()

    def close(self):
        """Close the HTTP client."""
        self._client.close()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()
