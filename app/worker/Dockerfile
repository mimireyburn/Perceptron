# Use a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the application files to the container
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8080

# Set the entrypoint command
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]