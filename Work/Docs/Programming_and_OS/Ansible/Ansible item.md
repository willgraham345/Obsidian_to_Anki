---
summary: A keyword in ansible, automatically created and populated by ansible in tasks which use loops.
type: note/component
component_of: ["[[Ansible playbook keywords]]"]
date created: Monday, March 17th 2025, 4:22:24 pm
date modified: Monday, March 17th 2025, 4:25:12 pm
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Examples
### For lists
The task will be run twice, first time with `item` set to `first`, second time with `second`
```yml
- debug:
    msg: "{{ item }}"
  with_items:
    - first
    - second
```

### For dictionaries
```yml
- debug:
    msg: "{{ item.my_value }}"
  with_items:
    - ny_element: first
      my_value: 1
    - my_element: second
      my_value: 2
```