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

echo $(whoami)

# Specify the version number for the image
VERSION=1.0

sudo docker build -t my_flask:v${VERSION} .

'''
      }
    }

  }
}
