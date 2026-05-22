---
summary: GNU privacy guard, a CLI tool helpful for encryption/decryption through two asymmetric keys. Has a key management system with widely used features. Used primarily to encrypt/files and emails.
type: note/function
headings:
associations:
  - "[[Git config.ssh]]"
  - "[[Git config]]"
date created: Friday, November 1st 2024, 4:29:59 pm
date modified: Tuesday, February 17th 2026, 6:45:15 pm
tags: [tools/gdb]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[A dive into GPG and SSH. | Ayush Gupta](https://www.isitayush.dev/blog/ssh-vs-gpg)
[Using GPG keys | Bitbucket Data Center 8.19 | Atlassian Documentation](https://confluence.atlassian.com/bitbucketserver0819/using-gpg-keys-1416825860.html)

# Usage
 - [p] `gpg --full-generate-key` = Generate a public and private key with gpg interactively.  = 
 - [p] `gpg --clearsign doc.txt` = Sign doc.txt without encryption, (will write output to `doc.txt.asc` = 
 - [p] `gpg --import public.gpg` = Import a public key. = 
 - [p] `gpg --export --armor `