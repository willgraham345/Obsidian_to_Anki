---
summary: Command line tools for ad hoc commands, and for performing operations/tasks. Ad hoc commands use the `/usr/bin/ansible` cli tool to automate a task on one or more nodes. These tasks are quick and easy, but not reusable.<br><br>Useful for rebooting servers, managing files, pagckages, groups/users,
headings: ["[[#Concepts of Note]]"]
type: note/component
component_of: ["[[Ansible]]"]
date created: Monday, March 17th 2025, 11:20:26 am
date modified: Thursday, July 3rd 2025, 1:52:14 pm
modules: "[[#Commands]]"
tags: [command/ansible]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Ansible CLI cheatsheet — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/command_guide/cheatsheet.html)

## Concepts of Note
Patterns
- When executing ad hoc commands, you need to choose which managed nodes/groups you want to execute against. Patterns let you run commands and playbooks from specific hosts and/or groups in your inventory. They are highly flexible, use wildcards, regular expressions, and more. [Patterns: targeting hosts and groups — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/inventory_guide/intro_patterns.html#intro-patterns)

## Commands
- [c] `ansible [host-pattern] -m [module] -a "[module-args]"` = Ansible basic command = #command/ansible
<!--ID: 1751434091874-->

  doxygen
[Ansible CLI cheatsheet — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/command_guide/cheatsheet.html)