pipeline {
  agent any
  stages {
    stage('Start') {
      steps {
        sh '''#!/bin/bash
echo "hello world"'''
      }
    }
    stage('Sleep') {
      steps {
        sleep 5
      }
    }
    stage('Notify') {
      steps {
        mail(subject: 'BlueOcean', body: 'Test ')
      }
    }
  }
}