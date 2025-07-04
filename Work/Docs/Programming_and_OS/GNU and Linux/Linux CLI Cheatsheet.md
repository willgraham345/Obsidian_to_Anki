---
type: cheatsheet
functions: 
date created: Friday, September 13th 2024, 3:08:29 pm
date modified: Friday, February 7th 2025, 4:04:26 pm
tags: [command/linux, command/linux/edit, command/linux/files, command/linux/networking, command/linux/permissions, command/linux/process, command/linux/searching, command/linux/variables, note/linux]
---


| Make/CMake                            | Description                                                                       |
| ------------------------------------- | --------------------------------------------------------------------------------- |
| `make`                                | Build the project according to the `Makefile`.                                    |
| `make target`                         | Build a specific target (e.g., `make all`, `make clean`).                         |
| `make -jN`                            | Build using `N` parallel jobs (e.g., `make -j4`).                                 |
| `make -f FILE`                        | Specify an alternate `Makefile` (e.g., `make -f MyMakefile`).                     |
| `make -C DIR`                         | Change to directory `DIR` before running the `Makefile`.                          |
| `make -n`                             | Show what would be done without actually doing it (dry run).                      |
| `make -k`                             | Continue as much as possible after an error.                                      |
| `make -s`                             | Silent mode; suppress command output.                                             |
| `make clean`                          | Remove build artifacts (files specified in `clean` target).                       |
| `cmake .`                             | Generate build files in the current directory.                                    |
| `cmake -Bbuild -H.`                   | Generate build files in the `build` directory.                                    |
| `cmake --build build`                 | Build the project using the files in the `build` directory.                       |
| `cmake --build build --target TARGET` | Build a specific target (e.g., `cmake --build build --target all`).               |
| `cmake -G GENERATOR`                  | Specify a generator for the build system (e.g., `cmake -G "Unix Makefiles"`).     |
| `cmake -DVAR=VALUE`                   | Define a variable for configuration (e.g., `cmake -DCMAKE_BUILD_TYPE=Release`).   |
| `cmake --version`                     | Show the CMake version.                                                           |
| `cmake --help`                        | Show help information.                                                            |
| `cmake ..`                            | Configure a build from a parent directory (often used with out-of-source builds). |

| **System**                    | **Description**                                        |
| ----------------------------- | ------------------------------------------------------ |
| `systemctl status`            | Display the status of a system or service              |
| `systemctl start <service>`   | Start a service                                        |
| `systemctl stop <service>`    | Stop a service                                         |
| `systemctl restart <service>` | Restart a service                                      |
| `systemctl reload <service>`  | Reload configuration for a service without stopping it |



- [p] `make` = Build the project according to the `Makefile`. = #command/linux
<!--ID: 1751434090903-->

- [p] `make target` = Build a specific target (e.g., `make all`, `make clean`). = #command/linux
<!--ID: 1751434090907-->

- [p] `make -jN` = Build using `N` parallel jobs (e.g., `make -j4`). = #command/linux
<!--ID: 1751434090910-->

- [p] `make -f FILE` = Specify an alternate `Makefile` (e.g., `make -f MyMakefile`). = #command/linux
<!--ID: 1751434090914-->

- [p] `make -C DIR` = Change to directory `DIR` before running the `Makefile`. = #command/linux
<!--ID: 1751434090918-->

- [p] `make -n` = Show what would be done without actually doing it (dry run). = #command/linux
<!--ID: 1751434090922-->

- [p] `make -k` = Continue as much as possible after an error. = #command/linux
<!--ID: 1751434090926-->

- [p] `make -s` = Silent mode; suppress command output. = #command/linux
<!--ID: 1751434090930-->

- [p] `make clean` = Remove build artifacts (files specified in `clean` target). = #command/linux
<!--ID: 1751434090934-->

- [p] `cmake .` = Generate build files in the current directory. = #command/linux
<!--ID: 1751434090939-->

- [p] `cmake -Bbuild -H.` = Generate build files in the `build` directory. = #command/linux
<!--ID: 1751434090944-->

- [p] `cmake --build build` = Build the project using the files in the `build` directory. = #command/linux
<!--ID: 1751434090948-->

- [p] `cmake --build build --target TARGET` = Build a specific target (e.g., `cmake --build build --target all`). = #command/linux
<!--ID: 1751434090952-->

- [p] `cmake -G GENERATOR` = Specify a generator for the build system (e.g., `cmake -G "Unix Makefiles"`). = #command/linux
<!--ID: 1751434090956-->

