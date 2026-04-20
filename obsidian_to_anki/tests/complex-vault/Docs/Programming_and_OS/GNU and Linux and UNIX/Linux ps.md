---
type: note
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Tuesday, November 26th 2024, 1:53:21 pm
function_of:
  - "[[Linux CLI]]"
  - "[[Linux Processes]]"
tool_of:
  - "[[Linux]]"
---
# Background
In Linux, a running instance of a program is called process, and there's usually a ton of these running all at once. 

It accepts several types of options (UNIX, BSD, GNU)

# Usage
## Outputs
- `PID` = Process id. Knowing this will allow you to kill a process.
- `TTY` = Name of the controlling terminal for the process
- `TIME` = Cumulative CPU time of the process, shown in minutes and seconds
- `CMD` = Name of the command that was used to start the process
- `USER` - The user who runs the process.
- `%CPU` - The [cpu](https://linuxize.com/post/get-cpu-information-on-linux/) utilization of the process.
- `%MEM` - The percentage of the process’s resident set size to the physical memory on the machine.
- `VSZ` - Virtual memory size of the process in KiB.
- `RSS` - The size of the physical [memory](https://linuxize.com/post/free-command-in-linux/) that the process is using.
- `STAT` - The the process state code, such as `Z` (zombie), `S` (sleeping), and `R` (running).
- `START` - The time when the command started.

## Usage
## See all running processes
```shell
ps -aux
```
- `a`:  tells `ps` to display the processes of all users
- `u`: Stands for user-oriented format that provides detailed information about the processes
- `x`: Instructs `ps` to list the processes without a controlling terminal. These are mainly processes that are started on boot time and running in the background. 

## View all Processes with all child processes under their parents
```shell
ps -efH
```

### View tree view of parent to child processes
```shell
ps auxf
```
or
```shell
ps -ef
```

## See all processes run by a user
```shell
ps -U user_name
```

## Sell all processes run by a group
```shell
ps -G group_name_or_id
```

## Get all occurrences and PID of a program
```shell
ps -C program_name
```

## Get process information about a PID
```shell
ps -pN
```
You can get more than one PID by separation with a comma

```shell
ps -pN1, N2, N3
```