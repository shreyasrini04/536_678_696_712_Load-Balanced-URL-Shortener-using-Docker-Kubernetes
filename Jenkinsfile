pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'url-shortener'
    }

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning the repository...'
                git branch: 'main', url: 'https://github.com/shreyasrini04/536_678_696_712_Load-Balanced-URL-Shortener-using-Docker-Kubernetes.git'
            }
        }

        stage('Verify Docker') {
            steps {
                echo 'Checking if Docker is available...'
                sh 'docker --version || { echo "Docker is not installed or not accessible"; exit 1; }'
            }
        }

        stage('Build') {
            steps {
                echo 'Building the application...'
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
                // Add test commands here if required
            }
        }

        stage('Deploy') {
            steps {
                echo 'Deploying the application...'
                sh 'docker run -d --name url-shortener-container -p 8080:8080 $DOCKER_IMAGE'
            }
        }
    }
}
