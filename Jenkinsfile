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
image_version=1.0

docker build -t thedemo-flaskapp:v${image_version} .

'''
      }
    }
    stage('Test') {
      steps {
          script {
echo  "The current image version is: ${image_version}"
        }
      }

    }
  
    stage('Login') {
      steps {
withDockerRegistry('https://index.docker.io/v2/', credentialsId: 'DOCKER_LOGIN_PASSWD') {
	    
        }
      }

    }

  }

}
