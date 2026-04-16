---
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, November 15th 2024, 3:12:14 pm
type: note
---
# Background
- 

## Useful flags
`-i` = interactive
`-t` = tty
`-t` = detached
`--rm` = remove automatically after it has exited
- Also means that `docker start` can't be used to start the container after it has exited. 

# Usage
## Run Ubuntu with a tty passing stdin to the container 
```shell
docker run -it ubuntu 
```
- Now we're inside the container, and if we press `ls` nothing will happen. This is because we're now sending messages into the container. 

Exit
```
exit
```