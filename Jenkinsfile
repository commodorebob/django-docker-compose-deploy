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

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-login', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
                    script {
                        echo "Pushing Docker Image to Docker Hub"
                        bat '''
                        @echo off
                        echo Logging into Docker Hub...
                        echo %PASS% | docker login -u %USER% --password-stdin
                        docker push %ImageRegistry%/%JOB_NAME%:%BUILD_NUMBER%
                        '''
                    }
                }
            }
        }

        stage('Deploy to EC2') {
            steps {
                script {
                    echo "Deploying to EC2 Instance"
                    bat '''
                    @echo off
                    scp -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\jenkins-key.pem docker-compose-deploy.yml ec2-user@%EC2_IP%:~/docker-compose-deploy.yml
                    scp -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\jenkins-key.pem .env.prod ec2-user@%EC2_IP%:~/.env.prod
                    ssh -o StrictHostKeyChecking=no -i C:\\Users\\commo\\Downloads\\jenkins-key.pem ec2-user@%EC2_IP% "docker-compose -f ~/docker-compose-deploy.yml --env-file ~/.env.prod pull && docker-compose -f ~/docker-compose-deploy.yml --env-file ~/.env.prod up -d"
                    '''
                }
            }
        }
    }
}