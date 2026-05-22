---
summary:
headings:
type: cheatsheet
functions:
date created: Friday, September 13th 2024, 3:08:29 pm
date modified: Tuesday, December 9th 2025, 3:23:41 pm
tags: [cs/linux, cs/linux/edit, cs/linux/files, cs/linux/networking, cs/linux/permissions, cs/linux/process, cs/linux/searching, cs/linux/variables]
template:
template-version:
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



  `make` ;;; Build the project according to the `Makefile`. 
ID: 1751997628850



  `make target` ;;; Build a specific target (e.g., `make all`, `make clean`). 
ID: 1751997628855



  `make -jN` ;;; Build using `N` parallel jobs (e.g., `make -j4`). 
ID: 1751997628859



  `make -f FILE` ;;; Specify an alternate `Makefile` (e.g., `make -f MyMakefile`). 
ID: 1751997628863



  `make -C DIR` ;;; Change to directory `DIR` before running the `Makefile`. 
ID: 1751997628867



  `make -n` ;;; Show what would be done without actually doing it (dry run). 
ID: 1751997628871



  `make -k` ;;; Continue as much as possible after an error. 
ID: 1751997628875



  `make -s` ;;; Silent mode; suppress command output. 
ID: 1751997628879



  `make clean` ;;; Remove build artifacts (files specified in `clean` target). 
ID: 1751997628883



  `cmake .` ;;; Generate build files in the current directory. 
ID: 1751997628887



  `cmake -Bbuild -H.` ;;; Generate build files in the `build` directory. 
ID: 1751997628891



  `cmake --build build` ;;; Build the project using the files in the `build` directory. 
ID: 1751997628895



  `cmake --build build --target TARGET` ;;; Build a specific target (e.g., `cmake --build build --target all`). 
ID: 1751997628899



  `cmake -G GENERATOR` ;;; Specify a generator for the build system (e.g., `cmake -G "Unix Makefiles"`). 
ID: 1751997628903



  `cmake -DVAR<equalSign>VALUE` ;;; Define a variable for configuration (e.g., `cmake -DCMAKE_BUILD_TYPE=Release`).  
ID: 1751997628907



  `cmake --version` ;;; Show the CMake version. 
ID: 1751997628911



  `cmake --help` ;;; Show help information. 
ID: 1751997628915



  `cmake ..` ;;; Configure a build from a parent directory (often used with out-of-source builds). 
ID: 1751997628920



  `systemctl status` ;;; Display the status of a system or service  
ID: 1751997628924



  `systemctl start <service>` ;;; Start a service  
ID: 1751997628928



  `systemctl stop <service>` ;;; Stop a service  
ID: 1751997628932



  `systemctl restart <service>` ;;; Restart a service  
ID: 1751997628936



  `systemctl reload <service>` ;;; Reload configuration for a service without stopping it  
ID: 1751997628940



  `uname` ;;; Display basic info about the system = `-a` All available info 
ID: 1751997628943



      `-r` Kernel release version
      `-n`Network node nost name
      `-m` System architecture
      `-o` Operating system
  `touch <file>` ;;; Create a new empty file or update the timestamp of an existing file. 
ID: 1751997628947



  `chmod <permissionsOwner><permissionGroup><permissionOthers> <file>` ;;; Change the permissions of a file or directory. = permissions:`7rwx, 6rw, 5rx, 4r, 3wx, 2w,1x,0(nothing)` 
ID: 1751997628952



  `chown <user>:<group> <file>` ;;; Change the owner and group of a file or directory. 
ID: 1751997628956



  `df -h` ;;; Show the disk space usage in a human-readable format.  
ID: 1751997628960



  `du -h <directory>` ;;; Show the disk usage of a directory and its contents in a human-readable format.  
ID: 1751997628964



  `ps aux` ;;; Display information about all running processes.  
ID: 1751997628969



  `kill <pid>` ;;; Terminate a process by its process ID (`pid`).  
ID: 1751997628973



  `grep <pattern> <file>` ;;; Search for a pattern within a file or files.  
ID: 1751997628977



  `find <directory> -name <filename>` ;;; Search for a file by name within a directory and its subdirectories.  
ID: 1751997628982



  `tar -czvf <archive_name>.tar.gz <directory>` ;;; Create a compressed archive of a directory.  
ID: 1751997628986



  `tar -xzvf <archive_name>.tar.gz` ;;; Extract a compressed archive. 
ID: 1751997628991



  `wget <url>` ;;; Download a file from the internet using its URL.  
ID: 1751997628995



  `curl <url>` ;;; Transfer data from or to a server, often used for making HTTP requests.  
ID: 1751997628999



  `ssh <user>@<host>` ;;; Connect to a remote server via SSH.  
ID: 1751997629003



  `scp <file> <user>@<host>:<destination>` ;;; Copy a file to a remote server using SSH. 
ID: 1751997629007



  `top` ;;; Display a real-time view of running processes and system resource usage. 
ID: 1751997629012



  `htop` ;;; An enhanced version of `top`, providing a more user-friendly interface. 
ID: 1751997629019



  `nano <file>` ;;; Open and edit a file using the `nano` text editor. 
ID: 1751997629025



  `vim <file>` ;;; Open and edit a file using the `vim` text editor.  
ID: 1751997629029



  `alias <alias_name>` ;;; Print alias value 
ID: 1751997629033



  `unalias <alias_name>` ;;; Remove an alias.  
ID: 1751997629037


 `ag <pattern>` ;;; Searches for patterns `<pattern>` within a file using the silver searcher `ag` 
        
