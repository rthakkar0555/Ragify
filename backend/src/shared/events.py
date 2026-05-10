"""
Domain event bus for inter-module communication.

Enables decoupled communication between modules in the modular monolith.
Events are dispatched in-process now but can be replaced with a message
broker (RabbitMQ, Kafka) for microservice migration.
"""

from typing import Any, Callable, Dict, List

_subscribers: Dict[str, List[Callable]] = {}


def subscribe(event_type: str, handler: Callable) -> None:
    """Register a handler for an event type."""
    if event_type not in _subscribers:
        _subscribers[event_type] = []
    _subscribers[event_type].append(handler)


async def publish(event_type: str, payload: Any) -> None:
    """Publish an event to all registered handlers."""
    handlers = _subscribers.get(event_type, [])
    for handler in handlers:
        await handler(payload)


# --- Event Types ---
DOCUMENT_INGESTED = "document.ingested"
DOCUMENT_CHUNKED = "document.chunked"
DOCUMENT_EMBEDDED = "document.embedded"
DOCUMENT_INDEXED = "document.indexed"
QUERY_EXECUTED = "query.executed"
