#!/bin/bash

# Stop the running container
docker stop docker-container

# Remove the existing container
docker rm docker-container

# Pull the latest changes from the Git repository
git pull 

# Build the Docker image
docker build -t fastapi .

# Run a new container with the updated image
docker run -d -p 8081:8081 --name docker-container fastapi

# Clean up unused Docker images and containers
docker system prune -af
