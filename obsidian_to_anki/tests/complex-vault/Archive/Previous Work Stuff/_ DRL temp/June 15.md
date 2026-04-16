# Notes
Have had issues running cfclient, and connecting to the crazyflies. . No idea what caused that. 

## Running cfclient
![[Pasted image 20240615121058.png | 700]]
- When I run `sudo apt install libxcb-xinerama0` I get it saying that it's already installed. 

People describing similar issues:
- https://github.com/yaml/pyyaml/issues/724

Was able to get through it, see Jira bugs. 

## Issues with Buildling
Apparently ROS needs `setuptools==58.2.0`. See [this thread](https://answers.ros.org/question/396439/setuptoolsdeprecationwarning-setuppy-install-is-deprecated-use-build-and-pip-and-other-standards-based-tools/)


## Debugging the Launch file
### `lighthouse_config_file` not initialized