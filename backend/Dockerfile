FROM python:3.13-slim

ARG GITHUB_TOKEN

WORKDIR /app

# Install uv
RUN pip install --no-cache-dir uv

# Install dependencies
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen

# Cope source code
COPY ./src .

# Run FastAPI/FastStream app
CMD ["uv", "run", "app.py"]
