---
type: note
---
# Background
Change the current directory/folder and store the previous folder/path for use in the [[Windows popd]] command

# Usage
## Syntax
  ```
  PUSHD [_drive_]_path_
  
  PUSHD
  ```
  - `drive` = The drive to switch to
	  - If not specified, current drive is assumed
  - `path` = The folder to make `current`
  - If both `drive` and `path` are not specified, `pushd` will display a list of previous path names. 
	  - Can be switched back by using [[Windows popd]]