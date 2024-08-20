#!/bin/bash
echo "+-------------------------------------------------------------+"
echo "|                                                             |"
echo "|                    Install Docker                           |"
echo "|                                                             |"
echo "+-------------------------------------------------------------+"

# Update the apt package index
sudo apt-get update
sudo apt install unzip

# Install packages to allow apt to use a repository over HTTPS
sudo apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Set up the stable repository
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update the apt package index again
sudo apt-get update

# Install Docker Engine
sudo apt-get install -y docker-ce docker-ce-cli containerd.io

# Add the current user to the docker group to run Docker without sudo
sudo usermod -aG docker $USER


cd /opt
sudo unzip flasjournal.zip

docker build -t flask-journal-pilot .
docker tag flask-journal-pilot:latest ritvikdocker/flask-journal-pilot:latest

echo "docker run -p 8080:5000 -e PORT=5000 -e OPENAI_API_KEY=YOUR_API_KEY ritvikdocker/flask-journal-pilot"

# docker run -d -p 8081:5000 --env-file .env --platform linux/amd64 ritvikdocker/flask-blog-post-generator