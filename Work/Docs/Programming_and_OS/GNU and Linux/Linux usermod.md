---
type: note
---
# Background
A command tool that modifies the system account files to reflect changes specified on command line. 
- It allows system administrators to make changes to existing user accounts without having to delete and recreate them.
[usermod man page](https://linux.die.net/man/8/usermod)

# Usage
| Flag | Description                                                         | Usage                                   | Example                                                                                            |
| ---- | ------------------------------------------------------------------- | --------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `-a`   | Add the user to supplementary group(s). Only use with `-G` flag.    | `usermod -aG groupname username`        | Add user "john" to the "sudo" group: `usermod -aG sudo john`                                       |
| `-c`   | Comment or GECOS field.                                             | `usermod -c "New comment" username`     | Add a comment "John Doe" to the user "john": `usermod -c "John Doe" john`                          |
| `-d`   | Specify the new home directory for the user.                        | `usermod -d /path/to/new/home username` | Change the home directory of user "john" to "/home/johnny": `usermod -d /home/johnny john`         |
| `-e`   | Set account expiration date (YYYY-MM-DD).                           | `usermod -e YYYY-MM-DD username`        | Set an expiration date of "2025-01-01" for user "john": `usermod -e 2025-01-01 john`               |
| `-g`   | Change the primary group of the user.                               | `usermod -g groupname username`         | Change the primary group of user "john" to "staff": `usermod -g staff john`                        |
| `-G`   | Add the user to supplementary group(s).                             | `usermod -aG groupname username`        | Add user "john" to the "sudo" group: `usermod -aG sudo john`                                       |
| `-l`   | Change the username of the user.                                    | `usermod -l newusername oldusername`    | Change the username from "john" to "johnny": `usermod -l johnny john`                              |
| `-L`   | Lock the user account.                                              | `usermod -L username`                   | Lock the account of user "john": `usermod -L john`                                                 |
| `-m`   | Move the contents of the user's home directory to the new location. | `usermod -m -d /new/home username`      | Move contents of user "john"'s home directory to "/home/johnny": `usermod -m -d /home/johnny john` |
| `-s`   | Change the user's login shell.                                      | `usermod -s /path/to/shell username`    | Change the login shell of user "john" to "/bin/bash": `usermod -s /bin/bash john`                  |
| `-u`   | Change the UID of the user.                                         | `usermod -u newUID username`            | Change the UID of user "john" to "1001": `usermod -u 1001 john`                                    |
| `-U`   | Unlock the user account.                                            | `usermod -U username`                   | Unlock the account of user "john": `usermod -U john`                                               |
