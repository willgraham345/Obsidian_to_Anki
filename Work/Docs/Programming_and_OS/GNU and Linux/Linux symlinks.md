---
type: note/component
component_of: ["[[Linux Filesystem Hierarchy]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:09:24 am
---
# Background
- A symbolic link (symlink), creates a name that references another file, directory, or other Linux file system object
	- Lets you make changes in one place, rather than in many. 

A symlink is a special type of file whose data is a path to the name of a file system object. The file system object can also be a file, directory, pipe, special device, or another symlink (also known as chains of symlinks)

## Chains of Soft links

Soft link vs hard link
- Entries 

# Usage
1. Linking using the `ln` command

## Create a symlink
```shell
ln -s /path/to/file /path/to/symlink
```


```bash
ln -s </target-directory/target-file> </symlink-directory/example-symlink>
```
- `-s` tells Linux to create a soft link rather than a hard link

## Create `symlink-directory` in Current Directory 
```bash
ln -s /tmp/reference-directory symlink-directory
```

## View Contents of a Symlink
```bash
ls -l symlink-directory
```
- Displays something like this:
```
symlink-file -> /tmp/reference-file
```