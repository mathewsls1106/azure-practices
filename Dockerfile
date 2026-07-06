
# === Etapa de base ===
FROM python:3.12-slim AS base
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# === Etapa de constructor (dev) ===
FROM base AS builder-dev
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
RUN uv venv /app/.venv && \
    UV_PROJECT_ENVIRONMENT=/app/.venv uv sync --frozen

# === Etapa de constructor (prod) ===
FROM base AS builder-prod
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY pyproject.toml uv.lock ./
RUN uv venv /app/.venv && \
    UV_PROJECT_ENVIRONMENT=/app/.venv uv sync --frozen --no-dev

# === Etapa de desarrollo ===
FROM base AS development
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/
COPY --from=builder-dev /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
ENV UV_PROJECT_ENVIRONMENT=/app/.venv
RUN mkdir -p /app/data
EXPOSE 8000

CMD ["sh", "-c", "uv sync --frozen && python manage.py runserver 0.0.0.0:8000"]



FROM base AS production
COPY --from=builder-prod /app/.venv /app/.venv
ENV PATH="/app/.venv/bin:$PATH"
COPY . .
RUN mkdir -p /app/data
EXPOSE 8000

CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3"]
