---
summary: Dependency manager through a variety of yaml files. Requires python 3.8.
type: note/system
headings:
concepts: ["[[Ansible keywords]]", "[[Ansible playbooks]]"]
date created: Thursday, March 13th 2025, 5:57:31 pm
date modified: Sunday, December 14th 2025, 2:52:48 pm
libraries: ["[[Ansible builtin]]"]
tags: [tools/ansible]
template:
template-version:
tools: ["[[Ansible CLI tools]]", "[[Ansible-pull]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
󰙎 Playbooks ;; An ordered list of tasks along with its necessary parameters that define a recipe to configure a system. See [[Ansible playbooks]]

󰙎 Roles ;; Redistributable units of organization that allow users to share automation code easier. See [[Ansible roles]]

󰙎 Tasks ;; Units of action that combine a module and its arguments along with some other parameters. See [[Ansible tasks]]

󰙎 Inventory ;; (doesn't apply if only managing one machine) A collection of all the hosts and groups that Ansible manages. Could be a static file in the simple cases or we can pull the inventory from remote sources, such as cloud providers.

󰙎 Host ;; A remote machine managed by Ansible.

󰙎 Group ;; Several hosts grouped together that share a common attribute.

󰙎 Modules ;; Units of code that Ansible sends to the remote nodes for execution.


󰙎 YAML ;; A popular and simple data format that is very clean and understandable by humans.

