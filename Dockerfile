FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY manage_cloudflare.py .

# Keep the container running or run a specific command
CMD ["python", "manage_cloudflare.py", "--help"]
