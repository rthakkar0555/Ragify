# ADR-001: Modular Monolith Architecture

## Status
Accepted

## Context
RAGify needs to balance development speed with future scalability.
A pure microservice architecture would add unnecessary complexity at this stage,
while a monolith would make future decomposition difficult.

## Decision
Adopt a modular monolith architecture where:
- Each domain module (`ingestion`, `chunking`, `embedding`, etc.) is self-contained
- Modules communicate via an in-process event bus
- Shared infrastructure is accessed through abstractions
- Module boundaries are enforced at the package level

## Consequences
- **Positive**: Faster development, simpler deployment, easy refactoring
- **Positive**: Clear migration path to microservices (each module → service)
- **Negative**: Requires discipline to maintain module boundaries
- **Mitigation**: CI checks for cross-module import violations
