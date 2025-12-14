pipeline {
    agent any
    
    environment {
        APP_NAME = 'password-app'
    }
    
    stages {
        stage('Checkout from Git') {
            steps {
                echo "=== CLONING CODE FROM GIT ==="
                // Код уже скачан автоматически
                sh 'ls -la'
            }
        }
        
        stage('Build Docker Image') {
            steps {
                sh '''
                    echo "=== BUILDING DOCKER IMAGE ==="
                    echo "Using ACTUAL files from Git repository:"
                    echo "- Dockerfile"
                    echo "- app.py (REAL password generator)"
                    echo "- build.sh"
                    echo ""
                    chmod +x build.sh
                    ./build.sh ${APP_NAME} ${BUILD_NUMBER}
                '''
            }
        }
        
        stage('Test Real Application') {
            steps {
                sh '''
                    echo "=== TESTING REAL APPLICATION ==="
                    echo "Running ACTUAL password generator..."
                    docker run --rm ${APP_NAME}:${BUILD_NUMBER}
                '''
            }
        }
        
        stage('Verify Files in Image') {
            steps {
                sh '''
                    echo "=== VERIFYING FILES IN IMAGE ==="
                    echo "1. Checking files inside container:"
                    docker run --rm ${APP_NAME}:${BUILD_NUMBER} ls -la /app
                    echo ""
                    echo "2. Checking app.py content:"
                    docker run --rm ${APP_NAME}:${BUILD_NUMBER} head -20 /app/app.py
                '''
            }
        }
    }
    
    post {
        success {
            echo '''
            ============================================
            ✅ CI/CD PROCESS COMPLETED SUCCESSFULLY!
            ============================================
            
            WHAT WAS DEMONSTRATED:
            1. ✅ Real code pulled from Git repository
            2. ✅ Docker image built from ACTUAL application
            3. ✅ Real password generator application runs
            4. ✅ Full CI/CD automation via Jenkins
            
            FILES FROM GIT REPOSITORY:
            - Dockerfile
            - app.py (real Python application)
            - build.sh (build script)
            - Jenkinsfile (this pipeline)
            
            ============================================
            '''
            
            sh '''
                echo ""
                echo "=== DOCKER IMAGES CREATED ==="
                docker images ${APP_NAME} --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedSince}}"
            '''
        }
        failure {
            echo '❌ Build failed'
        }
    }
}
