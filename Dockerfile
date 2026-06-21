FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml README.md ./
COPY src/ src/

RUN pip install --no-cache-dir -e ".[dev]"

EXPOSE 8000

CMD ["python", "scripts/run_api.py", "--host", "0.0.0.0", "--port", "8000"]
