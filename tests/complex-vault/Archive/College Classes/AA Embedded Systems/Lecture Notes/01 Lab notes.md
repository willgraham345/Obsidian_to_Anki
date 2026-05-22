# Prelab Notes
"Code without tests is bad code. It doesn’t matter how well written it is; it doesn’t matter how pretty or object-oriented or well-encapsulated it is. With tests, we can change the behavior of our code quickly and verifiably. Without them, we really don’t know if our code is getting better or worse."

Michael C. Feathers, Working Effectively with Legacy Code

## Different Components of the PlatformIO Organization
### Platforms - Microcontroller Architecture
- PlatformIO has decentralized architecture, with lots of different platforms. 
- A platform is usually a particular microcontroller or processor architecture that PlatformIO projects can be compiled to run on. 
	- Has pre-configured presets for embedded circuit boards
	- Pre-compiled toolchains and related tools for the architecture
- You specify the platform using the `platform` option on platformio.ini
	- [Platforms supported](https://docs.platformio.org/en/latest/platforms/index.html)
	- You can also specify a custom board

### Framework - Operating System or core HAL Libraries
- [Frameworks](https://docs.platformio.org/en/latest/frameworks/index.html)
	- Arduino, FreeRTOS, STM32Cube

### Package - an installable library
- PlatformIO manages dependencies really well.
	- See a list of [popular libraries](https://registry.platformio.org/search?t=library&s=trending) with how to add them to the project
	- Search with `pio pkg search` from cli
- Supports different library sources for declaring dependencies. 

##### Example
``` ini
; Common dependencies declared in the common "[env]" section
[env]
platform = ...
board = ...
framework = ...
lib_deps =
  dep_1
  dep_2

[env:release]
build_flags = -D RELEASE=1

; Specific dependencies that extend the common dependencies
[env:debug]
lib_deps =
  ${env.lib_deps}
  dep_3
```
`dep_1` and `dep_2` are common to the `release` and `debug` working environments, while `dep_3` is specific only for the `debug` working environment. 

`env:debug` overrides common `lib_deps` option and the `${env.lib_deps}`. 

### Board - A configuration for a specific development board


# Links for all this stuff:
Platforms - the microcontroller architecture [https://docs.platformio.org/en/latest/platforms/index.html](https://docs.platformio.org/en/latest/platforms/index.html)
Framework - the operating system or core HAL libraries [https://docs.platformio.org/en/latest/frameworks/index.html](https://docs.platformio.org/en/latest/frameworks/index.html)
Package - an installable library [https://docs.platformio.org/en/latest/librarymanager/dependencies.html](https://docs.platformio.org/en/latest/librarymanager/dependencies.html)
Board - a configuration for a specific development board. [https://docs.platformio.org/en/latest/boards/index.html](https://docs.platformio.org/en/latest/boards/index.html)



