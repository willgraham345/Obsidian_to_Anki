---
company: Varex
tags:
  - archive_deprecated/Varex
  - archive_deprecated/Varex/config
---
# Background
Holds TONS of example repositories

## Configuration Files
- `.dat`
- Usually token-value pair based file. 
	- Exceptions to this are sections which deal with hardware, CP or VCP registers, and DACs
- The type of token instructs that parser on technique for reading the value associated with it. 
	- There are only two basic types of values so this is easy
	- Integers can also represent enumerated and booleans
- Values are either integer or string (byte-arrays)

### Naming Scheme
`<partNumber>_<customerName>_`
`<SAP#>`

# Usage