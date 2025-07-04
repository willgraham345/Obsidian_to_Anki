---
summary: Filters let you transform data. You can use ansible-specific filters, or any filters shipped with Jinja2. You can also use python methods to transform data.
type: note/concept
components: 
date created: Tuesday, March 18th 2025, 3:47:33 pm
date modified: Thursday, July 3rd 2025, 1:52:01 pm
tags: [command/ansible_yml/filtering]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[Using filters to manipulate data — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html)

## Concepts of Note
### Default values
Default value if the variable `<some_variable>` isn't defined.
```yaml
{{ some_variable | default(<def_value>) }}
```
- Note, you can also set the <def_value> to `omit` to get rid of this.

### Mandatory values
```yml
{{ variable | mandatory }}
```

### Converting Data types
Strings to lists
- [c] `{{ <variable> | split(',') }}` =  Built in filter to transform a character/string into a list of items suitable for looping. = #command/ansible_yml/filtering
<!--ID: 1751434091833-->

- [c] `{{ <dict> | dict2items }}` = Transform dictionary to lists = #command/ansible_yml/filtering = [Using filters to manipulate data — Ansible Community Documentation](https://docs.ansible.com/ansible/latest/playbook_guide/playbooks_filters.html)
<!--ID: 1751434091837-->

- [c] `{{ <list> | items2dict }}` = Transforms items to dictionary, mapping the contents into key/value pairs. = #command/ansible_yml/filtering 
<!--ID: 1751434091840-->

- [c] `{{ <var> | to_nice_json }}` = Formats variable in structure to json = #command/ansible_yml/filtering 
<!--ID: 1751434091844-->

- [c] `{{ <var> | to_nice_yaml }}` = Formats variable in structure to yaml = #command/ansible_yml/filtering 
<!--ID: 1751434091847-->

- [c] `{{ <var1> | zip(<var2>) | }}` = Combine list elements `var1` onto var2, similar to a tuple  = #command/ansible_yml/filtering 
<!--ID: 1751434091851-->

- [c] `{{ <var1> | map('extract', <var2>) | dataType }}` = Maps from a list of indices to a list of values from a container (hash or array). Similar to `var2[var1]` = #command/ansible_yml/filtering 
<!--ID: 1751434091856-->

- [c] `{{ <var1> | map('extract', <var2>, <var3>) | dataType }}` = Maps from a list of indices to a list of values from a container (hash or array). Similar to `var2[var1][var3]` = #command/ansible_yml/filtering 
<!--ID: 1751434091861-->

### JSON querying
If you have data like this:
```json
    "domain": {
        "cluster": [
            {
                "name": "cluster1"
            },
            {
                "name": "cluster2"
            }
        ],
        "server": [
            {
                "name": "server11",
                "cluster": "cluster1",
                "port": "8080"
            },
            {
                "name": "server12",
                "cluster": "cluster1",
                "port": "8090"
            },
            {
                "name": "server21",
                "cluster": "cluster2",
                "port": "9080"
            },
            {
                "name": "server22",
                "cluster": "cluster2",
                "port": "9090"
            }
        ],
        "library": [
            {
                "name": "lib1",
                "target": "cluster1"
            },
            {
                "name": "lib2",
                "target": "cluster2"
            }
        ]
    }
```

You can query it like this:
```yml
- name: Display all cluster names
  ansible.builtin.debug:
    var: item
  loop: "{{ domain_definition | community.general.json_query('domain.cluster[*].name') }}"

- name: Display all ports from cluster1
  ansible.builtin.debug:
    var: item
  loop: "{{ domain_definition | community.general.json_query(server_name_cluster1_query) }}"
  vars:
    server_name_cluster1_query: "domain.server[?cluster=='cluster1'].port"
```