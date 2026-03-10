FROM python:3.12-slim

# Crea utente non-root
RUN useradd --create-home appuser
WORKDIR /app

# Installa dipendenze (layer caching + pip aggiornato)
COPY requirements.txt .
RUN python -m pip install --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.txt

# Copia il sorgente
COPY . .

# Permessi alla cartella di lavoro
RUN chown -R appuser:appuser /app

# Droppa privilegi
USER appuser

EXPOSE 8000

# Avvio Uvicorn (assume app.main:app esista davvero)
CMD ["uvicorn", "app.main:app", 
     "--host", "0.0.0.0", 
     "--port", "8000", 
     "--workers", "1", 
     "--loop", "asyncio", 
     "--access-log"]
