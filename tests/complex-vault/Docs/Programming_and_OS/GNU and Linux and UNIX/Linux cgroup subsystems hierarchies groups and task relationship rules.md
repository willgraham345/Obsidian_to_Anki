---
summary: A single hierarchy can have one or more subsystems to it. Any single subsystem cannot be attached to more than one hierarchy if one of those hierarchies has a different subsystem attached to it already.
type: note/concept
date created: Monday, December 9th 2024, 4:07:48 pm
date modified: Monday, December 9th 2024, 4:15:25 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Rules
1. A single hierarchy can have one or more subsystems attached to it
	1. `cpu` and `memory` could be attached to a single hierarchy
2. Any subsystem (such as `cpu`) cannot be attached to more than one hierarchy if one of those hierarchies has a different subsystem to it already
	1. `cpu` can never be attached to two hierarchies if one of those hierarchies already has the `memory` subsystem attached to it.
3. Each time a new hierarchy is created on a systems, all tasks on the systems are initially members of the default cgroup of the hierarchy (known as the root cgroup). 
	1. For any single hierarchy you create, each task on the system can be a member of exactly one cgroup in that hierarchy. 
4. Any process (task) on the system which forks itself creates a child task. A child task automatically inherits the cgroup membership of its parent but can be moved to different cgroups if needed.

## Implications
- Because a task can belong to only a single cgroup in any one hierarchy, there is only one way that a task can be limited or affected by any single subsystem. This is logical: a feature, not a limitation.
- You can group several subsystems together so that they affect all tasks in a single hierarchy. Because cgroups in that hierarchy have different parameters set, those tasks will be affected differently.
- It may sometimes be necessary to _refactor_ a hierarchy. An example would be removing a subsystem from a hierarchy that has several subsystems attached, and attaching it to a new, separate hierarchy.
- Conversely, if the need for splitting subsystems among separate hierarchies is reduced, you can remove a hierarchy and attach its subsystems to an existing one.
- The design allows for simple cgroup usage, such as setting a few parameters for specific tasks in a single hierarchy, such as one with just the `cpu` and `memory` subsystems attached.
- The design also allows for highly specific configuration: each task (process) on a system could be a member of each hierarchy, each of which has a single attached subsystem. Such a configuration would give the system administrator absolute control over all parameters for every single task.

[1.2. Relationships Between Subsystems, Hierarchies, Control Groups and Tasks | Red Hat Product Documentation](https://docs.redhat.com/en/documentation/red_hat_enterprise_linux/6/html/resource_management_guide/sec-relationships_between_subsystems_hierarchies_control_groups_and_tasks#sec-Relationships_Between_Subsystems_Hierarchies_Control_Groups_and_Tasks)