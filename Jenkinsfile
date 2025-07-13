pipeline {
    agent any

    environment {
        ImageRegistry = "commodorebob"
        EC2_IP = '34.238.255.105'
        DockerComposeFile = 'docker-compose-deploy.yml'
        DetEnvFile = '.env.prod'
    }

    stages {
        stage('buildImage') {
            steps {
                script {
                    echo "Building Docker Image"
                    powershell "docker build -t ${ImageRegistry}/${JOB_NAME}:${BUILD_NUMBER} ."
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    echo "Deploying to EC2 Instance"
                    bat '''
                    @echo off
                    icacls "C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem" /inheritance:r /grant:r "SYSTEM:F"

                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "git clone https://github.com/commodorebob/django-docker-compose-deploy.git && mv ~/django-docker-compose-deploy/.env.prod ~/django-docker-compose-deploy/.env"
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "docker-compose -f ~/django-docker-compose-deploy/docker-compose-deploy.yml up -d"
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "rm -R ~/django-docker-compose-deploy"
                    '''
                }
            }
        }
    }
}