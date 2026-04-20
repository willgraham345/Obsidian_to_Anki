---
type: note/tool
tags:
  - programming/linux
  - programming/linux/tools
  - networking
date created: Monday, March 30th 2026, 12:00:00 pm
date modified: Monday, March 30th 2026, 12:00:00 pm
ai_generated: true
up: "[[Linux]]"
similar:
  - "[[scp]]"
  - "[[ssh]]"
---

# Summary
󰙎 rsync ;;; fast, incremental file-transfer utility using a delta-transfer algorithm; transmits only changed byte ranges rather than whole files; supports local, SSH-tunneled, and native daemon (rsyncd) transports

# Additional Background
rsync computes rolling checksums on both source and destination, then sends only non-matching byte blocks (deltas). This makes it efficient for large files with small changes — database dumps, VM images, incremental backups. It can tunnel over SSH or speak directly to the rsync daemon (`rsyncd`) on TCP 873.

## Concepts of Note

### Delta Algorithm
󰙎 delta-transfer ;;; rsync splits the destination file into fixed-size blocks and checksums each; the source finds matching blocks and transmits only the differing regions
󰙎 checksum skip ;;; by default rsync skips files whose mtime and size match; `--checksum` forces a full content comparison regardless
󰙎 in-place ;;; `--in-place` writes directly into the destination file rather than a temp file then rename; useful on space-constrained systems or for large files where a rename would be expensive

### rsync Daemon (rsyncd)
󰙎 rsyncd ;;; rsync's built-in server mode; listens on TCP 873; configured via `/etc/rsyncd.conf`; allows anonymous or authenticated pull/push without SSH
󰙎 module ;;; named export in `rsyncd.conf`; a `[module]` stanza maps a name to a local filesystem path with its own access controls
󰙎 rsync:// URI ;;; daemon-mode addressing; `rsync://host/module/path` or shorthand `host::module/path`; port 873 by default

## Usage

### Essential Flags
󰙎 -a / --archive ;;; archive mode; expands to `-rlptgoD`; preserves symlinks, permissions, timestamps, owner, group, and device files — the most common flag for backups
󰙎 -z / --compress ;;; compress data in transit; reduces bandwidth at cost of CPU; skip for transfers on fast LANs
󰙎 -n / --dry-run ;;; simulate without writing; combine with `-v` to preview exactly what would change
󰙎 --delete ;;; remove destination files absent from source; makes DST an exact mirror of SRC
󰙎 --exclude=PATTERN ;;; skip files matching shell glob; repeatable; processed in order with `--include`
󰙎 --link-dest=DIR ;;; hard-link unchanged files from a previous snapshot DIR into the new destination; enables space-efficient incremental backups
󰙎 --partial ;;; keep partially transferred files on interruption; pair with `--append-verify` to resume
󰙎 --bwlimit=KBPS ;;; cap transfer bandwidth; useful for background syncs that shouldn't saturate a link
󰙎 -e / --rsh=CMD ;;; override the remote shell; default `ssh`; e.g., `-e 'ssh -p 2222 -i ~/.ssh/id_backup'`
󰙎 --progress ;;; show per-file transfer speed and completion percentage
󰙎 --stats ;;; print a transfer summary (bytes sent/received, speedup ratio) at the end

### Common CLI Patterns
- [p] `rsync -av SRC/ DST/` ;;; sync contents of SRC into DST; trailing slash = "contents of", not the dir node itself
- [p] `rsync -avz -e ssh SRC/ user@host:DST/` ;;; sync to remote over SSH with compression
- [p] `rsync -av --delete SRC/ DST/` ;;; mirror — deletes extras in DST not found in SRC
- [p] `rsync -avn SRC/ DST/` ;;; dry-run preview before committing
- [p] `rsync -av --exclude='*.tmp' --exclude='.git/' SRC/ DST/` ;;; exclude patterns
- [p] `rsync -av --link-dest=../prev/ SRC/ snapshots/current/` ;;; snapshot-style incremental backup with hard links
- [p] `rsync rsync://host/module/ /local/path/` ;;; pull from rsync daemon module
- [p] `rsync -av --bwlimit=5000 SRC/ DST/` ;;; throttle transfer to ~5 MB/s

## Configuration

### rsyncd Global Options (`/etc/rsyncd.conf`)
󰙎 uid / gid ;;; drop-privilege user/group after binding; typically `nobody`
󰙎 use chroot ;;; chroot into module `path` before serving; recommended `yes` for security; requires root
󰙎 max connections ;;; max simultaneous client connections per module
󰙎 log file ;;; path for daemon log; default logs to syslog
󰙎 pid file ;;; path where rsyncd writes its PID; used by init systems

### rsyncd Module Options
󰙎 path ;;; filesystem root exported by this module
󰙎 read only ;;; `yes` = pull-only; `no` = allow pushes; default `yes`
󰙎 auth users ;;; comma-separated list of allowed usernames; checked against `secrets file`
󰙎 secrets file ;;; path to a `user:password` plaintext file; must be `chmod 600`
󰙎 hosts allow / hosts deny ;;; IP or CIDR access control; `hosts allow` takes precedence
󰙎 exclude ;;; module-level glob exclusions; clients cannot override these

### Managing the Daemon
- [p] `rsync --daemon` ;;; start rsyncd in foreground daemon mode (reads `/etc/rsyncd.conf`)
- [p] `systemctl enable --now rsync` ;;; enable and start rsyncd via systemd
- [p] `rsync --daemon --config=/path/to/rsyncd.conf` ;;; run with a non-default config file

## Flashcards
- [t] What does a trailing slash on the rsync source path mean? ;; "contents of the directory" — omitting it syncs the directory node itself as a subdir of DST
- [t] What port does the rsync daemon listen on? ;; TCP 873
- [t] What flag deletes destination files absent from source? ;; `--delete`
- [t] How do snapshot-style incremental backups work in rsync? ;; `--link-dest=DIR` hard-links unchanged files from a prior snapshot; only changed data is actually transferred, saving space and time
- [t] What does `-a` expand to? ;; `-rlptgoD` — recursive, preserve symlinks, permissions, timestamps, group, owner, device files
- [t] What format does rsyncd's secrets file use? ;; plaintext `user:password` per line; file must be `chmod 600`; path set by `secrets file` directive in `rsyncd.conf`
- [t] How do you connect to a named rsync daemon module? ;; `rsync rsync://host/module/path` or shorthand `host::module/path`
