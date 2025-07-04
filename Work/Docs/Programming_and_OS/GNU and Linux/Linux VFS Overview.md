---
type: note/concept
concept_of: ["[[Linux Filesystem Hierarchy]]", "[[Linux Kernel Storage Interfaces]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Monday, November 25th 2024, 5:15:15 pm
---
# Background
- Software layer in the kernel that provides the filesystem interface to userspace programs. Provides abstraction within the kernel which allows different filesystem implementations to exist.

- Calls open(2), stat(2), read(2), write(2), chmod(2), and so on from a process context. Locking described within [[Linux Kernel Locking]].

[Read more here](https://docs.kernel.org/filesystems/vfs.html)
- This link goes directly to where the objects are stored in memory. 

## dcache (Directory Entry Cache)
The pathname that is passed to the commands bove is used by the VFS to search through the dcache. This is a faster look-up mechanism to translate a filename. 

## Inode Object
Filesystem objects like regular files, directories, FIFOs and other stuff. They live either on disc or in the (for block device filesystems) or memory (for pseudo filesystems).
To look up an inode requires that the VFS calls the lookup() method of the parent directory inode. 

## File Object
Opening a file requires another operation: allocation of a files structure. Initialized with a pointer to the dentry and a set of file operation member functions. These are taken from the inode data. 

# Usage