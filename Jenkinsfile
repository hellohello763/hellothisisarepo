


pipeline {
    // what of what you want to do with your build pipeline needs to be inside this pipeline block


    // in declaritive jenkins pipline we have statement and expression

    // no semicolon, each statement needs to be on its own line

    agent {
        node {
            label 'any'
            customWorkspace '~/Downloads/hihihi'
        }
    }

    options {
        timeout(time: 30, unit: 'SECONDS')

    }

    stages {
        stage('first stage') {
            steps{
                sh 'echo hello'
            }
            
        }

        stage('second stage') {
            steps {
                sh 'echo hello'
            }
            
        }


        stage('third stage') {

            steps{
                sh 'echo hello'
            }
        }
    }

}