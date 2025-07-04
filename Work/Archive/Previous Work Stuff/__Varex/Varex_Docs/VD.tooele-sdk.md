---
company: Varex
tags: archive_deprecated/Varex
---
# Background
Tooele was used as a way to house all SDKs under one repository. 
- [[VD.zlilz]] has T01 and T02, but T02 is only within tooele-sdk
	- These are branches within the repo, and I think they *might* be related to different RCs

## Instructions
[Bug Report](https://fpgit/#/c/10827/5/install/sdk/make_vsp2_sdk.sh)
logSettings.txt should have been added to the SDK zip file (in the TO2)
Look in the zlilz thing to figure out how they added it to the SDK zip file. 

## Commit that explains how `zlilz` implements the thing
[Commit with zlilz implementation](https://fpgit/#/c/10827/5/install/sdk/make_vsp2_sdk.sh)

# Questions
1. Why are we zipping these files?
	1. How are we zipping these files (I'm assuming it must be a shell script or something)
	2. Does Daniel Rolfe still work here?