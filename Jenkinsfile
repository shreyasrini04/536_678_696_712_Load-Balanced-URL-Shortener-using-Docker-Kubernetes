pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/shreyasrini04/536_678_696_712_Load-Balanced-URL-Shortener-using-Docker-Kubernetes.git'
            }
        }

        stage('Build') {
            steps {
                sh 'echo Building the application...'
                sh 'docker build -t url-shortener .'
            }
        }

        stage('Test') {
            steps {
                sh 'echo Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                sh 'echo Deploying the application...'
            }
        }
    }
}
