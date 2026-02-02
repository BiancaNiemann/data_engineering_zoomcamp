# Start with slim Python 3.13 image
FROM python:3.13.10-slim

# Copy uv binary from official uv image (multi-stage build pattern)
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/

# Set working directory
WORKDIR /app

# Add virtual environment to PATH so we can use installed packages
ENV PATH="/app/.venv/bin:$PATH"

# Copy dependency files first (better layer caching)
COPY "pyproject.toml" "uv.lock" ".python-version" ./
# Install dependencies from lock file (ensures reproducible builds)
RUN uv sync --locked

# Copy application code
COPY ingest_data.py ingest_data.py 
COPY ingest_zones.py ingest_zones.py
COPY ingest_parquet.py ingest_parquet.py

# Set entry point
CMD [ "python"]
# Was ENTRYPOINT [ "python", "data_ingest.py" ] but changed to CMD to allow overriding the command at runtime