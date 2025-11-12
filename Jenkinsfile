pipeline {
    agent any

    environment {
        DOCKERHUB_USER = "ashunairr"
        IMAGE_NAME = "flask-clock"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER .'
            }
        }

        stage('Login to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub_pass',
                                                  usernameVariable: 'DOCKER_USER',
                                                  passwordVariable: 'DOCKER_PASS')]) {
                    sh 'echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin'
                }
            }
        }

        stage('Push Image') {
            steps {
                sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                sh '''
                kubectl set image deployment/clock-deploy \
                clock-container=$DOCKERHUB_USER/$IMAGE_NAME:$BUILD_NUMBER --record
                '''
            }
        }
    }
}
