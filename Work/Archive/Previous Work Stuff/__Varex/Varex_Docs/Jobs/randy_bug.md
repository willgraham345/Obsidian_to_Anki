---
company: Varex
tags: archive_deprecated/Varex
---
Tags:
# Description:
[Bug 31450](https://fpbugs/issues/31450)
LogSettings.txt file was included at main level of the SDK (alongside README.TXT file). This needs to be in T02 as well. 
[How to create SDK zip files](https://fpgit/?#/c/10827/)
- I'm just monitoring this 
- I'm doing this for vsp2express_sdk
Am I just making sure that the `zlilz` repo gets the LogSettings as well?
- If there's a dependency on this submodule I think it'll come out in the wash when I refactor the logging changes I've made within [[01_logging_localTests]]
	- 
## Actual + Expected:
## System Overview/Notes:
# Solution
## Things That Haven't Worked:
## Things Fixed:
# Questions

# Meeting with Randy
- I can't see the Tooele `zlilz` builds

Last T01 official build  `T01_20.3.1._RC1`
- LogSettings.txt and README.md
- That is what needs to happen in `T02` as well as `T01`

There's a shell script that gathers certain files and zips them up, which happens with the README.md

Forget `zlilz`

Go to `tooele-sdk-repo`
- In the `install/`, there is a `package_sdk.sh`
	- THAT is what I'm editing.

Once I've made the changes, 

The git `HEAD` is usually master
- They label whenever possible, and branch only when necessary. 
- The idea is that I need to go towards