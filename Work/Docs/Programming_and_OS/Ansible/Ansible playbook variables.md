---
summary: Ansible requires values for all variables in templated expressions. You can make variables optional, as well as mandatory. Ansible will fail if a variable in your playbook or command is undefined.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
date created: Monday, March 17th 2025, 11:52:46 am
date modified: Monday, March 17th 2025, 12:07:01 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Using Variables — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html)

## Concepts of Note
### Referencing Simple Variables
After defining, use: something like `{{ <variableName> }}`
Make sure to surround the variable in `" "` if it is being used as the argument.

### Variable Precedence
1. command line values (for example, `-u my_user`, these are not variables)
2. role defaults (as defined in [Role directory structure](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#role-directory-structure)) [1](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id14)
3. inventory file or script group vars [2](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id15)
4. inventory group_vars/all [3](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id16)
5. playbook group_vars/all [3](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id16)
6. inventory group_vars/* [3](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id16)
7. playbook group_vars/* [3](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id16)
8. inventory file or script host vars [2](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id15)
9. inventory host_vars/* [3](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id16)
10. playbook host_vars/* [3](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id16)
11. host facts / cached set_facts [4](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_variables.html#id17)
12. play vars
13. play vars_prompt
14. play vars_files
15. role vars (as defined in [Role directory structure](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_reuse_roles.html#role-directory-structure))
16. block vars (only for tasks in block)
17. task vars (only for the task)
18. include_vars
19. set_facts / registered vars
20. role (and include_role) params
21. include params
22. extra vars (for example, `-e "user=my_user"`)(always win precedence

### Variables discovered from systems
There are types of variables that are discovered, not set by the user. These facts are derived from the remote system, with a complete set under the `ansible_facts` variable. Most facts are "injected" as top level variables preserving the `ansible_` prefix. 