FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY pyproject.toml .
COPY README.md .
COPY src/ src/

# Install Python dependencies
RUN pip install --no-cache-dir .

# Use PORT environment variable
ENV PORT 8080
EXPOSE ${PORT}

# Run the application
CMD ["python", "src/app.py"] 
