pipeline {
    agent any
    
    environment {
        APP_NAME = 'password-app'
    }
    
    stages {
        stage('Prepare') {
            steps {
                sh '''
                    echo "=== PREPARING BUILD ==="
                    echo "Current directory:"
                    pwd
                    echo ""
                    echo "Files from Git:"
                    ls -la
                    echo ""
                    echo "Checking file permissions..."
                    ls -la *.sh || echo "No .sh files"
                '''
            }
        }
        
        stage('Fix Build Script') {
            steps {
                sh '''
                    echo "=== FIXING BUILD SCRIPT ==="
                    echo "Current build.sh content (first 5 lines):"
                    head -5 build.sh || echo "Cannot read build.sh"
                    echo ""
                    echo "Converting build.sh for Linux..."
                    # Удаляем Windows символы конца строки если есть
                    sed -i 's/\\r$//' build.sh
                    # Проверяем результат
                    echo "First line of build.sh after fix:"
                    head -1 build.sh
                    echo ""
                    echo "Making build.sh executable..."
                    chmod 755 build.sh
                    ls -la build.sh
                '''
            }
        }
        
        stage('Execute Build Script') {
            steps {
                sh '''
                    echo "=== EXECUTING BUILD SCRIPT ==="
                    echo "Testing if build.sh is executable..."
                    if [ -x "./build.sh" ]; then
                        echo "✅ build.sh is executable"
                        echo "Running build script..."
                        ./build.sh ${APP_NAME} ${BUILD_NUMBER}
                    else
                        echo "❌ build.sh is NOT executable"
                        echo "Trying alternative method..."
                        sh build.sh ${APP_NAME} ${BUILD_NUMBER}
                    fi
                '''
            }
        }
        
        stage('Test Application') {
            steps {
                sh '''
                    echo "=== TESTING APPLICATION ==="
                    echo "Running the built Docker image..."
                    docker run --rm ${APP_NAME}:${BUILD_NUMBER}
                    echo ""
                    echo "✅ Application test completed!"
                '''
            }
        }
    }
    
    post {
        success {
            echo '''
            ============================================
            ✅ CI/CD WITH BUILD SCRIPT - SUCCESS!
            ============================================
            
            COMPONENTS DEMONSTRATED:
            1. Git repository with all files
            2. Build script (build.sh) for automation
            3. Dockerfile for image creation
            4. Jenkins CI/CD pipeline
            5. Full automated process
            
            FILES USED:
            - Dockerfile (image configuration)
            - app.py (Python application)
            - build.sh (build automation script)
            - Jenkinsfile (CI/CD pipeline)
            
            PROCESS:
            ✓ Code in Git repository
            ✓ Jenkins triggers build automatically
            ✓ Build script executes build steps
            ✓ Docker image created
            ✓ Application tested
            
            ============================================
            '''
            
            sh '''
                echo ""
                echo "=== FINAL RESULTS ==="
                echo "Docker images:"
                docker images ${APP_NAME} --format "table {{.Repository}}\t{{.Tag}}\t{{.Size}}\t{{.CreatedAt}}"
                echo ""
                echo "Build script executed successfully!"
            '''
        }
        failure {
            echo '❌ Build failed'
            sh '''
                echo "Debug information:"
                echo "Files in workspace:"
                ls -la
                echo ""
                echo "build.sh content (first 10 lines):"
                head -10 build.sh || echo "Cannot read build.sh"
                echo ""
                echo "File type:"
                file build.sh || echo "Cannot check file type"
            '''
        }
    }
}
