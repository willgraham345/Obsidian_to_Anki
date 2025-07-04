---
type: note
tags: note/git
---
[Workflow Syntax for GitHub Actions](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#about-yaml-syntax-for-workflows)

Uses YAML syntax.

# Naming
## `name`
- Name of the workflow. Names your workflows under your repositories "Actions" tab
## `run-name`
- Name for workflow runs generated from the workflow. 
```yaml
run-name: Deploy to ${{ inputs.deploy_target }} by @${{ github.actor }}
```

## `on`
- To trigger a workflow, use this. 
- [Events that trigger workflows](https://docs.github.com/en/actions/using-workflows/events-that-trigger-workflows)
```yaml
on: push
on: [push, fork]

on: 
	push:
		branches:
			- main
			- 'releases/**'
```
- You can also use activity types (some events have these). You can also use filters

## `defaults`
- Creates a map of default settings that will apply to all jobs in the workflow. 

### `defeaults.run`
- You can use this to provide default `shell` and `working-directory` options for all run steps in a workflow. You can also set default settings for run that are only available to a job. 
```yaml
defaults:
  run:
    shell: bash
    working-directory: ./scripts
```
# Jobs
## `jobs
- A workflow is made up of one or more jobs, which run in parallel by default. To run jobs sequentially, you need to define dependencies on other jobs using the `jobs.<job_id>.needs` (see [[#`jobs.<job_id>`]]) keyword.
- Each job runs in a runner environment specified by `runs-on`

### `jobs.<job_id>`
- Gives your job a unique identifier. The `job_id` is a string unique to the `jobs` object. 
```yaml
jobs:
  my_first_job:
    name: My first job
  my_second_job:
    name: My second job
```
#### `jobs.<job_id>.runs-on`
- Defines the type of machine to run on
- You can provide `runs-on` as:    
    - a single string
    - a single variable containing a string
    - an array of strings, variables containing strings, or a combination of both
    - a `key: value` pair using the `group` or `labels` keys
- If you specify an array of strings or variables, your workflow will execute on any runner that matches all of the specified `runs-on` values. For example, here the job will only run on a self-hosted runner that has the labels `linux`, `x64`, and `gpu`:

```yaml
runs-on: [self-hosted, linux, x64, gpu]
```
#### Choosing a Github-hosted runner
|**OS (YAML workflow label)**|**Notes**|
|---|---|
|`ubuntu-latest`, `ubuntu-22.04`, `ubuntu-20.04`|The `ubuntu-latest` label currently uses the Ubuntu 22.04 runner image.|
|`windows-latest`, `windows-2022`, `windows-2019`|The `windows-latest` label currently uses the Windows 2022 runner image.|
|`macos-latest`, `macos-14` [Beta], `macos-13`, `macos-12`, `macos-11`|The `macos-latest` workflow label currently uses the macOS 12 runner image.|


#### `jobs.<job_id>.needs`
- Identify jobs that must complete before this job runs. Can be a string, or an array of strings. 
```yaml
jobs:
  job1:
  job2:
    needs: job1
  job3:
    needs: [job1, job2]
```

#### `jobs.<job_id>.if`
- Can prevent a job from running unless a condition is met. This is evaluated before the `jobs.<job_id>.strategy.matrix` is applied. 

# Steps
## `jobs.<job_id>.steps`
- A job contains a sequence of tasks called `steps`. Steps can run commands, run setup tasks, or run an action in your repository, a public repository, or an action published in a Docker registry. Not all steps run actions, but all actions run a step. Each step runs in its own process in the runner environment and has access to the workspace and filesystem. Because steps run in their own process, changes to environment variables are not preserved between steps. 
```yaml
name: Greeting from Mona
on: push

jobs:
  my-job:
    name: My Job
    runs-on: ubuntu-latest
    steps:
      - name: Print a greeting
        env:
          MY_VAR: Hi there! My name is
          FIRST_NAME: Mona
          MIDDLE_NAME: The
          LAST_NAME: Octocat
        run: |
          echo $MY_VAR $FIRST_NAME $MIDDLE_NAME $LAST_NAME.
```
## `jobs.<jobs_id>.steps[*].id`
A unique identifier for the step. 
## `jobs.<job_id>.steps[*].if`

You can use the `if` conditional to prevent a step from running unless a condition is met. You can use any supported context and expression to create a conditional. For more information on which contexts are supported in this key, see "[Contexts](https://docs.github.com/en/actions/learn-github-actions/contexts#context-availability)."

When you use expressions in an `if` conditional, you can, optionally, omit the `${{ }}` expression syntax because GitHub Actions automatically evaluates the `if` conditional as an expression. However, this exception does not apply everywhere.

You must always use the `${{ }}` expression syntax or escape with `''`, `""`, or `()` when the expression starts with `!`, since `!` is reserved notation in YAML format. For example:

```yaml
if: ${{ ! startsWith(github.ref, 'refs/tags/') }}
```


## `jobs.<job_id>.steps[*].uses`

Selects an action to run as part of a step in your job. An action is a reusable unit of code. You can use an action defined in the same repository as the workflow, a public repository, or in a [published Docker container image](https://hub.docker.com/).

We strongly recommend that you include the version of the action you are using by specifying a Git ref, SHA, or Docker tag. If you don't specify a version, it could break your workflows or cause unexpected behavior when the action owner publishes an update.

- Using the commit SHA of a released action version is the safest for stability and security.
- If the action publishes major version tags, you should expect to receive critical fixes and security patches while still retaining compatibility. Note that this behavior is at the discretion of the action's author.
- Using the default branch of an action may be convenient, but if someone releases a new major version with a breaking change, your workflow could break.

Some actions require inputs that you must set using the [`with`](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions#jobsjob_idstepswith) keyword. Review the action's README file to determine the inputs required.

Actions are either JavaScript files or Docker containers. If the action you're using is a Docker container you must run the job in a Linux environment. For more details, see `runs-on` [[#`jobs.<job_id>.runs-on`]].

### Example: Using versioned actions

```yaml
steps:
  # Reference a specific commit
  - uses: actions/checkout@8f4b7f84864484a7bf31766abe9204da3cbe65b3
  # Reference the major version of a release
  - uses: actions/checkout@v4
  # Reference a specific version
  - uses: actions/checkout@v4.2.0
  # Reference a branch
  - uses: actions/checkout@main
```

### Example: Using a public action

`{owner}/{repo}@{ref}`

You can specify a branch, ref, or SHA in a public GitHub repository.

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        # Uses the default branch of a public repository
        uses: actions/heroku@main
      - name: My second step
        # Uses a specific version tag of a public repository
        uses: actions/aws@v2.0.1
```

### Example: Using a public action in a subdirectory

`{owner}/{repo}/{path}@{ref}`

A subdirectory in a public GitHub repository at a specific branch, ref, or SHA.

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: actions/aws/ec2@main
```

### Example: Using an action in the same repository as the workflow

`./path/to/dir`

The path to the directory that contains the action in your workflow's repository. You must check out your repository before using the action.

Example repository file structure:

```shell
|-- hello-world (repository)
|   |__ .github
|       └── workflows
|           └── my-first-workflow.yml
|       └── actions
|           |__ hello-world-action
|               └── action.yml
```

The path is relative (`./`) to the default working directory (`github.workspace`, `$GITHUB_WORKSPACE`). If the action checks out the repository to a location different than the workflow, the relative path used for local actions must be updated.

Example workflow file:

```yaml
jobs:
  my_first_job:
    runs-on: ubuntu-latest
    steps:
      # This step checks out a copy of your repository.
      - name: My first step - check out repository
        uses: actions/checkout@v4
      # This step references the directory that contains the action.
      - name: Use local hello-world-action
        uses: ./.github/actions/hello-world-action
```

### Example: Using a Docker Hub action

`docker://{image}:{tag}`

A Docker image published on [Docker Hub](https://hub.docker.com/).

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://alpine:3.8
```

### Example: Using the GitHub Packages Container registry

`docker://{host}/{image}:{tag}`

A public Docker image in the GitHub Packages Container registry.

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://ghcr.io/OWNER/IMAGE_NAME
```

### Example: Using a Docker public registry action

`docker://{host}/{image}:{tag}`

A Docker image in a public registry. This example uses the Google Container Registry at `gcr.io`.

```yaml
jobs:
  my_first_job:
    steps:
      - name: My first step
        uses: docker://gcr.io/cloud-builders/gradle
```

### Example: Using an action inside a different private repository than the workflow

Your workflow must checkout the private repository and reference the action locally. Generate a personal access token and add the token as a secret. For more information, see "[Managing your personal access tokens](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)" and "[Using secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)."

Replace `PERSONAL_ACCESS_TOKEN` in the example with the name of your secret.

```yaml
jobs:
  my_first_job:
    steps:
      - name: Check out repository
        uses: actions/checkout@v4
        with:
          repository: octocat/my-private-repo
          ref: v1.0
          token: ${{ secrets.PERSONAL_ACCESS_TOKEN }}
          path: ./.github/actions/my-private-repo
      - name: Run my action
        uses: ./.github/actions/my-private-repo/my-action
```

Alternatively, use a GitHub App instead of a personal access token in order to ensure your workflow continues to run even if the personal access token owner leaves. For more information, see "[Making authenticated API requests with a GitHub App in a GitHub Actions workflow](https://docs.github.com/en/apps/creating-github-apps/guides/making-authenticated-api-requests-with-a-github-app-in-a-github-actions-workflow)."

## `jobs.<jobs_id>.steps[*].working-directory`
- A keyword that can specify where to run command
```yaml
- name: Clean temp directory
  run: rm -rf *
  working-directory: ./temp
```