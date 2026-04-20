---
summary: Filesystem providing the means for exporting kernel data structures, their attributes, and the linkages between them to userspace.
type: note/function
concept_of: ["[[Linux Filesystem Hierarchy]]", "[[Linux Kernel Storage Interfaces]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Thursday, February 6th 2025, 10:00:55 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
- RAM-based filesystem initially based on ramfs. Provides a way to export kernel data structures, their attributes, and the linkages between them to userspace. 
- Tied inherently to the kobject infrastructure

<iframe src="https://docs.kernel.org/filesystems/sysfs.html" style="width: 100%; height: 600px;background-color:white;"></iframe>
