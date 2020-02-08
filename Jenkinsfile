def image_version

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
image_version='1.0'

docker build -t thedemo-flaskapp:v${image_version} .

'''
      }
    }
    stage('Push Image') {
      steps {
          withCredentials([string(credentialsId: 'DOCKER_HUB_PASSWORD', variable: 'DockerHubPassword')]) {

    sh "docker login -u lawaladekunle -p ${DockerHubPassword}"

  }

    sh export image_version='1.0'

    sh "docker push thedemo-flaskapp:v${image_version}"

      }

    }

  }

}
