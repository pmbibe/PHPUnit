//HelloWorld
pipeline {
  agent any
  
  stages {
    stage('Prepare') {
      steps {
        echo "--------------------Prepare Stage---------------------"
        sh "rm -rf PHPUnit"
        sh "git clone https://github.com/pmbibe/PHPUnit"
        sh "phpunit --version"
      }
    }
    stage('Test') {
      steps {
        echo "--------------------Test Stage---------------------"
        sh "phpunit --bootstrap autoload.php --log-junit report.xml  --coverage-html coverage --coverage-clover coverage.xml EmailTest"
        junit '*.xml'
        clover '*.xml'
      }
    }
    stage('Deploy') {
      steps {
        echo "--------------------Deploy Stage---------------------"
      }
    }
  }
}
