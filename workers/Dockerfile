# Use a base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /workers

# Copy the application files to the container
COPY . /workers

# Install dependencies
RUN pip install -r requirements.txt

# Expose port 8080
EXPOSE 8081

# Set the entrypoint command
CMD ["python3", "worker.py"]