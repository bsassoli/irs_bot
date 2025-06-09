FROM python:3.10-slim

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv

WORKDIR /app

# Copy uv files first (for better caching)
COPY pyproject.toml uv.lock ./

# Install dependencies
RUN uv sync --frozen --no-cache

# Copy rest of application
COPY . .

# Expose port
EXPOSE 8000

# Run the application
CMD ["uv", "run", "python", "src/irs_bot/server.py"]
