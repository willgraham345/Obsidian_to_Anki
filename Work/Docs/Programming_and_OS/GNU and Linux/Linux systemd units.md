---
summary: Abstractions of system resources in a standardized representation. Units can be jobs or other init systems, but with a much broader definition. Units can be managed by the suite of daemons and manipulated by the provided utilities. These system resources are generally kept in the /lib/systemd/system directory. The files typically have a type suffix according to the resource that they describe.
headings: ["[[#Breadcrumbs]]", "[[#Concepts of Note]]", "[[#Usage]]"]
type: note/concept
down: ["[[Linux systemd scope]]", "[[Linux systemd slice]]"]
workflows: ["[[Linux systemd Unit File Editing]]"]
concept_of: ["[[Linux systemd]]"]
date created: Tuesday, December 3rd 2024, 10:09:48 am
date modified: Wednesday, May 21st 2025, 2:40:06 pm
---

# Summary

`VIEW[**{summary}**][text(renderMarkdown)]`

## Concepts of Note

### Types of Units/Best Practice

Directory -> `.d` suffix
`.conf` can be used to override or extend attributes of system's unit files.
Type suffix

- **`.service`**:  
   Describes how to manage a service or application, including how to start/stop it, when to start automatically, and dependency/order information.
- **`.socket`**:  
   Defines a network or IPC socket (or FIFO buffer) for socket-based activation. Always paired with a `.service` file that starts when activity is detected.
- **`.device`**:  
   Describes a device managed by `systemd`, often triggered by `udev` or the `sysfs` filesystem. Useful for scenarios like ordering, mounting, and device access.
- **`.mount`**:  
   Manages a mount point on the system, with names based on the mount path (slashes replaced by dashes). Often generated from `/etc/fstab`.
- **`.automount`**:  
   Configures a mount point that is automatically mounted. Requires a matching `.mount` unit to define the mount specifics.
- **`.swap`**:  
   Describes swap space. Unit names reflect the device or file path used for swapping.
- **`.target`**:  
   Provides synchronization points during boot or state transitions. Other units tie their operations to specific targets.
- **`.path`**:  
   Defines a path for path-based activation. A `.service` unit with the same base name is triggered when the path changes, using `inotify`.
- **`.timer`**:  
   Similar to `cron`, defines a timer for delayed or scheduled activation. A matching unit starts when the timer is triggered.
- **`.snapshot`**:  
   Created with the `systemctl snapshot` command to save the current system state. Used to roll back temporary states; does not persist across sessions.
- **`.slice`**:  
   Associated with Linux Kernel cgroups for managing resource allocation. Unit names reflect their position in the cgroup hierarchy.
- **`.scope`**:  
   Automatically created by `systemd` from bus interface data to manage external sets of system processes.

## Breadcrumbs

```breadcrumbs
type: mermaid
field-groups: [downs]
merge-fields: true
sort: field asc
show-attributes: [field]
```

## Usage

Use cases:

- **socket-based activation**: Sockets associated with a service are best broken out of the daemon itself in order to be handled separately. This provides a number of advantages, such as delaying the start of a service until the associated socket is first accessed. This also allows the system to create all sockets early in the boot process, making it possible to boot the associated services in parallel.
- **bus-based activation**: Units can also be activated on the bus interface provided by `D-Bus`. A unit can be started when an associated bus is published.
- **path-based activation**: A unit can be started based on activity on or the availability of certain filesystem paths. This utilizes `inotify`.
- **device-based activation**: Units can also be started at the first availability of associated hardware by leveraging `udev` events.
- **implicit dependency mapping**: Most of the dependency tree for units can be built by `systemd` itself. You can still add dependency and ordering information, but most of the heavy lifting is taken care of for you.
- **instances and templates**: Template unit files can be used to create multiple instances of the same general unit. This allows for slight variations or sibling units that all provide the same general function.
- **easy security hardening**: Units can implement some fairly good security features by adding simple directives. For example, you can specify no or read-only access to part of the filesystem, limit kernel capabilities, and assign private `/tmp` and network access.
- **drop-ins and snippets**: Units can easily be extended by providing snippets that will override parts of the system’s unit file. This makes it easy to switch between vanilla and customized unit implementations.

## Editing files

- Found in ![[Linux Filesystem Hierarchy#/lib/systemd/system]]
  Best practice is to create directories named after the unit file with `.d` appended on the end.

## [[Linux systemd Unit File Editing]]
