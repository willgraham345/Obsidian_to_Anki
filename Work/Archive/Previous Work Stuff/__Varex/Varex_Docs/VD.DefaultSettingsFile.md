---
company: Varex
tags: archive_deprecated/Varex
---
- Description:
	- Subclass from [[VD.SettingsFileTests]]
	- Functional test
- Implementation:
	1. Instantiates a `VLogSettingsFile <shared_ptr>`
	2. Defines: `settings <shared_ptr<VlogSettingsFile>>`
	3. Calls `VloginitLogging` with `settings`
	- Fields:
	- Methods: