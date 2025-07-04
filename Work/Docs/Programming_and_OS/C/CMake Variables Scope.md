---
summary: 
source: ["[[CMake Variables]]"]
similar: ["[[Cmake target link scopes]]"]
date created: Tuesday, October 15th 2024, 6:15:01 pm
date modified: Wednesday, October 16th 2024, 11:33:11 am
type: note/concept
---
# Variable Scope
When you set a variable, it is visible to:
- Current `CMakeLists` file or function
- Any subdirectory's CMakeLists files
- Functions or macros that are invoked
- Any files that are included with the [[CMake.include]] command

When a new subdirectory is processed (or a function is called), a new variable scope is created and initialized wiht the curernt value of all variables in the calling scope. 
- Any new variables created will be within the child scope. Changes to existing variables will not impact parent scope.
	- If you'd like those changes to occur, see [[CMake.PARENT_SCOPE]]
Are defined in the order of execution of [[CMake.set]] commands.