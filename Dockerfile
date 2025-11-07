FROM python:3.10-slim

# Install ffmpeg (for video/audio)
RUN apt-get update && apt-get install -y --no-install-recommends ffmpeg && rm -rf /var/lib/apt/lists/*

# Working directory
WORKDIR /app

# Copy dependencies
COPY requirements.txt .

# Install Python packages (lightweight)
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . /app

# Expose FastAPI port
EXPOSE 8080

# Start bot + API
CMD ["python", "main.py"]
