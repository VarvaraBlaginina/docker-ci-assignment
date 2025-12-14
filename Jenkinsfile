pipeline {
    agent any
    
    environment {
        APP_NAME = 'password-app'
    }
    
    stages {
        stage('Prepare Files') {
            steps {
                script {
                    writeFile file: 'Dockerfile', text: '''FROM python:3.9-alpine
WORKDIR /app
COPY . .
CMD ["python", "app.py"]'''
                    
                    writeFile file: 'app.py', text: '''print("Hello from Docker CI/CD!")
print("This would be your password generator app")'''
                    
                    writeFile file: 'build.sh', text: '''#!/bin/bash
echo "Building $1:$2"
docker build -t $1:$2 .
echo "Done!"'''
                    
                    sh 'chmod +x build.sh'
                }
            }
        }
        
        stage('Build Image') {
            steps {
                sh './build.sh ${APP_NAME} ${BUILD_NUMBER}'
            }
        }
        
        stage('Test') {
            steps {
                sh '''
                    docker run --rm ${APP_NAME}:${BUILD_NUMBER}
                    echo "✅ CI/CD works!"
                '''
            }
        }
    }
}