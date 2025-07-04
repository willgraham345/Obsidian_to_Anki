---
summary: Simplest way to automate repeating tasks in reusable and consistent config files. Defined in YAML and contain any ordered set of steps to be executed on our managed nodes. At a minimum a playbook should define the managed nodes to target and some tasks to run against them.
type: note/concept
components:
  - "[[Ansible roles]]"
  - "[[Ansible playbook keywords]]"
headings:
  - "[[#Examples]]"
date created: Thursday, March 13th 2025, 6:13:47 pm
date modified: Monday, March 17th 2025, 10:45:45 am
concepts:
  - "[[Ansible playbook variables]]"
  - "[[Ansible playbook become]]"
  - "[[Ansible playbook filtering and data conversion]]"
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
1. Top section
	- defines the group of hosts to execute the playbook
2. Tasks
	- Contains info about task and module to be executed
3. Variables
	- Can be defined at more than one level
To avoid listing the location of our inventory file every time, we can define a location 

### Templating
Ansible uses Jinja2 to enable dynamic expressions and access to variables and facts. For more information, see the [[Ansible builtin template]] module.

## Examples
```yaml
---
- name: Intro to Ansible Playbooks
  hosts: all

  tasks:
  - name: Copy file hosts with permissions
    ansible.builtin.copy:
      src: ./hosts
      dest: /tmp/hosts_backup
      mode: '0644'
  - name: Add the user 'bob'
    ansible.builtin.user:
      name: bob
    become: yes
    become_method: sudo
  - name: Upgrade all apt packages
    apt:
      force_apt_get: yes
      upgrade: dist
    become: yes
```