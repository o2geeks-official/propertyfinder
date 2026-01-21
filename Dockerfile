# ---------- Build Stage ----------
FROM python:3.13-slim AS builder

# Install uv, git and other build dependencies
RUN apt-get update && apt-get install -y curl git && rm -rf /var/lib/apt/lists/*

# Set the working directory
WORKDIR /fastapi-app

# Copy project configuration and source files
COPY pyproject.toml README.md ./
COPY propertfinder_api ./propertfinder_api

# Install uv, create a virtual environment, and install dependencies
RUN curl -LsSf https://astral.sh/uv/install.sh | sh && \
    export PATH="/root/.local/bin:$PATH" && \
    uv venv && \
    . .venv/bin/activate && \
    uv sync

# ---------- Production Stage ----------
FROM python:3.13-slim

# Set the working directory
WORKDIR /fastapi-app

# Set Python environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copy the virtual environment from the builder stage
COPY --from=builder /fastapi-app/.venv ./.venv

# Copy the application code
COPY propertfinder_api ./propertfinder_api

# Activate the virtual environment
ENV PATH="/fastapi-app/.venv/bin:$PATH"

# Expose the application port
EXPOSE 8081

# Run the application using uvicorn
CMD ["uvicorn", "propertfinder_api.app:app", "--host", "0.0.0.0", "--port", "8081"]
