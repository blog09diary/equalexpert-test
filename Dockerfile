# ---------- Build stage ----------
FROM python:3.11-slim AS builder

# Set workdir
WORKDIR /app

# Install build tools (only in builder stage)
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy only requirements first (better caching)
COPY requirements.txt .

# Create venv and install dependencies
RUN python -m venv /venv && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir -r requirements.txt

# ---------- Final stage ----------
FROM python:3.11-slim

WORKDIR /app

# Copy virtualenv from builder
COPY --from=builder /venv /venv

# Use venv as default python/pip
ENV PATH="/venv/bin:$PATH"

# Copy only app source code
COPY . .

# Create non-root user
RUN useradd -m appuser
USER appuser

EXPOSE 8080

# Use app_entry as the entry point for Uvicorn
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8080"]