- [p] `cmake -DVAR<equalSign>VALUE` = Define a variable for configuration (e.g., `cmake -DCMAKE_BUILD_TYPE=Release`). = #command/linux 
<!--ID: 1751434090960-->

- [p] `cmake --version` = Show the CMake version. = #command/linux
<!--ID: 1751434090964-->

- [p] `cmake --help` = Show help information. = #command/linux
<!--ID: 1751434090969-->

- [p] `cmake ..` = Configure a build from a parent directory (often used with out-of-source builds). = #command/linux
<!--ID: 1751434090973-->

- [p] `systemctl status` = Display the status of a system or service = #command/linux/process 
<!--ID: 1751434090977-->

- [p] `systemctl start <service>` = Start a service = #command/linux/process 
<!--ID: 1751434090981-->

- [p] `systemctl stop <service>` = Stop a service = #command/linux/process 
<!--ID: 1751434090985-->

- [p] `systemctl restart <service>` = Restart a service = #command/linux/process 
<!--ID: 1751434090989-->

- [p] `systemctl reload <service>` = Reload configuration for a service without stopping it = #command/linux/process 
<!--ID: 1751434090993-->

- [p] `uname` = Display basic info about the system = #command/linux = `-a` All available info
<!--ID: 1751434090997-->

      `-r` Kernel release version
      `-n`Network node nost name
      `-m` System architecture
      `-o` Operating system
- [p] `touch <file>` = Create a new empty file or update the timestamp of an existing file. = #command/linux
<!--ID: 1751434091000-->

- [p] `chmod <permissionsOwner><permissionGroup><permissionOthers> <file>` = Change the permissions of a file or directory. = #command/linux/permissions = permissions:`7rwx, 6rw, 5rx, 4r, 3wx, 2w,1x,0(nothing)`
<!--ID: 1751434091004-->

- [p] `chown <user>:<group> <file>` = Change the owner and group of a file or directory. = #command/linux/permissions
<!--ID: 1751434091012-->

- [p] `df -h` = Show the disk space usage in a human-readable format. = #command/linux/files 
<!--ID: 1751434091018-->

- [p] `du -h <directory>` = Show the disk usage of a directory and its contents in a human-readable format. = #command/linux/files 
<!--ID: 1751434091022-->

- [p] `ps aux` = Display information about all running processes. = #command/linux/process 
<!--ID: 1751434091027-->

- [p] `kill <pid>` = Terminate a process by its process ID (`pid`). = #command/linux/process 
<!--ID: 1751434091031-->

- [p] `grep <pattern> <file>` = Search for a pattern within a file or files. = #command/linux/searching 
<!--ID: 1751434091035-->

- [p] `find <directory> -name <filename>` = Search for a file by name within a directory and its subdirectories. = #command/linux/searching 
<!--ID: 1751434091039-->

- [p] `tar -czvf <archive_name>.tar.gz <directory>` = Create a compressed archive of a directory. = #command/linux/files 
<!--ID: 1751434091043-->

- [p] `tar -xzvf <archive_name>.tar.gz` = Extract a compressed archive. = #command/linux/files
<!--ID: 1751434091047-->

- [p] `wget <url>` = Download a file from the internet using its URL. = #command/linux/networking 
<!--ID: 1751434091052-->

- [p] `curl <url>` = Transfer data from or to a server, often used for making HTTP requests. = #command/linux/networking 
<!--ID: 1751434091057-->

- [p] `ssh <user>@<host>` = Connect to a remote server via SSH. = #command/linux/networking 
<!--ID: 1751434091061-->

- [p] `scp <file> <user>@<host>:<destination>` = Copy a file to a remote server using SSH. = #command/linux
<!--ID: 1751434091064-->

- [p] `top` = Display a real-time view of running processes and system resource usage. = #command/linux/process
<!--ID: 1751434091068-->

- [p] `htop` = An enhanced version of `top`, providing a more user-friendly interface. = #command/linux/process
<!--ID: 1751434091072-->

- [p] `nano <file>` = Open and edit a file using the `nano` text editor. = #command/linux/edit
<!--ID: 1751434091077-->

- [p] `vim <file>` = Open and edit a file using the `vim` text editor. = #command/linux/edit 
<!--ID: 1751434091081-->

- [p] `alias <alias_name>` = Print alias value = #command/linux/variables
<!--ID: 1751434091085-->

- [p] `unalias <alias_name>` = Remove an alias. = #command/linux/variables 
<!--ID: 1751434091089-->

  - [p] `ag <pattern>` = Searches for patterns within a file = #command/linux/searching  = `--depth NUM` Search up to Num directories deep
        `-g` print filenames who have the pattern within them