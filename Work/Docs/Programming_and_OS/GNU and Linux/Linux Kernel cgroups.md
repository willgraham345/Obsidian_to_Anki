---
summary: Feature from linux kernel to manage, restrict, and audit a group of processes. Very flexible, as they can operate on a (sub)sets of processes. Has both V1 and V2, with Red Hat Linux enterprise offering multiple processes. By default, configuration will be stored in /sys/fs/cgroup/*. Each task will have a reference-counted pointer to a css_set. Subsystem = resource controller = controller = something that acts upon group of tasks (i.e. processes). Many different cgroups can exist simultaneously on a system. Each hierarchy of cgroups is attached to one or more subsystems.
type: note/component
down:
  - "[[Linux Kernel cgroups css_set]]"
workflows:
  - "[[Linux cgroups resource control workflow]]"
similar:
  - "[[Docker Container cgroups resource control workflow]]"
  - "[[Linux Kernel Namespaces]]"
concept_of:
  - "[[Linux Kernel]]"
date created: Friday, November 15th 2024, 3:08:02 pm
date modified: Monday, December 9th 2024, 4:04:07 pm
concepts:
  - "[[Linux cgroup subsystems hierarchies groups and task relationship rules]]"
---
 
  

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## cgroup types:
- CPU
- memory
- block I/O
- device

### Red Hat Linux Implementation

[Available Subsystems in Red Hat Enterprise Linux](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/resource_management_guide/ch01#sec-How_Control_Groups_Are_Organized:~:text=Available%20Subsystems%20in,Note)
- `blkio` — this subsystem sets limits on input/output access to and from block devices such as physical drives (disk, solid state, or USB).
- `cpu` — this subsystem uses the scheduler to provide cgroup tasks access to the CPU.
- `cpuacct` — this subsystem generates automatic reports on CPU resources used by tasks in a cgroup.
- `cpuset` — this subsystem assigns individual CPUs (on a multicore system) and memory nodes to tasks in a cgroup.
- `devices` — this subsystem allows or denies access to devices by tasks in a cgroup.
- `freezer` — this subsystem suspends or resumes tasks in a cgroup.
- `memory` — this subsystem sets limits on memory use by tasks in a cgroup and generates automatic reports on memory resources used by those tasks.
- `net_cls` — this subsystem tags network packets with a class identifier (classid) that allows the Linux traffic controller (`tc`) to identify packets originating from a particular cgroup task.
- `net_prio` — this subsystem provides a way to dynamically set the priority of network traffic per network interface.
- `ns` — the _namespace_ subsystem.
- `perf_event` — this subsystem identifies cgroup membership of tasks and can be used for performance analysis.

## V1 vs V2
### V2
- Single unified hierarchy.
- "Internal" processes are not permitted. 
- Active cgroups must be specified via the files `cgroup.controllers` and `cgroup.subtree_control`
- Notifications for empty cgroups is provided by the `cgroup.events` file
- [p] `mount -t cgroup2 none /mnt/cgroup2` = 

# Media
<iframe src="https://wiki.archlinux.org/title/Cgroups" style="width: 100%; height: 1000px;background-color:white;"></iframe>

<iframe src="https://man7.org/linux/man-pages/man7/cgroups.7.html" style="width: 100%; height: 600px;background-color:white;"></iframe>