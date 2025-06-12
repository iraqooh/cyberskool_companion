# Base image
FROM python:3.12-slim

# Environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --upgrade && pip && pip install -r requirements.txt

# Copy source code
COPY . .

# Port 
EXPOSE 8000

# Start server with Gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app:app"]