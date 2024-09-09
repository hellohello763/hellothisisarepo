


pipeline {
    // what of what you want to do with your build pipeline needs to be inside this pipeline block


    // in declaritive jenkins pipline we have statement and expression

    // no semicolon, each statement needs to be on its own line

    agent {
        node {
            label 'hello_my_computer_node'
            customWorkspace '/Users/yefeili/Downloads/hihihi'
        }
    }

    options {
        timeout(time: 30, unit: 'SECONDS')

    }

    stages {
        stage('make install, installling dependencies') {
            steps{
                // stash includes: '**', name: 'repoFiles'
                // sh 'echo hello'
                sh 'python3 -m venv hello'
                sh './bin/activate'
                sh 'pip'
                sh 'make install'
            }
            
        }

        stage('run black style check on the code base') {
            steps {
                sh 'make format'
            }
            
        }


        stage('third stage') {

            steps{
                sh 'echo zip to package all the files to result.zip'
                sh 'zip result.zip *'
            }
        }
    }

}