---
status: closed
type: project
project_id: 4
company: Varex
project: VivaPro
subproject: linux_development
tags:
  - archive_deprecated/Varex/vivaPro
---
# Related Links:
[[Fred Zoghi]]
- [[P013 VivaPro Network Settings Tool Crashes]]

# P011 Updates/Notes:
Things that need to be finished as I push for the first time:
- [x] Stage correct files
- [x] Get commit message in the right place
- [x] Push

Things that I don't want in the push:
- Anything related to the config thing for commenting out problems. 

### 2024-07-08 09:00
I'm not sure where I was trying to upload my build/changes to the VivaPro
Solved: I did it in the `host_guest_share` in Windows, or the `src` in Linux
- Has a commit with me as the editor. Need to figure out how to get that pushed to Jenkins

### 2024-07-08 11:00
Messaged with Fred, and asked to log a new bug saying that VivaPro doesn't compile on Linux. Logged a new bug, and renamed this project to the project file description

### 2024-07-08 12:00
Just got back from lunch and I'm jumping back into this. There were time issues with the Linux VM. Found a stack overflow thread describing how I'd go about resetting the time on the system. 
- [x] Updated date/time on Linux VM
Seeing different errors now, mostly related to VSP stuff. Nothing too crazy yet. 
Getting errors related to the virtualModeMapper function/gui. 
- I'm going to try and rebuild, but only while referencing the virtualModes folders within the qtBuildOnly directory thats in the repo I'm modifying. I think the errors are due to multiple definitions for the functions/classes
- Still getting the error
- What worked for us last time was to comment out the functions in VirtualModeMapper. I don't think that's necessarily the right move, and won't pass code review.

### 2024-07-08 14:00
Had issues with the timestamp, so I needed an active internet connection. Moved to a NAT connection with the local machine on the VirtualBox and that seemed to fix everything. Still have my git access. 

Testing the build on Linux from CMakeLists.txt scripts

Got another problem with the dlgOptions.cpp rule
- "No rule to build this..."
- My solution was to add that to the win32 and move the uncapitalized version to the Unix conditional
	- Also moved `INCLUDEPATH` to after the `SOURCES` value in the Unix conditional
		- Not sure what that's doing, but it seemed to go further in the build.

#### Issue with the viewFrameDisplayInterval.cpp
Added the cpp back to the sources list on the win32 conditional. I think it wasn't recognizing that part of it.

