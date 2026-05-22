---
summary: POSIX/Linux typedef aliases for system-call interfaces, defined in <sys/types.h> and related headers; provide stable, architecture-independent types.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Flashcards]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
concept_of:
  - "[[Linux File Permissions]]"
  - "[[Linux Processes]]"
  - "[[UNIX File Descriptor]]"
date created: Tuesday, March 17th 2026, 3:17:00 pm
date modified: Tuesday, March 17th 2026, 3:25:11 pm
tags: [cs/linux/kernel/syscall, cs/posix/types]
template:
template-version:
used_by:
  - "[[Networking Berkeley Sockets|BSD sockets]]"
---

# Summary
󰙎 system_data_types ;;; POSIX/Linux typedef aliases (`pid_t`, `off_t`, `size_t`, etc.) that abstract underlying integer widths, ensuring portability across 32/64-bit architectures. Documented in `man 7 system_data_types`.

# Additional Background

## Concepts of Note
- Primary header: `<sys/types.h>`; supplemented by `<stdint.h>`, `<time.h>`, `<signal.h>`, `<unistd.h>`, `<sys/socket.h>`, `<pthread.h>`
- Underlying types vary by arch (LP64 vs ILP32); typedef aliases keep call sites stable
- `off_t` is 32-bit by default on 32-bit systems; define `_FILE_OFFSET_BITS=64` before includes for large-file support (LFS)
- No fixed `printf` specifier for most types — cast to `long`/`unsigned long` and use `%ld`/`%lu`, or use `PRId64` from `<inttypes.h>` for `int64_t`

## Properties
### classes

##### pid_t
󰫧 :
- description: Process ID
- type: `int`
- header: `<sys/types.h>`
󰫧 end:

##### uid_t
󰫧 :
- description: User ID
- type: `unsigned int`
- header: `<sys/types.h>`
󰫧 end:

##### gid_t
󰫧 :
- description: Group ID
- type: `unsigned int`
- header: `<sys/types.h>`
󰫧 end:

##### off_t
󰫧 :
- description: File offset; 32-bit by default on 32-bit systems, promoted to 64-bit with LFS
- type: `long` (or `long long` with `_FILE_OFFSET_BITS=64`)
- header: `<sys/types.h>`
󰫧 end:

##### size_t
󰫧 :
- description: Unsigned object size / allocation count
- type: `unsigned long`
- header: `<stddef.h>` / `<sys/types.h>`
󰫧 end:

##### ssize_t
󰫧 :
- description: Signed byte count; −1 on error
- type: `long`
- header: `<sys/types.h>`
󰫧 end:

##### time_t
󰫧 :
- description: Calendar time as seconds since the Unix epoch
- type: `long`
- header: `<time.h>`
󰫧 end:

##### clock_t
󰫧 :
- description: Processor time in clock ticks
- type: `long`
- header: `<time.h>`
󰫧 end:

##### mode_t
󰫧 :
- description: File permission and type bits
- type: `unsigned int`
- header: `<sys/types.h>`
󰫧 end:

##### dev_t
󰫧 :
- description: Device number encoding major + minor device identifiers
- type: `unsigned long`
- header: `<sys/types.h>`
󰫧 end:

##### ino_t
󰫧 :
- description: Inode number
- type: `unsigned long`
- header: `<sys/types.h>`
󰫧 end:

##### nlink_t
󰫧 :
- description: Hard link count
- type: `unsigned long`
- header: `<sys/types.h>`
󰫧 end:

##### blksize_t
󰫧 :
- description: Preferred I/O block size
- type: `long`
- header: `<sys/types.h>`
󰫧 end:

##### blkcnt_t
󰫧 :
- description: Count of 512-byte blocks allocated to a file
- type: `long`
- header: `<sys/types.h>`
󰫧 end:

##### socklen_t
󰫧 :
- description: Length of a socket address structure
- type: `unsigned int`
- header: `<sys/socket.h>`
󰫧 end:

##### sigset_t
󰫧 :
- description: Signal set; opaque bitmask used with `sigprocmask`, `sigaction`, etc.
- type: opaque struct (typically `unsigned long` array internally)
- header: `<signal.h>`
󰫧 end:

##### pthread_t
󰫧 :
- description: POSIX thread handle
- type: `unsigned long`
- header: `<pthread.h>`
󰫧 end:

##### pthread_mutex_t
󰫧 :
- description: Mutex synchronisation object; opaque — must be initialized via `pthread_mutex_init` or `PTHREAD_MUTEX_INITIALIZER`
- type: opaque struct
- header: `<pthread.h>`
󰫧 end:

##### pthread_cond_t
󰫧 :
- description: Condition variable; opaque — used with `pthread_cond_wait` / `pthread_cond_signal`
- type: opaque struct
- header: `<pthread.h>`
󰫧 end:

##### intptr_t
󰫧 :
- description: Signed integer guaranteed wide enough to hold a pointer value
- type: `long`
- header: `<stdint.h>`
󰫧 end:

##### uintptr_t
󰫧 :
- description: Unsigned integer guaranteed wide enough to hold a pointer value
- type: `unsigned long`
- header: `<stdint.h>`
󰫧 end:

##### ptrdiff_t
󰫧 :
- description: Result type of subtracting two pointers
- type: `long`
- header: `<stddef.h>`
󰫧 end:

##### suseconds_t
󰫧 :
- description: Microseconds field of `struct timeval`
- type: `long`
- header: `<sys/types.h>`
󰫧 end:

## Usage

```c
#include <sys/types.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>

pid_t pid = getpid();
printf("pid: %ld\n", (long)pid);

int fd = open("file.bin", O_RDONLY);
off_t pos = lseek(fd, 0, SEEK_END);
printf("size: %ld bytes\n", (long)pos);
```

`(long)pid` ;;; Cast `pid_t` to `long` before `%ld` — no dedicated printf specifier for POSIX typedefs
`_FILE_OFFSET_BITS=64` ;;; Compile-time macro that promotes `off_t` to 64 bits on 32-bit systems; define before any includes

## Flashcards
󰠗 What header is the primary source for POSIX system data types? ;; `<sys/types.h>`
󰠗 Why cast `pid_t` to `long` for printf? ;; No fixed printf conversion specifier exists for POSIX typedefs; `long` is the widest safe match on LP64
󰠗 How do you enable 64-bit `off_t` on a 32-bit Linux build? ;; Define `_FILE_OFFSET_BITS=64` before any includes (or pass `-D_FILE_OFFSET_BITS=64` to the compiler)
󰠗 Which type holds a signal set for `sigprocmask`? ;; `sigset_t` from `<signal.h>`
󰠗 What distinguishes `size_t` from `ssize_t`? ;; `size_t` is unsigned (object sizes, allocation counts); `ssize_t` is signed (byte counts that may be -1 on error)
