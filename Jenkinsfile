def tfEnv = 'dev'

pipeline {
  agent any

  stages {
        stage('Env Settings') {
            sh '''
            if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
                tfEnv='prod'
            fi
            '''
        }

        stage('Load Artifact - dev') {
            when { anyOf {branch "dev"} }
            copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
        }

        stage('Load Artifact - prod') {
            when { anyOf {branch "master"} }
            copyArtifacts filter: 'infra/prod/terraform.tfstate', projectName: '${JOB_NAME}'
        }

        stage('Terraform Init & Plan'){
            when { anyOf {branch "master";branch "dev";changeRequest()} }
            steps {
                sh '''
                cd infra/${tfEnv}
                terraform init
                terraform plan
                '''
            }
        }

        stage('Terraform Apply - dev'){
            when { anyOf {branch "dev"} }
            steps {
                sh '''
                cd infra/dev
                terraform apply
                '''
                archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
            }
        }

        stage('Terraform Apply - prod'){
            when { anyOf {branch "master"}; }
            input {
                message "Do you want to proceed for infrastructure provisioning?"
            }
            steps {
                sh '''
                cd infra/prod
                terraform apply
                '''
                archiveArtifacts artifacts: 'infra/prod/terraform.tfstate', onlyIfSuccessful: true
            }
        }

  }
}


