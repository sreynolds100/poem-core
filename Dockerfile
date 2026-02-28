# POEM - Product Operations Engineering Marketing Lifecycle Agent
# Copyright (C) 2026 Samantha Reynolds
# Licensed under AGPL-3.0. See LICENSE for details.

FROM python:3.11-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY pyproject.toml ./
RUN pip install --no-cache-dir -e ".[dev]" 2>/dev/null || echo "Dependencies will be installed when pyproject.toml is complete"

# Copy application code
COPY poem/ ./poem/
COPY prompts/ ./prompts/
COPY config.example.yaml ./

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD python -c "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')" || exit 1

EXPOSE 8000

CMD ["python", "-m", "poem"]
