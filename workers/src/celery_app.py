"""
Celery application configuration.
"""

from celery import Celery

app = Celery("ragify")

app.config_from_object({
    "broker_url": "redis://localhost:6379/1",
    "result_backend": "redis://localhost:6379/2",
    "task_serializer": "json",
    "result_serializer": "json",
    "accept_content": ["json"],
    "timezone": "UTC",
    "enable_utc": True,
    "task_track_started": True,
    "task_acks_late": True,
    "worker_prefetch_multiplier": 1,
    "task_routes": {
        "workers.tasks.ingestion.*": {"queue": "ingestion"},
        "workers.tasks.embedding.*": {"queue": "embedding"},
        "workers.tasks.chunking.*": {"queue": "chunking"},
        "workers.tasks.multimodal.*": {"queue": "multimodal"},
        "workers.tasks.analytics.*": {"queue": "analytics"},
        "workers.tasks.cleanup.*": {"queue": "cleanup"},
    },
})

# Auto-discover task modules
app.autodiscover_tasks([
    "workers.src.tasks.ingestion",
    "workers.src.tasks.embedding",
    "workers.src.tasks.chunking",
    "workers.src.tasks.multimodal",
    "workers.src.tasks.analytics",
    "workers.src.tasks.cleanup",
])
