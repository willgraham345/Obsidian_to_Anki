---
type: note
tags: note/git
---
By default, when you clone a project with a submodule, you get the directories that contain submodules with none of the files in them. 
- To get the files, you need to run `git submodule init` to initialize, then `git submodule update` to fetch the data
- OR, you can pass in the `--recurse-submodules` into your clone and it will automatically initialize and update each submodule in the repository, including nested submodules. 


