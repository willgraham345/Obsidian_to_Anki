# Duplicate Note Report

Generated from live DB query. Last updated: 2026-04-20.

---

## DB Status Summary

| Status | Count |
|--------|-------|
| synced | 2946 |
| not_in_anki (pending add) | 1560 |
| stale_id (pending re-add) | 174 |
| modified (pending update) | 49 |
| orphan_in_anki (in Anki, no vault match) | 35 |

---

## Part 1 — Obsidian Files with Duplicate Note Content

These vault files have the same flashcard `field_1` content appearing 2+ times.
Most have a **1:1 duplicate ratio** — likely caused by **content being accidentally
doubled** in the file (Obsidian sync conflict, copy-paste). A few (Docker Compose,
Berkeley Sockets) have notes appearing 3–6x because the same keyword appears in
multiple spec sections.

**Action:** Open each file in Obsidian and remove the duplicate notes. After
cleaning, re-run `scan.py --vault` and `scan.py --anki` to rebuild the DB.

> `dup_note_count` = distinct `field_1` values that appear more than once.
> `extra_copies` = total redundant rows (total − 1 per unique value).

| File | Dup note count | Extra copies |
|------|---------------|-------------|
| Docs/Terminology Sheet.md | 136 | 136 |
| Docs/Programming_and_OS/Docker/Docker Compose spec.md | 46 | 69 |
| Docs/Programming_and_OS/SQL/SQLite.md | 32 | 54 |
| Docs/Networks_Signals_Protocols/Networking Berkeley Sockets.md | 25 | 42 |
| Docs/ComputerScience/DP Testing Dependency Injection.md | 21 | 39 |
| Docs/Programming_and_OS/C/Cpp gtest Assertions.md | 24 | 37 |
| Docs/Programming_and_OS/Python/Python Docker SDK.md | 32 | 32 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux groups.md | 30 | 30 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux systemd directives.md | 29 | 29 |
| Docs/ComputerScience/DP Type Erasure.md | 26 | 26 |
| Docs/Programming_and_OS/C/Cpp std chrono.md | 24 | 24 |
| Docs/Software/openc3/CS packet.md | 23 | 23 |
| Docs/Programming_and_OS/SQL/SQLite Cpp Interface.md | 15 | 23 |
| Docs/Software/Postgres/Postgres.md | 15 | 22 |
| Docs/Programming_and_OS/C/Cpp gtest Mocking.md | 21 | 21 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/rsync.md | 21 | 21 |
| Docs/Software/openc3/openc3 interfaces.md | 20 | 20 |
| Docs/Programming_and_OS/C/Cpp std memory shared_ptr.md | 12 | 20 |
| Docs/Programming_and_OS/Bash/Bash set command.md | 10 | 20 |
| Docs/Programming_and_OS/Docker/Docker Dockerfile.md | 17 | 19 |
| Docs/Programming_and_OS/C/Cpp CLI11.md | 19 | 19 |
| Docs/ComputerScience/CS Bitmask.md | 19 | 19 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/GNU make rules.md | 9 | 17 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Buildroot.md | 15 | 17 |
| Docs/Programming_and_OS/C/Cpp pointers.md | 12 | 16 |
| Docs/Networks_Signals_Protocols/PTP Server.md | 16 | 16 |
| Docs/Programming_and_OS/SQLite/Usage/sqlite_usage.md | 10 | 15 |
| Docs/Programming_and_OS/Debuggers/gdb.md | 15 | 15 |
| Docs/Programming_and_OS/Bash/Bash Basics.md | 8 | 15 |
| Docs/Programming_and_OS/Python/Python importlib.md | 14 | 14 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/dbus_messages.md | 14 | 14 |
| Docs/Programming_and_OS/C/Cpp gtest Matchers.md | 14 | 14 |
| Docs/Programming_and_OS/C/CMake target_link_libraries.md | 7 | 14 |
| Docs/Programming_and_OS/C/Cpp std memory unique_ptr.md | 12 | 13 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/GNU make.md | 12 | 12 |
| Docs/Programming_and_OS/C/Cpp preprocessor directives.md | 12 | 12 |
| Docs/Programming_and_OS/C/CMake file_sets.md | 8 | 12 |
| Docs/Software/openc3/openc3 command configuration.md | 11 | 11 |
| Docs/ComputerScience/CS Binary Storage.md | 11 | 11 |
| Docs/Programming_and_OS/Rust/Rust Generics.md | 10 | 10 |
| Docs/Programming_and_OS/C/Cpp interface.md | 4 | 10 |
| Docs/Programming_and_OS/C/Cpp condition_variable condition_variable.md | 10 | 10 |
| Docs/Networks_Signals_Protocols/PTP Classes.md | 10 | 10 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux apt.md | 9 | 9 |
| Docs/Programming_and_OS/C/CMake cmake_parse_arguments.md | 3 | 9 |
| Docs/Networks_Signals_Protocols/Networking CRC.md | 9 | 9 |
| Docs/ComputerScience/DP Principles.md | 6 | 9 |
| Docs_Research_Industry/research_citations/@jiangenterprise2024.md | 8 | 8 |
| Docs/Software/Postgres/Postgres Architecture.md | 5 | 8 |
| Docs/Programming_and_OS/Rust/Rust writing a macro.md | 3 | 8 |
| Docs/Programming_and_OS/Python/Python Scoping Rules.md | 8 | 8 |
| Docs/Programming_and_OS/Markdown and Configuration/YAML.md | 8 | 8 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux systemd unit.md | 8 | 8 |
| Docs/Programming_and_OS/C/Cpp templates.md | 8 | 8 |
| Docs/Programming_and_OS/C/Cpp std memory weak_ptr.md | 8 | 8 |
| Docs/Networks_Signals_Protocols/TCP Protocol Suite.md | 8 | 8 |
| Docs/Programming_and_OS/Python/Python OOP.md | 7 | 7 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Networking/Linux syscall networking.md | 7 | 7 |
| Docs/Programming_and_OS/C/Cpp functions.md | 7 | 7 |
| Docs/ComputerScience/CS Endianness.md | 4 | 7 |
| TagPages/cybersecurity_Tags.md | 6 | 6 |
| Docs/Programming_and_OS/Rust/Rust std attribute macros.md | 3 | 6 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux journalctl.md | 6 | 6 |
| Docs/Programming_and_OS/C/Cpp std function.md | 6 | 6 |
| Docs/Programming_and_OS/C/Cpp const.md | 6 | 6 |
| Docs/Programming_and_OS/C/Cpp Ninja.md | 6 | 6 |
| Docs/Programming_and_OS/C/Cpp Class Constructors.md | 6 | 6 |
| Docs/Programming_and_OS/C/CMake CLI Environment.md | 6 | 6 |
| Docs/Programming_and_OS/Bash/Bash Redirections.md | 6 | 6 |
| Docs/ComputerScience/CS OOP Polymorphism.md | 4 | 6 |
| Docs/Programming_and_OS/SQL/SQLite database file.md | 5 | 5 |
| Docs/Programming_and_OS/Rust/Rust impl.md | 5 | 5 |
| Docs/Programming_and_OS/Python/Python typing.md | 5 | 5 |
| Docs/Programming_and_OS/C/pixi manifest.md | 5 | 5 |
| Docs/Programming_and_OS/C/CMake install.md | 5 | 5 |
| Docs/Software/openc3/openc3.md | 4 | 4 |
| Docs/Programming_and_OS/Rust/Rust Self.md | 4 | 4 |
| Docs/Programming_and_OS/Python/Python os environ.md | 4 | 4 |
| Docs/Programming_and_OS/Python/Python enum.md | 4 | 4 |
| Docs/Programming_and_OS/Python/Python dunder functions and methods.md | 4 | 4 |
| Docs/Programming_and_OS/Python/Python TypedDict.md | 4 | 4 |
| Docs/Programming_and_OS/Python/Python Decorators.md | 4 | 4 |
| Docs/Programming_and_OS/C/Cpp union.md | 4 | 4 |
| Docs/Programming_and_OS/C/Cpp references.md | 4 | 4 |
| Docs/Programming_and_OS/C/Cpp if else.md | 4 | 4 |
| Docs/Programming_and_OS/C/Cpp attributes.md | 4 | 4 |
| Docs/Programming_and_OS/C/Cpp Casting.md | 4 | 4 |
| Docs/Programming_and_OS/C/CMake visibility.md | 4 | 4 |
| Docs/Programming_and_OS/C/CMake target_sources.md | 4 | 4 |
| Docs/Programming_and_OS/C/CMake option.md | 4 | 4 |
| Docs/Programming_and_OS/C/CMake add_custom_target.md | 4 | 4 |
| Docs/Programming_and_OS/C/CMake Libraries.md | 4 | 4 |
| Docs/Programming_and_OS/C/C netinet.md | 4 | 4 |
| Docs/ComputerScience/Machine Learning/Machine Learning Terminology Sheet.md | 4 | 4 |
| Docs/ComputerScience/Factory Method.md | 4 | 4 |
| Docs/ComputerScience/ECE/CA.ArchitectureTypes.md | 4 | 4 |
| Docs/ComputerScience/CS Messaging and Serialization.md | 4 | 4 |
| Docs/Software/Caddy/Caddyfile.md | 3 | 3 |
| Docs/Programming_and_OS/Rust/Rust type conversions.md | 3 | 3 |
| Docs/Programming_and_OS/Rust/Rust trait.md | 3 | 3 |
| Docs/Programming_and_OS/Rust/Rust std sync Mutex.md | 3 | 3 |
| Docs/Programming_and_OS/Rust/Rust std String.md | 3 | 3 |
| Docs/Programming_and_OS/Python/Python dunder members.md | 3 | 3 |
| Docs/Programming_and_OS/Python/Python dataclass.md | 3 | 3 |
| Docs/Programming_and_OS/Python/Python Logic Operators.md | 3 | 3 |
| Docs/Programming_and_OS/Python/Python Functions.md | 3 | 3 |
| Docs/Programming_and_OS/Jupyter/Jupyter kernel.md | 3 | 3 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/linuxptp.md | 3 | 3 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux process limits.md | 3 | 3 |
| Docs/Programming_and_OS/C/libc.md | 3 | 3 |
| Docs/Programming_and_OS/C/Cpp switch.md | 3 | 3 |
| Docs/Programming_and_OS/C/Cpp std mutex.md | 3 | 3 |
| Docs/Programming_and_OS/C/Cpp std array.md | 3 | 3 |
| Docs/Programming_and_OS/C/Cpp gTest Mocking Workflow.md | 3 | 3 |
| Docs/Programming_and_OS/C/Cpp Assignment Operators.md | 3 | 3 |
| Docs/Programming_and_OS/C/CMake if.md | 3 | 3 |
| Docs/Programming_and_OS/C/C syntax.md | 3 | 3 |
| Docs/Programming_and_OS/Bash/Bash Conditionals.md | 3 | 3 |
| Docs/Networks_Signals_Protocols/Networking socket.md | 3 | 3 |
| Docs/ComputerScience/DP Actor Model (Conflicted copy iPhone 202509252029).md | 3 | 3 |
| Docs/Software/Postgres/Postgres Accessing a Database.md | 2 | 2 |
| Docs/Software/Git/Git Cheatsheet.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust usize.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust std thread.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust serde.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust match.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust closures.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust attributes.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust Variables and Type System.md | 2 | 2 |
| Docs/Programming_and_OS/Rust/Rust Functions.md | 2 | 2 |
| Docs/Programming_and_OS/Ruby/Ruby Syntax.md | 2 | 2 |
| Docs/Programming_and_OS/Python/Python pytest parameterizing.md | 2 | 2 |
| Docs/Programming_and_OS/Python/Python pytest markernames.md | 2 | 2 |
| Docs/Programming_and_OS/Python/Python Union.md | 2 | 2 |
| Docs/Programming_and_OS/Python/Python Modules.md | 2 | 2 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux time.md | 2 | 2 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux signals.md | 2 | 2 |
| Docs/Programming_and_OS/GNU and Linux and UNIX/Linux sed.md | 2 | 2 |
| Docs/Programming_and_OS/Docker/Docker Networks.md | 2 | 2 |
| Docs/Programming_and_OS/C/pixi.md | 2 | 2 |
| Docs/Programming_and_OS/C/Cpp std metaprogramming.md | 2 | 2 |
| Docs/Programming_and_OS/C/Cpp std memory make_unique.md | 2 | 2 |
| Docs/Programming_and_OS/C/Cpp std atomic.md | 2 | 2 |
| Docs/Programming_and_OS/C/Cpp macros.md | 2 | 2 |
| Docs/Programming_and_OS/C/Cpp include.md | 2 | 2 |
| Docs/Programming_and_OS/C/Cpp enumeration.md | 2 | 2 |
| Docs/Programming_and_OS/C/Cpp GoogleTest.md | 2 | 2 |
| Docs/Programming_and_OS/C/CMake target_include_directories.md | 2 | 2 |
| Docs/Programming_and_OS/C/CMake find_package.md | 2 | 2 |
| Docs/Programming_and_OS/C/CMake add_library.md | 2 | 2 |
| Docs/Programming_and_OS/Ansible/Ansible CLI tools.md | 2 | 2 |
| Docs/Networks_Signals_Protocols/Time and Time Servers.md | 2 | 2 |
| Docs/Networks_Signals_Protocols/Serial Protocols.md | 2 | 2 |
| Docs/Math and Physics/Set Theory.md | 2 | 2 |
| Docs/History of Timekeeping.md | 2 | 2 |
| Docs/ComputerScience/CS Virtual memory.md | 2 | 2 |
| Docs/ComputerScience/CS Memory.md | 2 | 2 |
| Docs/ComputerScience/Attack patterns.md | 2 | 2 |
| zz_Templates/template_classes/full_schema.md | 1 | 1 |
| zz_Templates/template_classes/base_note_template.md | 1 | 1 |
| Docs_Research_Industry/Topics/Space/Walker constellation.md | 1 | 1 |
| Docs/Software/openc3/openc3 telemetry configuration.md | 1 | 1 |
| Docs/Software/openc3/openc3 targets.md | 1 | 1 |
| Docs/Software/openc3/openc3 python API.md | 1 | 1 |
| Docs/Software/openc3/openc3 protocols.md | 1 | 1 |
| Docs/Software/openc3/openc3 file format.md | 1 | 1 |
| Docs/Software/openc3/openc3 configuration.md | 1 | 1 |
| Docs/Software/openc3/openc3 accessors.md | 1 | 1 |
| Docs/Software/openc3/openc3 Group.md | 1 | 1 |
| Docs/Software/Valgrind/Valgrind Callgrind.md | 1 | 1 |
| Docs/Software/Jenkins/Jenkins.md | 1 | 1 |
| Docs/Software/Git/Git clean.md | 1 | 1 |
| Docs/Software/Git/Git Merge Conflicts.md | 1 | 1 |
| Docs/Software/Caddy/Caddy.md | 1 | 1 |
| Docs/Programming_and_OS/SQL/SQL Terminology.md | 1 | 1 |

