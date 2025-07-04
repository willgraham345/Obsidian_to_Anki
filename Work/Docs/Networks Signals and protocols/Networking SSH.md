---
type: note
up: ["[[Networking]]"]
concepts: ["[[Networking SSH Keys]]", "[[Networking SSH Terminology]]"]
functions: ["[[ssh keygen]]"]
workflows: ["[[Networking SSH Usage]]"]
component_of: ["[[Networking Terminology]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 23rd 2024, 9:45:57 am
---
# Background
SSH = secure shell
- Designed as an alternative to unsecured remote shell protocols, and uses a client-server paradigm with clients and servers communicating via a secure channel. 
- Runs on TCP/IP. 

![[Networking SSH How it Works.png|550]]

## 3 Layers to SSH
1. Transport layer
	1. Ensures secure communication between server and client, monitors data encryption/decryption, and provides intregrity to the connection. Also performs data connection and compression
2. Authentication Layer
	1. Conducts client authentication procedure
3. Connection Layer
	1. Manages communication channels after authentication

# Linux `.ssh` Folder
The `.ssh` folder is for managing SSH keys and client configuration. 
- This folder comes to life the moment you use SSH or `ssh-keygen` for the first time. 


