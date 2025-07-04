---
company: Varex
tags: archive_deprecated/Varex
---
# VD SettingsFileTests
`<testing_suite>`
- Overview
	- Fixture for tests for other tests to inherit and edit
	- Tests start with no log file, and remove earlier test files. 
- `protected` 
	- Methods:
		- `createTestLogSettingsFile()` 
			- [[#createTestLogSettingsFile]]
		- `SetUp()`
		- `TearDown()`
	- Attributes:
		- `maxNbrTestLogFiles`
		- `logOutputFile : str = "logfile.txt"`
		- `logSettingsDefaultTestFile : str = "LogSettings.txt"`
		- `logSettingsFileSettingsFilePartialWildcardTest : str = "SettingsFileTests-SettingsFilePartialWildcard.txt`

### createTestLogSettingsFile
Overview:
- Method that sets up the test logging
Inputs
- `testLogSettingsFileName` = Name of existing Log Settings File
- `numLogFiles` = Test File Number of Log Files
- `maxLogFileSize`
- `relaodFreqInSec`
- `format` = Test File Logging Format
- `VlogSettingsFile::LoggerSeverityMap & newSeverityMap` = Test file list of Loggers and Logging Severity for each Logger

#### Assertions
1. Number of log files is zero
2. Max log file output was zero
3. Check settings file changes