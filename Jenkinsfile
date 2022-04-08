pipeline {
  environment {
    imagename = "deepdockerpro/my_calculator"
    registryCredential = 'deepdockerpro-dockerhub'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://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@github.com/deeplearn-optimizer/calculator.git', branch: 'master', credentialsId: 'deepdockerpro-github'])

      }
    }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker.withRegistry( '', registryCredential ) {
             dockerImage.push('latest')
          }
        }
      }
    }
    stage('Remove Unused docker image') {
      steps{
         sh "docker rmi $imagename:latest"
      }
    }

    stage("Invoke ansible playbook") {
      steps{
      ansiblePlaybook(
        inventory: "Inventory",
        installation: "ansible",
        limit: "",
        playbook: "docker_playbook.yaml",
        extras: ""
      )
    }
    }

  }
}