---
summary: Secure shell, which is an alternative to unsecured remote shell protocols. Uses a client-server paradigm with clients and servers communicating via a secure channel run on TCP/IP.
headings:
  - "[[#Concepts of Note]]"
  - "[[#Diagrams]]"
  - "[[#Usage]]"
type: note/tool
up:
  - "[[Networking]]"
concepts:
  - "[[Networking SSH Keys]]"
  - "[[Networking SSH Terminology]]"
processes:
  - "[[Networking SSH Usage]]"
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Wednesday, October 8th 2025, 11:06:11 am
item_of:
  - "[[Application Layer Protocols]]"
  - "[[Networking Systems and Conventions]]"
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[Networking Application Layer|OSI Application Layer 7]]"
tool_of:
  - "[[Networking Tools]]"
tools:
  - "[[ssh keygen]]"
---


# Summary
󰙎 Networking SSH ;;; Secure shell, which is an alternative to unsecured remote shell protocols. Uses a client-server paradigm with clients and servers communicating via a secure channel run on TCP/IP.
# Additional Background
## Concepts of Note
SSH = secure shell
- Designed as an alternative to unsecured remote shell protocols, and uses a client-server paradigm with clients and servers communicating via a secure channel. 
- Runs on TCP/IP. 
### Config directory 

### 3 Layers to SSH
1. Transport layer
	1. Ensures secure communication between server and client, monitors data encryption/decryption, and provides intregrity to the connection. Also performs data connection and compression
2. Authentication Layer
	1. Conducts client authentication procedure
3. Connection Layer
	1. Manages communication channels after authentication
## Usage
- [Set up personal SSH keys on Linux \| Bitbucket Cloud \| Atlassian Support](https://support.atlassian.com/bitbucket-cloud/docs/set-up-personal-ssh-keys-on-linux/)
- [Excruciatingly Detailed Guide to SSH](https://grahamhelton.com/blog/ssh-cheatsheet/)

## Diagrams
![[Networking SSH How it Works.png|550]]