def VERSION

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
VERSION=1

docker build -t thedemo-flaskapp:v${VERSION} .

'''
      }
    }
    stage('Upload Image') {
      steps {
	withDockerRegistry(credentialsId: 'DOCKER_LOGIN_PASSWD', url: 'https://index.docker.io/v2/') {
        echo $VERSION

	docker login
        
        }
      }

    }
  }
}
