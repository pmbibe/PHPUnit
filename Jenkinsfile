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
        sh "whoami"
        sh "su -"
        sh "whoami"
      }
    }
    stage('Test') {
      steps {
        echo "--------------------Test Stage---------------------"
        sh "phpunit --bootstrap autoload.php --log-junit report.xml EmailTest"
        junit '*.xml'
        
      }
    }
    stage('Deploy') {
      steps {
        echo "--------------------Deploy Stage---------------------"
        sh "chmod +x PHPUnit/Deploy.sh"
        sh "PHPUnit/Deploy.sh"
      }
    }
  }
}
