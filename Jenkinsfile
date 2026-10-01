pipeline {
    agent any

    stages {

        stage('Build Docker Image') {
            steps {
                bat '"C:\\Users\\Newst\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" build -t jenkins-ghcr-demo:latest .'
            }
        }

        stage('Tag Image for GHCR') {
            steps {
                bat '"C:\\Users\\Newst\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" tag jenkins-ghcr-demo:latest ghcr.io/codersentry/jenkins-ghcr-demo:latest'
            }
        }

        stage('Login to GHCR') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'ghcr-credentials',
                        usernameVariable: 'GHCR_USER',
                        passwordVariable: 'GHCR_PAT'
                    )
                ]) {
                    bat 'echo %GHCR_PAT%| "C:\\Users\\Newst\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" login ghcr.io -u %GHCR_USER% --password-stdin'
                }
            }
        }

        stage('Push Image to GHCR') {
            steps {
                bat '"C:\\Users\\Newst\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" push ghcr.io/codersentry/jenkins-ghcr-demo:latest'
            }
        }
    }
}