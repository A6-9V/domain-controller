FROM python:3.11-slim

# Create a non-root user and group
RUN groupadd -r appgroup && useradd -r -g appgroup appuser

WORKDIR /app

# Install dependencies
# Using --chown here to set ownership during the copy process
COPY --chown=appuser:appgroup requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files and set ownership
COPY --chown=appuser:appgroup manage_cloudflare.py .

# Switch to the non-root user
USER appuser

# Keep the container running or run a specific command
CMD ["python", "manage_cloudflare.py", "--help"]
