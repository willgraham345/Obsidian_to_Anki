---
type: note/system
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Wednesday, March 4th 2026, 1:17:10 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 Jenkins ;;; Open source server that runs CI/CD pipelines. Written in Java, runs only on Java.

# Additional Background
## Concepts of Note
Build Pipeline steps
1. Test code 
2. Build application
3. Push repos
4. Deploy to server

`${env}` and `${env.*}` variables
- Environment variables set throughout pipeline, typically through the `environment { }` codeblock.
- Common

## Examples

```groovy
pipeline {
    agent any  // where to run (any node, docker, specific label)

    stages {
        stage('Build') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }
    }

    post {
        always { echo 'Done' }
        failure { echo 'Failed!' }
    }
}
```

### Common Environment Built-ins
```groovy
env.BUILD_NUMBER    // "42"
env.JOB_NAME        // "my-pipeline"
env.BRANCH_NAME     // "main" (for multibranch pipelines)
env.WORKSPACE       // "/var/jenkins/workspace/my-pipeline"
env.BUILD_URL       // full URL to this build
env.GIT_COMMIT      // current commit SHA
```