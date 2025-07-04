---
company: Varex
tags: archive_deprecated/Varex
---
## Windows
```shell
./generate.bat
./build.bat
```
## Linux
```shell
./generate.sh
./build.sh
```

`generate.bat` is a cmake utility that lets us compile on multiple files from source
- Creates VS project files for our OS
- We don't have to run `build.bat`, we can just build 

`generate.sh` is on Linux
- Cross-compile is allowed from that

Within the `build/win64/test/tooele-sdk-tests.sln` folder
- Go to `win64` and `test`
- Double click it and it'll open in VS