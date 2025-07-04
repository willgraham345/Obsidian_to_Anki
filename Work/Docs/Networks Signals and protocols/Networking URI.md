---
type: note/component
component_of: ["[[Networking Terminology]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 11:33:53 am
---
# Background
URL is a similar concept to URIs. 
URI = uniform resource identifier
- Identify abstract or physical resources on the internet. 

## Syntax
Has 5 parts, but all other than two are optional.
1. **Scheme (required)**: Gives info about protocol being used
2. **Authority**: Identifies the domains
3. **Path (required)**: Shows the exact path to the resource
4. **Query**: Represents a request action
5. **Fragment**: Refers to a partial aspect of a resource

### Examples
All components are listed successively and separated by specific, predefined characters:
```
scheme :// authority path ? query # fragment
```

`//` slashes after first colon are only necessary if the *authority* part is filled. *Authority* can also contain user info that is detached from the domain's `@` symbol. 

Typical web address is a good example
 `"https://example.org/test/test1?search=test-question#part2"`
- _scheme_: https
- _authority_: example.org
- _path_: test/test1
- _query_: search=test-question
- _fragment_: part2
![[Pasted image 20240513162005.png | 300]]

# Usage
Best known schemes are: 
- **about**: Browser information
- **data**: Embedded data
- **feed**: Web feeds
- **file**: Files
- **ftp**: [File Transfer Protocol](https://www.ionos.com/digitalguide/server/know-how/file-transfer-protocol/ "File Transfer Protocol")
- **git**: Version management with Git
- **http**: [Hypertext Transfer Protocol](https://www.ionos.com/digitalguide/hosting/technical-matters/what-is-http/ "protocolo HTTP")
- **https:** [Hypertext Transfer Protocol Secure](https://www.ionos.com/digitalguide/hosting/technical-matters/what-is-https/ "What is HTTPS?")
- **imap:** Internet Message Access Protocol
- **mailto**: Email addresses
- **news**: Usenet newsgroups
- **pop**: POP3
- **rsync**: Data synchronization
- **sftp**: SSH File Transfer Protocol
- **ssh**: [Secure shell](https://www.ionos.com/digitalguide/server/tools/ssh-secure-shell/ "SSH: Secure Shell")
- **tel**: Telephone numbers
- **urn**: Uniform Resource Names