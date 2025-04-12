# Load-Balanced URL Shortener using Docker & Kubernetes

## Description
This project implements a highly scalable and fault-tolerant URL shortener application. It employs Docker containers and Kubernetes for load balancing and orchestration, ensuring seamless scalability and reliability.

### Key Features
- **URL Shortening**: Convert long URLs into short, shareable links.
- **Load Balancing**: Distributes traffic across multiple instances for high availability.
- **Dockerized Services**: Each component is containerized for ease of deployment.
- **Kubernetes Orchestration**: Automates deployment, scaling, and management of containerized applications.

---

## Project Structure
The repository contains the following key components:
- **Backend**: Python-based service to handle URL shortening logic.
- **Frontend**: Basic interface (using JavaScript and CSS) for users to interact with.
- **Load Balancer**: Ensures even distribution of traffic.
- **Deployment Scripts**: Shell and PowerShell scripts for setting up the environment.

---

## Prerequisites
1. Install **Docker**: [Get Docker](https://www.docker.com/get-started)
2. Install **Kubernetes**: [Kubernetes Installation Guide](https://kubernetes.io/docs/setup/)
3. Python environment for local testing.

---

## Installation
### Step 1: Clone the Repository
```bash
git clone https://github.com/shreyasrini04/536_678_696_712_Load-Balanced-URL-Shortener-using-Docker-Kubernetes.git
cd 536_678_696_712_Load-Balanced-URL-Shortener-using-Docker-Kubernetes
```

### Step 2: Build Docker Images and pip installations 
```bash
pip install -r requirements.txt
docker-compose up
```

### Step 3: Deploy with Kubernetes
```bash
kubectl apply -f k8s/redis-deployment.yaml
kubectl apply -f k8s/redis-service.yaml
kubectl apply -f k8s/url-shortener-deployment.yaml
kubectl apply -f k8s/url-shortener-service.yaml
```

---

## Usage
1. Access the frontend via the load balancer's external IP.
2. Enter a URL to shorten it and receive a short link.
3. Use the short link to redirect to the original URL.

---

