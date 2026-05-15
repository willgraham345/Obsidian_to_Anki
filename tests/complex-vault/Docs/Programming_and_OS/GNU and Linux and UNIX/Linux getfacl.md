---
type: note/tool
ai_generated: true
tags:
  - linux/permissions
date created: Friday, March 27th 2026, 12:00:00 pm
date modified: Friday, March 27th 2026, 12:00:00 pm
similar:
  - "[[Linux chmod]]"
  - "[[Linux chown]]"
uses:
  - "[[Linux File Permissions]]"
---

# Summary
󰙎 `getfacl` ;;; Display file Access Control Lists (ACLs) — extended per-user/group permissions beyond standard POSIX `rwx`

# Additional Background

## Concepts of Note

### ACLs vs Standard Permissions

Standard POSIX permissions assign `rwx` to exactly three entities: owner, group, others. ACLs extend this by allowing arbitrary additional user/group entries on a file.

| | Standard (`chmod`) | ACL (`getfacl`/`setfacl`) |
|---|---|---|
| Granularity | owner, group, others | any user or group |
| Visibility | `ls -l` | `getfacl` only |
| Storage | inode | extended attributes |

- 󰙎 `mask` ;;; ACL entry that caps the effective permissions of named users/groups (does not affect owner or other)
- 󰙎 `effective rights` ;;; actual permissions after the mask is applied; shown as `#effective:...` in output

### Output Format

```
# file: example.txt
# owner: alice
# group: devs
user::rw-
user:bob:r--
group::r--
mask::r--
other::---
```

Each line is an ACL entry: `tag:qualifier:permissions`.

## Usage

- [p] `getfacl <file>` ;;; show ACL for a file or directory
- [p] `getfacl -R <dir>` ;;; recursive — show ACLs for all files under a directory
- [p] `getfacl -e <file>` ;;; show effective rights after mask is applied
- [p] `getfacl -p <file>` ;;; absolute path mode — omit leading `/` strip (used for portable restore)
- [p] `getfacl --omit-header <file>` ;;; suppress `# file / # owner / # group` comment lines
- [p] `getfacl -R <dir> > acls.txt` ;;; backup ACLs for an entire directory tree
- [p] `setfacl --restore=acls.txt` ;;; restore ACLs from a backup produced by `getfacl -R`
