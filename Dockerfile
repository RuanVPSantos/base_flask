# Use Python base image
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY ./app /app/app
COPY .env.prod /app/.env

# Expose port
EXPOSE 5000

# Start application
CMD ["python", "app/main.py"]
