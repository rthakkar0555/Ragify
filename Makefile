.PHONY: help dev backend frontend workers test lint docker-up docker-down migrate

help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'

# ─── Development ──────────────────────────────────────
dev: ## Start infra services for local development
	docker compose up -d postgres redis qdrant
	@echo "Infrastructure services started."

backend: ## Run backend server locally
	cd backend && uvicorn src.main:app --reload --host 0.0.0.0 --port 8000

frontend: ## Run frontend dev server
	cd frontend && npm run dev

workers: ## Run Celery workers locally
	cd workers && celery -A src.celery_app worker --loglevel=info --concurrency=4

worker-beat: ## Run Celery Beat scheduler
	cd workers && celery -A src.celery_app beat --loglevel=info

# ─── Testing ──────────────────────────────────────────
test: ## Run all backend tests
	cd backend && pytest src/tests/ -v --cov=src

test-unit: ## Run unit tests only
	cd backend && pytest src/tests/unit/ -v

test-integration: ## Run integration tests
	cd backend && pytest src/tests/integration/ -v

# ─── Linting ──────────────────────────────────────────
lint: ## Lint backend code
	cd backend && ruff check src/ && ruff format --check src/

format: ## Format backend code
	cd backend && ruff format src/

# ─── Database ─────────────────────────────────────────
migrate: ## Run database migrations
	cd backend && alembic upgrade head

migrate-create: ## Create a new migration (usage: make migrate-create MSG="description")
	cd backend && alembic revision --autogenerate -m "$(MSG)"

migrate-rollback: ## Rollback last migration
	cd backend && alembic downgrade -1

# ─── Docker ───────────────────────────────────────────
docker-up: ## Start all services with Docker
	docker compose up -d --build

docker-down: ## Stop all Docker services
	docker compose down

docker-logs: ## View Docker logs
	docker compose logs -f

docker-clean: ## Remove all Docker volumes and images
	docker compose down -v --rmi all

# ─── Utilities ────────────────────────────────────────
seed: ## Seed database with sample data
	python scripts/seed/seed_data.py

clean: ## Clean build artifacts
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
