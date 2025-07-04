---
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, November 15th 2024, 3:13:49 pm
type: note
---
# Background
- Configuration file for the devcontainer, similar to the `launch.json` file.
- 

# Usage
## Simple Example of a pre-built Development Container Image

```json
{
  "image": "mcr.microsoft.com/devcontainers/typescript-node",
  "forwardPorts": [3000],
  "customizations": {
    // Configure properties specific to VS Code.
    "vscode": {
      // Add the IDs of extensions you want installed when the container is created.
      "extensions": ["streetsidesoftware.code-spell-checker"]
    }
  }
}
```

## Creating a Dev Container
[Create a Dev Container](https://code.visualstudio.com/docs/devcontainers/create-dev-container)

## Pre-building dev container images
Using pre-built images will result in a faster container startup, simpler configuration, and allows you to pin a specific version of tools to improve supply-chain security and avoid potential breaks. 