---

## Part 2 — Orphan Anki Notes (delete from Anki)

These 35 notes exist in Anki but cannot be matched to any vault entry.
Many may auto-resolve after cleaning vault duplicates (Part 1) and
re-running `scan.py --vault && scan.py --anki`. Check the list again
after that step before manually deleting.

| Anki ID | Note type | Field 1 | Deck |
|---------|-----------|---------|------|
| 1776720774002 | Code | `$$` | Default |
| 1776720800864 | Code | `ASSERT_*` | C |
| 1776720774765 | Code | `ASSERT_EQ(condition) << "Failure msg"` | C |
| 1776720801180 | Code | `EXPECT_GT(a, b)` | C |
| 1776720801056 | Code | `EXPECT_NE(a, b)` | C |
| 1776720801328 | Code | `EXPECT_STRCASEEQ(s1, s2)` | C |
| 1776720803604 | Code | `auto q = p;` | C |
| 1776720805086 | Code | `configs` | Docker |
| 1776720805604 | Code | `depends_on` | Docker |
| 1776720805101 | Code | `include` | Docker |
| 1776720775565 | Code | `name` | Docker |
| 1776720775454 | Code | `networks` | Docker |
| 1776720805071 | Code | `secrets` | Docker |
| 1776720804934 | Code | `services` | Docker |
| 1776720774330 | Code | `set +o` | Default |
| 1776720799206 | Code | `target_sources(<target> PUBLIC FILE_SET HEADERS ...` | C |
| 1776720797019 | Code | `using SpeedGetter = std::function<int()>;` | Default |
| 1776720805152 | Code | `version` | Docker |
| 1776720775429 | Code | `volumes` | Docker |
| 1776720805133 | Code | `x-<name>` | Docker |
| 1776720821631 | Term | `INADDR_ANY` | Networking |
| 1776720779333 | Term | `SOCK_SEQPACKET` | Networking |
| 1776720779368 | Term | `SOCK_STREAM` | Networking |
| 1776720821660 | Term | `htons()` | Networking |
| 1776720821602 | Term | `socklen_t` | Networking |
| 1776720826113 | Term | `Cpp interface` | C |
| 1776720819631 | Term | `DP Testing Dependency Injection` | Default |
| 1776720820003 | Term | `Depend on abstractions` | Default |
| 1776720778479 | Term | `Embedded computing` | Default |
| 1776720819460 | Term | `Open-closed principle` | Default |
| 1776720819981 | Term | `Prefer constructor injection` | Default |
| 1776720819446 | Term | `Single responsibility principle` | Default |
| 1776720778767 | Term | `Template injection` | Default |
| 1776720826305 | Term | `pointer` | C |
| 1776720826328 | Term | `reference` | C |

---

## Part 3 — Test Vault Contamination (informational)

The DB contains **1508 notes from 314 test vault files** stored with absolute
paths (`/home/will/projects/.../tests/complex-vault/...`). These will never
sync to your real Anki because they don't match your vault's folder deck patterns.
They inflate the `not_in_anki` count but cause no direct errors.

**Action (optional):** Run this to clear them:
```sql
DELETE FROM notes WHERE file_path LIKE '/home/will/projects%';
```

---

## Recommended Cleanup Order

1. Fix vault files in Part 1 (open each in Obsidian, remove duplicate note blocks)
2. `uv run python scan.py --vault` — rebuilds `notes` table
3. `uv run python scan.py --anki` — re-runs reconciliation; many Part 2 orphans may resolve
4. `uv run python diff.py` — regenerate diff
5. Review Part 2 list again; delete any remaining unresolved orphans from Anki
6. `uv run python write.py --execute`
