# Fase de resolución de dependencias
FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

# Fase de ejecución
FROM python:3.10-slim

WORKDIR /app

COPY --from=builder /app /app

COPY . .

# Instala Flask
RUN pip install Flask
RUN pip install pymongo

CMD ["python3", "app.py"]