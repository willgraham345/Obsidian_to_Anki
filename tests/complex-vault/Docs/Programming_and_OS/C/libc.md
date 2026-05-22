---
type: hub
headings:
functions:
  - "[[libc functions]]"
up:
  - "[[Programming_and_OS Hub]]"
similar:
  - "[[dbus_messages]]"
next:
  - "[[Cpp std]]"
associations:
  - "[[C Memory in a C Program Overview]]"
  - "[[C Mutex]]"
  - "[[C Threads]]"
date created: Wednesday, March 18th 2026, 12:00:00 pm
date modified: Thursday, April 2nd 2026, 11:50:52 am
items:
  - "[[libc errno]]"
  - "[[libc gnu extensions]]"
  - "[[libc math]]"
  - "[[libc posix extensions]]"
  - "[[libc pthread]]"
  - "[[libc signal]]"
  - "[[libc stdio]]"
  - "[[libc stdlib]]"
  - "[[libc string]]"
  - "[[libc sys]]"
  - "[[libc unistd]]"
library_of:
  - "[[C]]"
  - "[[Cpp]]"
  - "[[Linux]]"
tags: [programming/c, programming/c/stdlib]
template:
template-version:
---

# Summary
󰙎 glibc ;;; GNU implementation of the C standard library; default libc on Linux; provides syscall wrappers, POSIX APIs, and GNU extensions

# Additional Background
glibc (GNU C Library) is the foundational userspace library on virtually every Linux system. It sits between application code and the kernel: C standard calls (e.g. `printf`, `malloc`) compile against glibc, which either handles them in userspace or issues the appropriate Linux syscall via the kernel ABI. Every process on a glibc-based Linux system is implicitly linked to `libc.so.6`.

## Concepts of Note

### Relationship to the Linux Kernel
glibc is not part of the kernel — it is a userspace library. It wraps Linux syscalls through a thin assembly trampoline (`syscall` instruction on x86-64), translating C-level calls into kernel entry points.

󰠗 What sits between a `read()` call and the kernel? ;; glibc — it issues the `read` syscall via the kernel ABI using the `syscall` instruction

󰠗 What shared object does glibc ship as? ;; `libc.so.6` — the `.6` reflects the ABI major version frozen since glibc 2.0

### Symbol Versioning
glibc uses ELF symbol versioning (`@@GLIBC_2.x`) to maintain ABI compatibility across releases. A binary linked against glibc 2.17 runs on any later glibc without recompilation.

󰙎 symbol versioning ;;; ELF mechanism tagging each exported symbol with the glibc version that introduced it; enables forward-compatible binaries

 `objdump -p /lib/x86_64-linux-gnu/libc.so.6 | grep GLIBC` ;;; list all GLIBC version nodes exported by the installed libc

### Checking the Installed Version
 `ldd --version` ;;; print glibc version (first line of output)
 `getconf GNU_LIBC_VERSION` ;;; print glibc version via POSIX conformance interface
 `__GLIBC__` / `__GLIBC_MINOR__` ;;; preprocessor macros exposing major/minor version at compile time

### Header Areas

| Header | Domain |
|---|---|
| `stdio.h` | Buffered I/O — `printf`, `fopen`, `fread`, `fwrite`, `fgets` |
| `stdlib.h` | Memory, process control — `malloc`, `free`, `exit`, `qsort`, `atoi` |
| `string.h` | Byte/string ops — `memcpy`, `memmove`, `strlen`, `strcpy`, `strtok` |
| `math.h` | Floating-point math — `sin`, `cos`, `sqrt`, `pow`; link with `-lm` |
| `unistd.h` | POSIX process/IO — `read`, `write`, `fork`, `exec`, `getpid`, `close` |
| `errno.h` | Error reporting — global `errno` variable; `strerror`, `perror` |
| `signal.h` | Signal handling — `signal`, `sigaction`, `kill`, `sigprocmask` |
| `pthread.h` | POSIX threads — `pthread_create`, `pthread_mutex_lock`; link with `-lpthread` |
| `sys/socket.h` | BSD socket API — `socket`, `bind`, `connect`, `send`, `recv` |
| `sys/mman.h` | Memory mapping — `mmap`, `munmap`, `mprotect` |
| `sys/stat.h` | File metadata — `stat`, `fstat`, `chmod` |
| `sys/wait.h` | Child-process reaping — `wait`, `waitpid` |

### POSIX Extensions
glibc implements the full POSIX.1-2017 standard (feature-test macro: `_POSIX_C_SOURCE`). Adds APIs beyond ISO C: `pread`/`pwrite`, `openat`, `clock_gettime`, `sem_*`, directory streams.

󰙎 feature-test macro ;;; `#define _POSIX_C_SOURCE 200809L` before any include; controls which declarations glibc exposes

### GNU Extensions
`_GNU_SOURCE` (gcc default on Linux) unlocks non-standard APIs: `asprintf`, `getline`, `memmem`, `qsort_r`, `pthread_setname_np`, `memfd_create`, the `err.h` family.

 `#define _GNU_SOURCE` ;;; enable all GNU + POSIX extensions; supersedes `_POSIX_C_SOURCE` and `_BSD_SOURCE`

## Usage

### Linking
Most glibc components are in `libc.so.6` and linked automatically. Exceptions:

| Library | Flag | Contents |
|---|---|---|
| `libm` | `-lm` | `math.h` floating-point functions |
| `libpthread` | `-lpthread` | `pthread.h` threading primitives |
| `librt` | `-lrt` | POSIX real-time extensions (`shm_open`, `mq_*`) |
| `libdl` | `-ldl` | Dynamic loading (`dlopen`, `dlsym`) |

### Static vs Dynamic Linking
Dynamic (default): binary contains a `PT_INTERP` ELF segment pointing to `/lib64/ld-linux-x86-64.so.2`. Static (`-static`): bundles glibc into the binary; loses symbol-versioning portability.

󰠗 How do you statically link glibc? ;; Pass `-static` to gcc/ld; the resulting binary has no external libc dependency but is tied to the glibc version at build time

## Flashcards

󰠗 What is glibc? ;; GNU implementation of the ISO C standard library; default libc on Linux; ships as `libc.so.6`
󰠗 Which header provides POSIX thread primitives? ;; `pthread.h`; link with `-lpthread`
󰠗 How does glibc invoke Linux syscalls? ;; Via the `syscall` instruction (x86-64) — glibc wraps kernel entry points in thin C-callable stubs
󰠗 What does `_GNU_SOURCE` unlock? ;; All GNU and POSIX extensions in glibc headers — e.g. `asprintf`, `getline`, `memfd_create`
󰠗 How do you check the runtime glibc version? ;; `ldd --version` or `getconf GNU_LIBC_VERSION`
