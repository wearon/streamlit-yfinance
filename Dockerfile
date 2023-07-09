# Use an official Python runtime as the base image
FROM python:3.11

# Install system-level dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpoppler-cpp-dev \
    pkg-config \
    python3-dev \
    poppler-utils

# Install pipenv to manage Python dependencies
RUN pip install pipenv

# Set the working directory in the container
WORKDIR /app

COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

RUN pip3 install -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Streamlit application will run on
EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]