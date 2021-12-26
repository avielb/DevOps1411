properties([pipelineTriggers([pollSCM('* * * * *')])])
node {
    stage("clone"){
       checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/avielb/DevOps1411.git']]]) 
    }
    stage("show files"){
        sh "ls -l"
    }
}
