FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential ffmpeg \
    && rm -rf /var/lib/apt/lists/*

COPY workers/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY backend/src/ ./src/
COPY workers/src/ ./workers/

CMD ["celery", "-A", "workers.src.celery_app", "worker", "--loglevel=info", "--concurrency=4"]