Found [this stack overflow answer](https://stackoverflow.com/questions/17168144/qt-project-no-rule-to-make-target-needed-by) which says  that I should basically add it to my sources. 

I changed it back to a capital letter. I need to go and check that directory to see what was made. 
- In the directory, it doesn't have capital letters...
- No idea what to do here. 
Realized I hadn't uncapitalized the detectorAcquisitonRad file in the Unix source thing. 
Fixed it, only needed to uncomment the part in the `SOURCES` variable that was referencing the file capitalized. Instead, I separated it into win32 and unix components.

### 2024-07-08 16:00
Figured out how to get past the errors I was seeing earlier by commenting and uncommenting the `SOURCES` stuff like I said earlier. 
Now I'm seeing a big error log about the references to `DlgVirtualModeMapper`. 

### 2024-07-09 13:00
I modified the project file in the `~/vivapro` rather than in the `~/src/vivapro` that I have on Windows + Linux 

I'm wondering if there's a way to use debugging symbols from a windows build onto the Linux OS.
- I don't think this is possible, because the symbols would be accessed differently. 

I need to learn how debuggers work. 
- [[How does a debugger work]]

#### Breakdown of the errors I'm seeing
`/vivapro/build/msvc/2015/x64/debug/obj/viewframedisplayinterval.o`
- Function `QTypedArrayData`
- Multiple definitions for this file
	- `ViewFrame::setFluorolComboboxToIncomingFrames`
		- Defined first in the `.o` file, and then again in the `.cpp` file for `viewframedisplayinterval`
- Then it's saying that we don't have references to `DlgVirtualModeMappper` stuff.

I wonder if I try to rebuild the whole project, if that file will still be there. 
- When cleaning in QtCreator, the `dlgVirtualModeMapper` is still there, but the `viewframedisplayinterval` is not. 
- When I run `build.sh` I'm curious what happens
	- Not much. I think the `dlgVirtualModeMapper` is created in this or the `generate.sh` step.

Went through and tried to redo the functions that had been changed. I was dumb and didn't stash the changes.
- Failed at the same place
	- QComboBox wasn't defined. I included that into the file so it would be. 
- I'm realizing a lot of these errors may be due to the `release:` and `debug:` filepaths. Changed them to be platform-specific

### 2024-07-11 10:00
Back at it again. Fred's instructions were to look for where I include the `setFluoroComboIComboboxToIncomingFrame()`.

`/usr/bin/ld` is the thing showing the errors. This is the file for the Linux linker. 

I have two definitions for `setFluorolComboboxToIncomingFrames`

I'm including stuff only from Linux, so I'm free there. I don't understand why qt would be finding that other definition in the build files. 
I don't know that the error is happening when I'm including the right/wrong directory.
- It may be happening because the file is looking for the incorrect definition. 

![[P011 VivaPro Project File Doesn't Compile 2024-07-11 11.17.50.excalidraw]]
[[2024-07-11 Fred - VivaPro Errors]]

### 2024-07-15 13:00
- Sent Fred an update on the using the `win32` and `unix` conditionals within the project. 
- 

### 2024-07-15 14:00
Fred called me, we're debugging the message.
Realized I had a double definition of a couple things. Making sure we have the right stuff defined here. 

Fred and I realized that we don't know what's going on with the error saying `undefined reference to 'typeinfo for BaseException'`
- We need to do some additional research on it. 
![[P011 VivaPro Project File Doesn't Compile 2024-07-15 15.26.44.excalidraw]]

#### Google search results
[Stack overflow virtual function](https://stackoverflow.com/questions/307352/g-undefined-reference-to-typeinfo)
- Says we might be declaring a virtual function without defining it. 
- I think we might need to include exceptions.cpp to the compiler and/or include path

#### Update to Fred
I found this [stack overflow thread](https://stackoverflow.com/questions/307352/g-undefined-reference-to-typeinfo "https://stackoverflow.com/questions/307352/g-undefined-reference-to-typeinfo"), which talks about a virtual function never being defined. If we think that's what is happening, then there's likely a definition for the `BaseException`. I looked in the includes, and I believe the only place it is defined is in test/exceptions/src/exceptions.cpp. I found this [additional Reddit thread](https://www.reddit.com/r/cpp_questions/comments/thh1sy/errors_undefined_reference_to_vtable_for_shape_as/ "https://www.reddit.com/r/cpp_questions/comments/thh1sy/errors_undefined_reference_to_vtable_for_shape_as/") which says a similar thing. I'm not sure if this is correct, but it looks like these functions are not "pure virtual". I could be off here, but that's my current thought process.

### 2024-07-15 16:00
We have VivaPro compiling and debugging. The next steps are:
1. Change `BaseBlock.h`
2. Change `exceptions.cpp` and `exceptions.h` to make things work without commenting stuff out. 


Fred wants me to "work on bugs again" time is indeed a flat circle

### 2024-07-16 10:00
My git just stopped letting me clone. No idea why. 
Reviewed private-public key stuff

Fred told me to rename win32/linux stuff, and make sure that the filenames match the linux names. I think I'm supposed to rename some of the files. 
My bug workflow should be something like:
1. Make changes
2. Stage with git commit
3. Push

[[2024-07-16 Fred - Naming Bug]]
I'm a little confused with what Fred meant by "renaming the files on the disk". 

Things removed from header file:
- dlgoptions.cpp
- detectoracquisitionrad.cpp
- viewframedisplayinterval.cpp
- test/qtbuildonly/autoversionqtbuildonly

### 2024-07-16 15:00
Build failed for some UNKNOWN freaking reason. Fred also had a few other things he didn't like about it. 

### 2024-07-16 10:00
My git just stopped letting me clone. No idea why. 
Reviewed private-public key stuff

Fred told me to rename win32/linux stuff, and make sure that the filenames match the linux names. I think I'm supposed to rename some of the files. 
My bug workflow should be something like:
1. Make changes
2. Stage with git commit
3. Push

[[2024-07-16 Fred - Naming Bug]]
I'm a little confused with what Fred meant by "renaming the files on the disk". 

Things removed from header file:
- dlgoptions.cpp
- detectoracquisitionrad.cpp
- viewframedisplayinterval.cpp
- test/qtbuildonly/autoversionqtbuildonly

### 2024-07-16 15:00
Build failed for some UNKNOWN freaking reason. Fred also had a few other things he didn't like about it. 

Copied `qtBuildOnly` to the `/usr` directory
Cloning to the `qt_name_update` in my VM home directory

I've had some issues with building the library to test it. There's an issue with bringing the `vsp2.h` into the build. 
- 

First thing for tomorrow should be to get the VivaPro building within Linux, with the vsp2 header that is missing. 

### 2024-07-17 10:00
Looking into how I can output the path of Qt stuff. 

Figured out how to expand the variable I wanted, here's my output:
- ![[P011 VivaPro Project File Doesn't Compile.png|550]]
[[P011 VivaPro Project File Doesn't Compile]]

Having a nice chat with Fred. He isn't sure what's going on. 

From what I can tell, we need to have the qtBuildOnly within the repository, or in the ~ (home) directory
- The pathing is all goofy. Not sure why it doesn't like that. 

We've gone in a circle, Fred did not help much. 

The autoversion.h needs to stay in the same case. 

Figured out how to update local variables, see [[Qt.qmake]] section on the language. Found a really good stack overflow article showing how to access and use the variables. 

#### Plan moving forward
1. Build in local 
	1. Fix autoVersion.h renaming problem. 

I'm seeing an error similar to the earlier entry about `typeinfo for BaseException`
- I think it's because Fred's local `qtBuildOnly` doesn't have correct stuff. I may need to send him a new/revised version. 

### 2024-07-17 14:00
I need to reorganize which repository means what with my computer. I may need to update Fred on this

I'm working with the `viva_name_update` repo. 

#### Draft to Fred saying that the qtBuildOnly is wrong
After looking into this quite a bit, the issues I'm seeing may be related to the default

### 2024-07-18 10:00
Getting the right stuff going again. Redid a lot of the repository configuration to make more sense. Added some descriptions on the different cloned versions of vivapro.

Reset undesired changes with git on Vivapro repo I'm working with 
Next steps
1. Get the repo building
	1. Could require mods to the `qtBuildOnly` I have locally. This thing should also likely be in source control. 
2. Push changes to Gerrit. 
3. Reach out to Fred with update. 

The error I'm getting again is that I have a `undefined reference to 'typeinfo for BaseException'`
- Not sure if this is the same thing. I think there

Things I've tried to fix the bug
- Updated includepath to have the test directories. 
	- Modified the dlgVirtualModeMapper.h and dlgVirtualModeMapper.h files to not use the BaseBlockTypes stuff. This needs to be included in the push/pull commit. 
Got it working with the current stuff. I pushed it to source control, waiting on the build.
- The repo that I have building has the path: `/media/sf_host_guest_share/viva_name_update/vivapro`
- I think that's wrong, it is `/media/sf_host_guest_share/viva_clean`

