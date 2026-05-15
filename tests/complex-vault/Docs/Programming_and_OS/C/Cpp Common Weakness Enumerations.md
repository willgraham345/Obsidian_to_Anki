---
summary: CWE is a bit like a class, and a CVE is an object
type: note/concept
associations: ["[["]
concept_of: ["[[Security and Cybersecurity]]"]
date created: Wednesday, February 26th 2025, 11:02:18 am
date modified: Wednesday, February 26th 2025, 11:09:47 am
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
[CWE - CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/)
1. Out of bounds write 
	1. [CWE - CWE-787: Out-of-bounds Write (4.16)](https://cwe.mitre.org/data/definitions/787.html)
	2. Local privilege elevation
2. Out of bounds read
	1. [CWE - CWE-125: Out-of-bounds Read (4.16)](https://cwe.mitre.org/data/definitions/125.html)
	2. Access to secret data
	3. Use tools (cppcheck and clang-tidy)
	4. Heartbleed leaked secrets
	5. Assume all input is malicious, and validate it accordingly. Make sure it is exactly as big as you think it is.
3. Use after free
	1. [CWE - CWE-416: Use After Free (4.16)](https://cwe.mitre.org/data/definitions/416.html)
	2. Another part of your app reads memory that was freed
	3. Privilege escalation in android
	4. Chrome free on one thread, continue using on another thread
	5. Set freed pointers to `nullptr`
4. Null pointer dereference
	1. [CWE - CWE-476: NULL Pointer Dereference (4.16)](https://cwe.mitre.org/data/definitions/476.html)
	2. Accessing memory through pointers that were set to `nullptr`
		1. Application crash, execution of unexpected code (rare)
	3. DOS attacks happen from this...
	4. Use cppcheck