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
	withDockerRegistry([usernamePassword( credentialsId: 'DOCKER_LOGIN_PASSWD', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD') url: 'https://index.docker.io/v2/']) {

 sh '''#!/bin/bash

# Specify the version number for the image
image_version=1.0

docker login -u "${USERNAME}" -p "${PASSWORD}"
docker push thedemo-flaskapp:v${image_version}

'''
	    
        }
      }

    }

  }

}
