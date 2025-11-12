# ====== Base Image ======
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirement file
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose Streamlit default port
EXPOSE 8501

# Default command (can be overridden in docker-compose)
CMD ["python", "src/paris_chatbot.py"]