---
summary: Command line tools for ad hoc commands, and for performing operations/tasks. Ad hoc commands use the `/usr/bin/ansible` cli tool to automate a task on one or more nodes. These tasks are quick and easy, but not reusable.<br><br>Useful for rebooting servers, managing files, pagckages, groups/users,
type: note/tool
headings: ["[[#Concepts of Note]]", "[[#Usage]]"]
date created: Monday, March 17th 2025, 11:20:26 am
date modified: Monday, January 5th 2026, 3:06:23 pm
tags: [tools/ansible]
template:
template-version:
tool_of: ["[[Ansible]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Ansible CLI cheatsheet — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/command_guide/cheatsheet.html)

## Concepts of Note
Patterns
- When executing ad hoc commands, you need to choose which managed nodes/groups you want to execute against. Patterns let you run commands and playbooks from specific hosts and/or groups in your inventory. They are highly flexible, use wildcards, regular expressions, and more. [Patterns: targeting hosts and groups — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/inventory_guide/intro_patterns.html#intro-patterns)

## Usage
  `ansible [host-pattern] -m [module] -a "[module-args]"` ;;; Ansible basic command 
  `ansible-playbooks thing.yml` ;;; Run an ansible playbook `thing.yml`
  `ansible-playbooks thing.yml --check` ;;; Dry-run an ansible playbook `thing.yml`



  doxygen
[Ansible CLI cheatsheet — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/command_guide/cheatsheet.html)
