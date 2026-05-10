# RAGify System Architecture

## High-Level Overview

```
┌─────────────┐     ┌─────────────────────────────────────┐
│   Frontend   │────▶│            Nginx / LB               │
│  (Next.js)   │     └──────────┬──────────────────────────┘
└─────────────┘                │
                               ▼
                    ┌──────────────────────┐
                    │   FastAPI Backend     │
                    │   (Modular Monolith)  │
                    │                      │
                    │  ┌───────────────┐   │
                    │  │  Ingestion    │   │
                    │  │  Chunking     │   │
                    │  │  Embedding    │   │
                    │  │  VectorStore  │   │
                    │  │  Retrieval    │   │
                    │  │  Query        │   │
                    │  │  Auth         │   │
                    │  │  Analytics    │   │
                    │  └───────────────┘   │
                    └──────┬───────┬───────┘
                           │       │
              ┌────────────┘       └───────────┐
              ▼                                ▼
    ┌──────────────┐                  ┌──────────────┐
    │  PostgreSQL   │                  │    Redis      │
    │  (metadata)   │                  │  (cache/queue)│
    └──────────────┘                  └──────┬───────┘
                                             │
              ┌──────────────┐               ▼
              │    Qdrant     │     ┌──────────────────┐
              │  (vectors)    │     │  Celery Workers   │
              └──────────────┘     │  - ingestion      │
                                   │  - embedding      │
                                   │  - chunking       │
                                   │  - multimodal     │
                                   └──────────────────┘
```

## Data Flow

1. **Ingestion**: User uploads document → API validates → stores in object storage → dispatches Celery task
2. **Processing**: Worker picks up task → extracts text (multimodal) → chunks text → generates embeddings → indexes in Qdrant
3. **Query**: User sends query → embed query → vector search in Qdrant → optional rerank → return results
4. **Analytics**: Every operation logs metrics → background worker aggregates → dashboard displays

## Module Communication

Modules communicate through an in-process event bus. When migrating to microservices,
the event bus is replaced with a message broker (RabbitMQ/Kafka).
