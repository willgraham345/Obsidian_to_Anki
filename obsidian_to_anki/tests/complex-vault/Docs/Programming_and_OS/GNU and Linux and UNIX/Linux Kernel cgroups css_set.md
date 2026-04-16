---
summary: A data structure representing a set of reference-counted pointers to cgroup_subsys_state objects. There is one of these for each cgroup subsystem registered in the system. There is no direct link from a task to the cgroup of which it's a member in each hierarchy. This can be determined by following pointers through the cgroup_subsys_state objects.
type: note/standard
up: ["[[Linux Kernel cgroups]]"]
aliases: [css_set]
date created: Monday, December 2nd 2024, 5:15:02 pm
date modified: Monday, December 9th 2024, 3:52:44 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`
A linked list runs through the cg_list field of each task_struct using the css_set, anchored at css_set->tasks.


