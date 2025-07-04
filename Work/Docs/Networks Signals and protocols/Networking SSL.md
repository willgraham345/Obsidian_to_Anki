---
summary: I think this is somewhat similar to the ssh keys protocols. This was the predecessor to the TLS protocol.
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Saturday, December 7th 2024, 10:40:57 am
type: note/system
next:
  - "[[Networking TLS]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Background
![[Networking SSL.png|214]]

## Concepts:
- Data that has been encrypted with a public key can only be decrypted with the corresponding private key. 
- Data that has been encrypted with a private key can only be decrypted with the corresponding public key. 

## Terms:
Certificate:
- Verifies that an entity is the owner of a particular public key. 
Private key:
- Used for encryption and decryption
- The only key is copied or shared by another party to decrypt the cipher text. Faster than public-key cryptography.
Public key 
- Used in SSL 
- Two keys:
	- Encryption key (public)
		- Public key is used to encrypt the plain text to convert it into cipher text
	- Decryption key (private key)
		- Used by the receiver to decrypt the cipher text to read the message
- Inefficient, used for short messages
