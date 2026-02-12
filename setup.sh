#!/bin/bash

# Install Jules CLI
npm install -g @google/jules

# Install Docker
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify Docker status
sudo systemctl status docker
sudo systemctl start docker

echo "Setup complete. Jules and Docker are installed."
