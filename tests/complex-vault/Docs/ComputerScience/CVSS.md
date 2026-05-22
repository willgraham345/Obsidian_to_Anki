---
summary: Vulnerability modeling, but it seems to be very focused on rating individual attack vectors rather than everything at once.
headings: ["[[#Concepts of Note]]"]
type: note/concept
concept_of: ["[[Threat Modeling]]"]
date created: Wednesday, August 27th 2025, 4:26:05 pm
date modified: Thursday, September 4th 2025, 10:02:05 am
diagrams: ["[[CVSS-1.png]]", "[[CVSS-2.png]]", "[[CVSS-3.png]]", "[[CVSS-4.png]]", "[[CVSS-5.png]]", "[[CVSS-6.png]]", "[[CVSS-7.png]]", "[[CVSS.png]]"]
sources: ["[[@cvss4|NVD - CVSS v3 Calculator]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

[NVD - CVSS v3 Calculator](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator)

## Concepts of Note
- Base score metrics (measures severity, not risk)
	- Exploitability Metrics
	- Impact Metrics
- Temporal score metrics
- Environmental score metrics
	- Exploitability metrics
	- Impact metrics
	- Impact Subscore Modifiers

### Terms
󰙎  CVSS-B ;;; Base metrics within the CVSS framework. Measures severity, not risk. = #cs/security/threat-modeling/cvss
<!--ID: 1759415941298-->

󰙎  CVSS-BE ;;; Base and Environmental metrics within the CVSS framework. = #cs/security/threat-modeling/cvss
<!--ID: 1759415941302-->

󰙎  CVSS-BT ;;; Base and Threat metrics within the CVSS framework. = #cs/security/threat-modeling/cvss
<!--ID: 1759415941307-->

󰙎  CVSS-BTE ;;; Base and Threat and Environmental metrics within the CVSS framework. = #cs/security/threat-modeling/cvss
<!--ID: 1759415941312-->


### Scoring Rubrics
- ![[CVSS.png | 700]]
- ![[CVSS-1.png | 700]]
- ![[CVSS-2.png | 700]]
- ![[CVSS-3.png | 700]]
- ![[CVSS-4.png| 700]]
- ![[CVSS-5.png| 700]]
- ![[CVSS-6.png | 700]]
- ![[CVSS-7.png | 700]]

### Terms Glossary %% fold %% 
**Affected**: A system is affected by a vulnerability if a user or operator of the system must take action to remediate, mitigate, or otherwise address the vulnerability.[5](https://www.first.org/cvss/user-guide#fn:5) If a system is affected by a vulnerability, the CVSS v4.0 Base score must not be 0.0.

**Attacker**: A human person that “...attempts to evade security services and violate the security policy of a system. That is, an actual assault on system security….”[6](https://www.first.org/cvss/user-guide#fn:6), often but not always attempted by exploiting a vulnerability in the system. (Consistent with NIST [CSRC definitions](https://csrc.nist.gov/glossary/term/attacker), an attacker is a person.)

**Chained score**: The Base Score produced by scoring two or more chained vulnerabilities.

**Chained vulnerabilities**: See _Vulnerability Chaining_.

**Default credential**: Data such as a user name and password that is initially configured and allows authentication unless it has been changed. A default credential may be shared by many systems or unique to individual systems. A system may force a default credential to be changed.

**Hard-coded credential**: Data such as a user name and password that is always configured, always allows authentication, and cannot be changed or disabled.

**Proof-of-Concept exploit code:** Software or sufficient technical details that can be used to demonstrate the existence of a vulnerability.

**Privilege**: A collection of rights (typically read, write, and execute) granted to a user or user process which defines access to computing resources. The terms “privilege,” “permission,” and “authorization” are used interchangeably.[7](https://www.first.org/cvss/user-guide#fn:7)

**Published**: Any publicly, commercially, or socially available exploit code.

**Reasonable worst-case**: An instance of a plausible path to the exploitation of a vulnerability, the worst-case after any unreasonable high-impact low-likelihood paths have been discountedIt is not a prediction of what will happen, rather an illustration of what could reasonably be foreseen by an experienced analyst and that would require response action by a security professional or team.[8](https://www.first.org/cvss/user-guide#fn:8)

**Reported**: Based on applicable threat intelligence, activity targeting the vulnerability is known by someone other than the attacker and the victim.

**Resource**: Asset used or consumed during the execution of a process[.](https://www.iso.org/standard/63711.html)[9](https://www.first.org/cvss/user-guide#fn:9) Examples of resources include (but are not limited to) file contents, file identifiers, memory pointers, memory contents, CPU cycles, and network bandwidth.

**Security domain**: Set of assets and resources subject to a common security policy.[10](https://www.first.org/cvss/user-guide#fn:10)

**Security policy:** A set of policy rules (or principles) that direct how a system (or an organization) provides security services to protect sensitive and critical system resources.[11](https://www.first.org/cvss/user-guide#fn:11)

**Solutions to simplify**: Software that makes exploitation of the vulnerability trivial, including exploit frameworks, such as Metasploit or Cobalt Strike, or other tools that work reliably and against many different systems.

**System, information system:** An organized assembly of computing and communication resources and procedures — i.e., equipment and services, together with their supporting infrastructure, facilities, and personnel — that create, collect, record, process, store, transport, retrieve, display, disseminate, control, or dispose of information to accomplish a specified set of functions.[12](https://www.first.org/cvss/user-guide#fn:12) Uses of “system” means “Information system” unless otherwise specified. Information systems include, for example, IT systems, ICS systems, OT systems, computing hardware, and so on.

**Subsequent System**: A system whose security policy is violated as a result of the exploited vulnerability but that is not the Vulnerable System.

**Successful attack**: A successful attack (or successful exploit of a vulnerability) is a situation where an attacker violates the security policy of an information system.

**User**: An authorized human person. For CVSS, usually said of a person authorized to access a vulnerable system affected by the vulnerability being scored.

**Vulnerability**: A weakness or flaw in the functional behavior of an information system (software or hardware) that can be exploited, resulting in a negative impact to the Confidentiality, Integrity, and/or Availability of the vulnerable system or a subsequent system (that is, the violation of a security policy of an information system).[13](https://www.first.org/cvss/user-guide#fn:13)

**Vulnerability chaining**: The sequential exploitation of multiple vulnerabilities in order to attack an information system, where one or more exploits at the end of the chain requires the successful completion of prior exploits in order to be exploited.[14](https://www.first.org/cvss/user-guide#fn:14)

**Vulnerable System**: A system whose security policy is violated as the result of an exploited vulnerability and which contains the vulnerability.

[](https://www.first.org/cvss/user-guide#body)
