---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/vivaPro
---
Tags:

# Description:
## Actual + Expected:
- Linux build works great when using the `build.sh` and `generate.sh` scripts
- Fred has a build that I'm *guessing* was built within Windows using the `build.bat` and `build` scripts. This build has the bug that we're seeing.
- I have a hard time believing that the fileopen filesave operations will be the end of our problems for the Linux application. I think the easiest path forward would be to build the Windows application for Windows, and build a Linux application within Linux. The `generate.sh` and `build.sh` built a correct and working version for me (based on the current `master` branch). As that is under source control, we could create two builds, with one on Linux and one on Windows. I'm guessing that would be the correct way to move forward. .

## What I Did:
### Email to Paul
Paul,

Fred and I talked about the bug, and we are back on the same page. In Bug #31545, Fred's "Save" button isn't correctly saving opened files within VivaPro. My VivaPro application didn't experience the same error. After talking with Fred, we realized that his VivaPro application may have been built within Windows and copied over into the guest Linux-OS while mine was built natively using the VivaPro repository and the `generate.sh` and `build.sh` scripts. I believe this is what is causing the bug, and likely doesn't require software changes.

I think the easiest way to resolve this in the future is by having two separate builds for the two different operating systems. If we can correctly configure the Jenkins builds, they should be able to work similarly to what I've had. 

Fred, please feel free to correct me with anything I missed. 

### SDK Build Process
What goes to the customer is the `tooele-SDK`
There's a lot of stuff going into the build process
- There's a bunch of `.gimodules` that are required. 
- CMake file
- There are a TON of different things going on with the build process.
- They send the ENTIRE SDK to the customer. 
	- We need to somehow integrate the build scripts in the 

## Meeting with David Marshall
On the Jenkins build, this creates everything natively into on Windows, Ubuntu 18, Ubuntu 20, and other stuff.
- Fred could have built it on 18.04

In the tooele sdk it has a step that combines outputs from other submodules.
- vivaPro is a submodule of tooele-sdk. 
	- The main thing 

### Jenkins
- For automating builds
- Someone make a jenkins job, and its tied to a repository in Gerritt. 
	- Everytime we push to Gerrit, it triggers a build.
	- Builds based on a script within the repository. 
		- Written in groovy
	- archiveArtifacts
		- These commands store stuff within the Jenkins build log. 
		- Outputs for different build platforms. 
- Specific builds are associated with specific tags within Gerrit. 
	- Pushing is to the common job. 
- Building different things is triggered with tags within 
	- Randy typically manages this
		- Tags are differentiated within 

## System Overview/Notes:
# Solution
## Things That Haven't Worked:
## Things Fixed: