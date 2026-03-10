FROM python:3.12-slim

# Security: run as non-root
RUN useradd --create-home appuser
WORKDIR /app

# Install dependencies first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy source
COPY . .

# Drop privileges
USER appuser

EXPOSE 8000

# Uvicorn with 1 async worker (SSE requires sticky connections)
CMD ["uvicorn", "app.main:app", 
     "--host", "0.0.0.0", 
     "--port", "8000", 
     "--workers", "1", 
     "--loop", "asyncio", 
     "--access-log"]