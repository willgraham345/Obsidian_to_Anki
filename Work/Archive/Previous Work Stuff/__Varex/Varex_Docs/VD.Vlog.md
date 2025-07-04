---
company: Varex
tags: archive_deprecated/Varex
---
# Vlog
- Overview:
	- Tooele's logging class

## Members
### Public 
#### Types
- `Logger : typedef std::shared_ptr<spdlog::logger>`
- `Level : typedef spdlog::level::level_enum`

#### Member Functions
- `getSettings() : VlogSettingsInterface *`
- `createLogger() : Logger`
- `getLogger() : Logger`
- `flush(Logger logger) : void`
	- Flushes pending messages

##### Static public member functions
- `initLogging(std::shared_ptr<VlogSettingsInterface> s) : static Vlog *`
	- Has a few different implementations

#### Attributes
- `error : Nano::Signal<void()>`
- `critical : Nano::Signal<void()>`

### Private
#### Constructors
- Has a couple [[#VLog Constructors]]

#### Attributes
- `settings : std::shared_ptr<VlogSettingsInterface>`
- `logfileSink : LogSink`

##### Static private attributes
- `inst : static Vlog*`
	- Singleton instance
- `initMutex : std::mutex`
	- mutex for initDone
- `FLUSH_PERIOD`
- `QUEUE_SIZE = 256`

## VLog Constructors
![[Pasted.Image.20240613145701_233.png| 300]]

