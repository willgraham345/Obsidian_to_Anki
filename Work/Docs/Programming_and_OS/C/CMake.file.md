---
type: note
---
# Background
Command dedicated to file and file path manipulation requiring access to the filesytem.

# Usage
## Syntax
```cmake
Reading
  file(READ <filename> <out-var> [...])
  file(STRINGS <filename> <out-var> [...])
  file(<HASH> <filename> <out-var>)
  file(TIMESTAMP <filename> <out-var> [...])
  file(GET_RUNTIME_DEPENDENCIES [...])

Writing
  file({WRITE | APPEND} <filename> <content>...)
  file({TOUCH | TOUCH_NOCREATE} <file>...)
  file(GENERATE OUTPUT <output-file> [...])
  file(CONFIGURE OUTPUT <output-file> CONTENT <content> [...])

Filesystem
  file({GLOB | GLOB_RECURSE} <out-var> [...] <globbing-expr>...)
  file(MAKE_DIRECTORY <directories>...)
  file({REMOVE | REMOVE_RECURSE } <files>...)
  file(RENAME <oldname> <newname> [...])
  file(COPY_FILE <oldname> <newname> [...])
  file({COPY | INSTALL} <file>... DESTINATION <dir> [...])
  file(SIZE <filename> <out-var>)
  file(READ_SYMLINK <linkname> <out-var>)
  file(CREATE_LINK <original> <linkname> [...])
  file(CHMOD <files>... <directories>... PERMISSIONS <permissions>... [...])
  file(CHMOD_RECURSE <files>... <directories>... PERMISSIONS <permissions>... [...])

Path Conversion
  file(REAL_PATH <path> <out-var> [BASE_DIRECTORY <dir>] [EXPAND_TILDE])
  file(RELATIVE_PATH <out-var> <directory> <file>)
  file({TO_CMAKE_PATH | TO_NATIVE_PATH} <path> <out-var>)

Transfer
  file(DOWNLOAD <url> [<file>] [...])
  file(UPLOAD <file> <url> [...])

Locking
  file(LOCK <path> [...])

Archiving
  file(ARCHIVE_CREATE OUTPUT <archive> PATHS <paths>... [...])
  file(ARCHIVE_EXTRACT INPUT <archive> [...])
```

### Filesystem
#### Globbing
```cmake
file(GLOB <variable> [LIST_DIRECTORIES true|false] [RELATIVE <path>] [CONFIGURE_DEPENDS]
	<globbing-expressions>...)
file(GLOB_RECURSE <variable> [FOLLOW_SYMLINKS] [LIST_DIRECTORIES true|false] [RELATIVE <path>]
	[CONFIGURE_DEPENDS] <globbing-expressions>...)
```
- Generates a list of files that matches the `<globbing-expression>` and stores it into the `<variable>`. 
	- `GLOB_RECURSE` mode will traverse all subdirectories of the matched directory and match the files. Subdirectories are only traversed if `FOLLOW_SYMLINKS` is given.
- They don't recommend using GLOB to collect a list of source files from the source tree. If no CMakeLists.txt file changes when a source is added/removed, the generated build system cannot know when to ask CMake to regenerate. d

| Example Globbing Expressions | Results                                          |
| ---------------------------- | ------------------------------------------------ |
| `*.cxx`                      | match all files with extension `cxx`             |
| `*.vt?`                      | match all files with extension `vta`, ..., `vtz` |
| `f[3-5].txt`                 | match files `f3.txt`, `f4.txt`, `f5.txt`         |
