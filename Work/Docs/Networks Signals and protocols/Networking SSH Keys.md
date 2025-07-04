---
summary: How ssh deals with authentication. There is a private key as well as a public key. Private key should be kept secret, the public can be put anywhere. The private key is used to pretend to be yourself. Public key can be generated from the private key, but not vice versa. The idea
type: note/concept
date created: Friday, November 22nd 2024, 12:46:29 pm
date modified: Friday, November 22nd 2024, 3:05:05 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

## Public Key and Private Key
```mermaid
---
title: Using SSH with PC and server
---
classDiagram
	direction TD
	class PC {
		-id_rsa.pub
		id_rsa
		ssh-keygen() : id_rsa, id_rsa.pub
	}
	class server {
		-copied_id_rsa.pub
	}
		
	server <-- PC: knows public key
	PC <-- server: knows public key

```
![[ssh-asymmetric-encryption.svg]]

# More Info
<iframe src="https://www.manageengine.com/privileged-access-management/what-is-ssh-secure-shell.html" style="width: 100%; height: 600px;background-color:white;"></iframe>


<iframe src="https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-linux/" style="width: 100%; height: 600px;background-color:white;"></iframe>