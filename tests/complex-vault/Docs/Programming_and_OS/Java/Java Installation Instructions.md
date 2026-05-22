---
type: note
---
# Oracle JDK and OpenJDK
Oracle JDK
JDK is a software development environment used in Java platform programming
- Contains a complete Java Runtime Environment (JRE)

OpenJDK
Free and open-source


Performance
- No difference between the two, as the build process for Oracle JDK is based on that of OpenJDK
- Oracle's is MUCH better regarding responsiveness and JVM performance
	- Puts more focus on stability 

## Installation of Oracle
### Linux
https://www.geeksforgeeks.org/setting-environment-java/
#### Setting Default Java Version on Linux
https://phoenixnap.com/kb/install-java-ubuntu#:~:text=You%20can%20install%20one%20or,of%20the%20JRE%20and%20JDK

```
sudo update-alternatives --config java
```

#### Setting `JAVA_HOME` Environment Variable
`JAVA_HOME="/yourinstallation/path/"`

### Windows
- https://www.oracle.com/java/technologies/downloads/#jdk17-windows
	- LTS is version 17 at the moment of writing

sudo apt install oracle-java17-set-default


## Uninstall Java on Ubuntu
### Remove OpenJDK
```shell
sudo apt remove default-jdk
```