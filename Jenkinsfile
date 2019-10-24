//HelloWorld
pipeline {
  agent any
  
  stages {
    stage('Prepare') {
      steps {
        echo "1"
        sh "git clone https://github.com/pmbibe/PHPUnit"
      }
    }
    stage('Test') {
      steps {
        echo "2"
      }
    }
    stage('Deploy') {
      steps {
        echo "3"
      }
    }
  }
}
