---
type: note
date created: Tuesday, August 20th 2024, 2:05:35 pm
date modified: Thursday, August 22nd 2024, 11:05:29 am
---
# Background
- SSH cloning requires authentication once, while https requires authentication each time you perform an operation between your computer and GitLab

- Https advantages
	- Easier to access from anywhere, you only need your account details
	- HTTPS is a port that is open in all firewalls, which makes access less likely to be blocked
- SSH advantages
	- SSH keys don't provide access to your GitHub account, so your account can't be hijacked if your key is stolen
	- Using a strong keyphrase with your 

- If your account credentials (username/password) are stolen, you can be locked out. 
- If a private key (ssh key) is stolen, the only thing they can break is whatever repository they have set up. 

- See [[Networking SSL]] for more information

# Usage