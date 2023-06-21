pipeline {
    agent any
    
    stages {
        stage('Cleanup') {
            steps {
                script {
                    env.TEST_IP = "54.162.13.250"
                    env.PRODACT_IP = "3.92.212.97"
                }
                sh 'echo "Performing cleanup..."'
                sh 'rm -rf *'
            }
        }
        
        stage('Clone') {
            steps {
                sh 'echo "Cloning repository..."'
                sh 'git clone https://github.com/nedm0r/sample-flask-.git'
                sh 'ls'
            }
        }
        
        stage('Build') {
            steps {
                sh 'echo "Building..."'
                sh 'echo "Packaging..."'
                sh 'tar -czvf sampleflask.tar.gz sample-flask-'
                sh 'ls'
            }
        }
        
        stage('Upload') {
            steps {
                withCredentials([
                    [
                        $class: 'AmazonWebServicesCredentialsBinding',
                        credentialsId: 'nedm0rS3',
                        accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                        secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                    ]
                ]) {
                    sh 'aws s3 cp sampleflask.tar.gz s3://nedm0rs3'
                }
            }
        }
        
        stage('Test') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'Project-SSH', keyFileVariable: 'KEY_FILE')]) {
                    withCredentials([
                        [
                            $class: 'AmazonWebServicesCredentialsBinding',
                            credentialsId: 'nedm0rS3',
                            accessKeyVariable: 'AWS_ACCESS_KEY_ID',
                            secretKeyVariable: 'AWS_SECRET_ACCESS_KEY'
                        ]
                    ]) {
                        sshagent(['SSH_ec2']) {
                            sh """
                                scp -i \${KEY_FILE} -o StrictHostKeyChecking=no sampleflask.tar.gz ec2-user@\${TEST_IP}:/home/ec2-user/
                                ssh-keyscan \${TEST_IP} >> /var/lib/jenkins/.ssh/known_hosts
                                ssh -o StrictHostKeyChecking=no -i \${KEY_FILE} ec2-user@\${TEST_IP} '
                                    tar -xzf sampleflask.tar.gz
                                    rm -fr sampleflask.tar.gz
                                    ls
                                    bash /home/ec2-user/sample-flask-/flaskrun.sh > /dev/null 2>&1 & disown
                                '
                            """
                        }
                    }
                }
            }
        }
        
        stage('Testing Flask') {
            steps {
                withCredentials([sshUserPrivateKey(credentialsId: 'Project-SSH', keyFileVariable: 'KEY_FILE')]) {
                    sh """
                        ssh -o StrictHostKeyChecking=no -i \${KEY_FILE} ec2-user@\${TEST_IP} '
                            cd /home/ec2-user/sample-flask-
                            chmod +x test.sh
                            ./test.sh
                            sudo bash /home/ec2-user/sample-flask-/tests/tests.sh
                            sudo bash /home/ec2-user/sample-flask-/flaskstop.sh
                            exit
                            ls
                        '
                    """
                }
            }
        }
        
        stage('Deploy') {
            steps {
                    sh """
                        cd '
                            echo "Deploying to production server..."
                            # Add your deployment commands here
                        '
                    """
                }
            }
        }
    }
}
