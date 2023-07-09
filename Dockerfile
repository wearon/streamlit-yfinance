# Use an official Python runtime as the base image
FROM python:3.8-slim-buster

# Install the system-level dependency (poppler-utils) for pdftotext
RUN apt-get update && apt-get install build-essential libpoppler-cpp-dev pkg-config python3-dev

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code into the container
COPY . .

# Expose the port that the Streamlit application will run on
EXPOSE 8501

# Set the command to run the Streamlit application
CMD ["streamlit", "run", "--server.port", "8501", "app.py"]
