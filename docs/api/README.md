# RAGify API Documentation

## Base URL
```
https://api.ragify.dev/v1
```

## Authentication
All API requests require a Bearer token or API key:
```
Authorization: Bearer <api_key>
```

## Endpoints

### Ingestion
- `POST /ingestion/documents` — Upload a document
- `GET /ingestion/documents` — List documents
- `GET /ingestion/documents/{id}` — Get document details
- `DELETE /ingestion/documents/{id}` — Delete a document

### Retrieval
- `POST /retrieval/search` — Vector search
- `POST /retrieval/hybrid-search` — Hybrid search

### Query
- `POST /query/` — Execute RAG query
- `POST /query/stream` — Streaming RAG query

### Auth
- `POST /auth/register` — Register
- `POST /auth/login` — Login
- `POST /auth/api-keys` — Create API key
- `GET /auth/api-keys` — List API keys
