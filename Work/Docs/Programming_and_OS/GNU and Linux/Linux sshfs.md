---
summary: Really cool tool that lets you remotely edit an ssh connection by mounting it as a filesystem.
type: 
date created: Thursday, February 6th 2025, 5:41:11 pm
date modified: Thursday, February 6th 2025, 5:42:41 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
```shell
sudo apt-get install sshfs
```

## Setup
```shell
mkdir ~/remoteserv    
sshfs -o idmap=user <username>@<ipaddress>:/remotepath ~/remoteserv
```

<iframe src="https://vim.fandom.com/wiki/Editing_remote_files_via_scp_in_vim" style="width: 100%; height: 600px;"></iframe>