.PHONY: help dev backend frontend workers worker-beat \
test test-unit test-integration \
lint format frontend-lint frontend-build \
docker-test check \
docker-up docker-down docker-logs docker-clean \
migrate migrate-create migrate-rollback \
seed clean

# ─── Help ─────────────────────────────────────────────
help: ## Show this help message
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-25s\033[0m %s\n", $$1, $$2}'

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
	cd backend && pytest src/tests/ -v --cov=src --cov-report=term-missing

test-unit: ## Run unit tests only
	cd backend && pytest src/tests/unit/ -v

test-integration: ## Run integration tests
	cd backend && pytest src/tests/integration/ -v

# ─── Backend Linting & Formatting ─────────────────────
lint: ## Lint backend code
	cd backend && ruff check src/

format: ## Format backend code
	cd backend && ruff format src/

format-check: ## Check backend formatting
	cd backend && ruff format --check src/

# ─── Frontend ─────────────────────────────────────────
frontend-lint: ## Run frontend lint
	cd frontend && npm run lint

frontend-build: ## Run frontend production build
	cd frontend && npm run build

# ─── Docker ───────────────────────────────────────────
docker-test: ## Test frontend Docker build
	docker build -f infra/docker/frontend/Dockerfile .

docker-up: ## Start all services with Docker
	docker compose up -d --build

docker-down: ## Stop all Docker services
	docker compose down

docker-logs: ## View Docker logs
	docker compose logs -f

docker-clean: ## Remove all Docker volumes and images
	docker compose down -v --rmi all

# ─── Database ─────────────────────────────────────────
migrate: ## Run database migrations
	cd backend && alembic upgrade head

migrate-create: ## Create a new migration
	cd backend && alembic revision --autogenerate -m "$(MSG)"

migrate-rollback: ## Rollback last migration
	cd backend && alembic downgrade -1

seed: ## Seed database with sample data
	python scripts/seed/seed_data.py

# ─── CI / Pre-push Checks ─────────────────────────────
check: ## Run all CI checks locally
	make lint
	make format-check
	make test
	make frontend-lint
	make frontend-build
	make docker-test
	@echo "All checks passed successfully."

# ─── Utilities ────────────────────────────────────────
clean: ## Clean build artifacts and caches
	find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .pytest_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name .ruff_cache -exec rm -rf {} + 2>/dev/null || true
	find . -type d -name node_modules -prune -o -type f -name "*.pyc" -exec rm -f {} + 2>/dev/null || true