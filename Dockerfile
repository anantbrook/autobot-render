FROM python:3.11-slim

WORKDIR /app

# Install system deps
RUN apt-get update && apt-get install -y \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Create empty __init__.py files
RUN touch scrapers/__init__.py content/__init__.py \
    affiliate/__init__.py publisher/__init__.py \
    distributor/__init__.py database/__init__.py \
    scheduler/__init__.py

CMD ["python", "main.py"]
