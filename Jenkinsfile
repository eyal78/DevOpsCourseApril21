pipeline {
  agent any

  stages {
        stage('Build fantastic ascii'){
            steps {
                sh '''
                cd package_demo
                python setup.py sdist bdist_wheel
                '''
            }
        }

        stage('Publish fantastic ascii'){
            steps {
                rtServer (
                    id: 'Artifactory-1',
                    url: 'https://devopsmar22.jfrog.io/artifactory',
                    credentialsId: 'jfrog'
                )

                rtUpload (
                    serverId: 'Artifactory-1',
                    spec: '''{
                          "files": [
                            {
                              "pattern": "package_demo/dist/",
                              "target": "internal-pypi/"
                            }
                         ]
                    }'''
                )
            }
        }
//
//         stage('Load Artifact - dev') {
//             when { anyOf {branch "dev"} }
//             steps {
//                 copyArtifacts filter: 'infra/dev/terraform.tfstate', projectName: '${JOB_NAME}'
//             }
//         }
//
//         stage('Load Artifact - prod') {
//             when { anyOf {branch "master"} }
//             steps {
//                 copyArtifacts filter: 'infra/prod/terraform.tfstate', projectName: '${JOB_NAME}'
//             }
//         }
//
//         stage('Terraform Init & Plan'){
//             when { anyOf {branch "master";branch "dev";changeRequest()} }
//             steps {
//                 sh '''
//                 if [ "$BRANCH_NAME" = "master" ] || [ "$CHANGE_TARGET" = "master" ]; then
//                     cd infra/prod
//                 else
//                     cd infra/dev
//                 fi
//                 echo ${JOB_NAME}
//                 terraform init
//                 terraform plan
//                 '''
//             }
//         }
//
//         stage('Terraform Apply - dev'){
//             when { anyOf {branch "dev"} }
//             steps {
//                 sh '''
//                 cd infra/dev
//                 terraform apply -auto-approve
//                 '''
//                 archiveArtifacts artifacts: 'infra/dev/terraform.tfstate', onlyIfSuccessful: true
//             }
//         }
//
//         stage('Terraform Apply - prod'){
//             when { anyOf {branch "master"}; }
//             input {
//                 message "Do you want to proceed for infrastructure provisioning?"
//             }
//             steps {
//                 sh '''
//                 cd infra/prod
//                 terraform apply -auto-approve
//                 '''
//                 archiveArtifacts artifacts: 'infra/prod/terraform.tfstate', onlyIfSuccessful: true
//             }
//         }
  }
}


