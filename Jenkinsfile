def IMAGE_VERSION

pipeline {
  agent {
    node {
      label 'Jenkins'
    }

  }
  stages {
    stage('Build') {
      steps {
        sh '''#!/bin/bash

# Specify the version number for the image
IMAGE_VERSION='1.0'

docker build -t lawaladekunle/thedemo-flaskapp:v${IMAGE_VERSION} .

'''
      }
    }
    stage('Push Image') {
      steps {
          withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWORD', variable: 'DockerHubPassword')]) {

    sh "docker login -u lawaladekunle -p ${DockerHubPassword}"

  }

    script {
      
      IMAGE_VERSION="1.0"

      sh "docker push lawaladekunle/thedemo-flaskapp:v${IMAGE_VERSION}"
      
      }
    

      }

    }

    stage('Deploy to Kubernetes') {

      steps {

          sh "kubectl version"

      }

    }

  }

}
