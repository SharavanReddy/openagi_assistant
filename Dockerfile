# Use Python 3.8 as base image
FROM python:3.8

# Set working directory within the container
WORKDIR /app

# Copy requirements.txt to container
COPY requirements.txt .

# Install Python dependencies
RUN pip install -r requirements.txt

# Copy all files from the current directory to container
COPY . .

# Expose port 8000 for the FastAPI app
EXPOSE 8000

# Command to start the FastAPI app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

