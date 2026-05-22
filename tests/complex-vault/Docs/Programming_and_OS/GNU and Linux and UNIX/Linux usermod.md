---
summary: "Change the group(s) a user belongs to. "
type: note/tool
headings:
  - "[[#Usage]]"
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, January 22nd 2026, 3:53:53 pm
template: "[[base_note_template]]"
template-version: 1.0.1
similar:
  - "[[Linux chmod]]"
tool_of:
  - "[[Linux]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[usermod man page](https://linux.die.net/man/8/usermod)

## Usage
 `usermod -aG groupname username` ;;; Add the user to supplementary group(s). Only use with `-G` flag.  
 `usermod -c "New comment" username` ;;; Comment or GECOS field.  
 `usermod -d /path/to/new/home username` ;;; Specify the new home directory for the user.  
 `usermod -e YYYY-MM-DD username` ;;; Set account expiration date (YYYY-MM-DD).  
 `usermod -g groupname username` ;;; Change the primary group of the user.  
 `usermod -aG groupname username` ;;; Add the user to supplementary group(s).  
 `usermod -l newusername oldusername` ;;; Change the username of the user.  
 `usermod -L username` ;;; Lock the user account.  
 `usermod -m -d /new/home username` ;;; Move the contents of the user's home directory to the new location.  
 `usermod -s /path/to/shell username` ;;; Change the user's login shell.  
 `usermod -u newUID username` ;;; Change the UID of the user.  
 `usermod -U username` ;;; Unlock the user account.  



