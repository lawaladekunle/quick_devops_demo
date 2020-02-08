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
VERSION=1.0

docker build -t my_flask:v${VERSION} .

'''
      }
    }

  }
}
