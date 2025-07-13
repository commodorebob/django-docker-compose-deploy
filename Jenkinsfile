pipeline {
    agent any

    environment {
        ImageRegistry = "commodorebob"
        EC2_IP = '34.238.255.105'
        DockerComposeFile = 'docker-compose-deploy.yml'
        DetEnvFile = '.env.prod'
    }

    stages {
        stage('Deploy to EC2') {
            steps {
                script {
                    echo "Deploying to EC2 Instance"
                    bat '''
                    @echo off
                    icacls "C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem" /inheritance:r /grant:r "SYSTEM:F"

                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "sudo rm -rf ~/django-docker-compose-deploy || true"
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "git clone https://github.com/commodorebob/django-docker-compose-deploy.git"
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "cd ~/django-docker-compose-deploy && cp .env.prod .env"
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "cd ~/django-docker-compose-deploy && sudo docker-compose -f docker-compose-deploy.yml down || true"
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "cd ~/django-docker-compose-deploy && sudo docker-compose -f docker-compose-deploy.yml build --no-cache"
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "cd ~/django-docker-compose-deploy && sudo docker-compose -f docker-compose-deploy.yml up -d"
                    echo "Checking deployment status..."
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "cd ~/django-docker-compose-deploy && sudo docker-compose -f docker-compose-deploy.yml ps"
                    echo "Checking application logs..."
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\django-server-key-jenkins.pem ec2-user@%EC2_IP% "cd ~/django-docker-compose-deploy && sudo docker-compose -f docker-compose-deploy.yml logs app"
                    '''
                }
            }
        }
    }
}