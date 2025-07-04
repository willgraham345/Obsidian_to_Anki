---
company: Varex
tags: archive_deprecated/Varex
---
# Background
# Usage
## Within another project
All logging should be done through [[VD.VLOG_macros]]
### Creating, Retrieving, and Using Loggers
Methods `Vlog::createLogger()` and `Vlog::getLogger()` are used. Once the logger has been retrieved, logging macros can be used. You don't need to free loggers when it isn't needed. Loggers are tracked by shared pointers and will be destroyed when all references to the logger are out of scope. 
```cpp
Vlog::Logger logger = Vlog::get()->createLogger("logger");
VLOG_INFO(logger, "log message no data");
```
- Keep the logger returned by `Vlog:getLogger()` to reuse for logging. 
- Existing logger pointers can be copied safely to other scopes without calling `Vlog::getLogger()`

### Logging Data
Uses the `fmt` library for inserting data into log messages (similar to python f-strings)
```cpp
VLOG_ERROR(logger, "log message with data int={} string={}", 4, "blah");
// OR
VLOG_ERROR(logger, "positional formatted log message with data int={0} string={1} int again={0}", 22, "asdfajh");
```

### Log Severity
```cpp
Vlog::get()->setSeverity(logger, Vlog::Level::warn);
VLOG_TRACE(logger, "trace level message");
VLOG_DEBUG(logger, "debug level message");
VLOG_INFO(logger, "info level message");
VLOG_WARN(logger, "warn level message");
VLOG_ERROR(logger, "error level message");
VLOG_CRITICAL(logger, "critical level message");
```

From code, log severity can be set with `Vlog::setSeverity()`, but this is typically done by modifying the log settings file. 
