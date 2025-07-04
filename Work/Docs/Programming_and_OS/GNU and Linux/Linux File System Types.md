---
type: note/concept
concept_of: ["[[Linux Filesystem Hierarchy]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 9:59:14 am
tags: [note/GNU_Linux]
---
# Background
- File system types are ways of organizing/storing data in a medium. Define how data is accessed, stored, and managed.

## CommonTypes
### FAT32 
- FAT32 = File Allocation Table 32
- Older file system known for simplicity and compatibility with operating systems
- Often used on removeable storage types like USB and SD cards

### exFAT
- Extended File Allocation Table
- An extension of FAT32 designed to overcome limitations, especially regarding file size and partition size
- Suitable for flash drives, external hard drives and anything that needs to be compatible with different operating systems

### NTFS (New Technology File System)
- Default file system for modern Windows OS
- Supports features like file permissions, encryption, and compression

### ext4 (Fourth Extended File System)
- Default file system for many Linux distributions
- Used on Linux for both systems and data partitions. Supports large file systems and files, journaling, and backward compatibility with ext3 and ext2

### HFS+ (Hierarchical File System Plus)
- Default file system used by macOS versions prior to macOS High Sierra

### ZFS
- Powerful/feature-rich file system originally developed by sun microsystems
- OS, and some Linux distributions, FreeBSD. Supports cool stuff like copy-on-write, snapshots, and data integrity

### ReFS (Resilient File System)
- Made by microsoft, designed for high-resiliency and scalability
- Primarily for enterprise environments.

# Usage

## Linux File System
Follows the FHS standard, which defines the directory structure and purpose of each directory 
