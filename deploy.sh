#!/bin/bash
# Stop and remove the existing containers (you may use docker-compose down for this)
docker-compose down

# Pull the latest changes from the Git repository
git pull

# Build the Docker image
docker-compose build

# Run a new container with the updated image
docker-compose up -d # The -d flag runs the container in detached/background mode
