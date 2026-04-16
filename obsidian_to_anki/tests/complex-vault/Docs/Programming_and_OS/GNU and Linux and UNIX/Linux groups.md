---
type: note/concept
headings:
similar:
  - "[[dbus_messages]]"
concept_of:
  - "[[Linux Kernel]]"
date created: Tuesday, March 24th 2026, 12:00:00 pm
date modified: Sunday, March 29th 2026, 6:48:59 pm
tags: [linux/permissions, programming/linux]
template:
template-version:
---

# Summary
󰙎 Linux Groups ;;; A mechanism for managing collective access permissions — each user belongs to a primary group and zero or more supplementary groups, which gate access to devices, services, and privileged operations.

# Additional Background

Group membership is stored in `/etc/group`. The kernel checks group membership on every file/device access. Changes to group membership require logout/login (or `newgrp`) to take effect in running sessions.

## Concepts of Note

### Primary vs Supplementary Groups
󰙎 primary group ;;; The group associated with a user at login; sets the GID on new files created by that user. Defined in `/etc/passwd`.
󰙎 supplementary groups ;;; Additional groups a user belongs to; grant access to resources without changing file ownership. Listed in `/etc/group`.
󰙎 GID ;;; Group ID — numeric identifier for a group. System groups typically use GIDs < 1000.

### /etc/group Format
󰙎 `/etc/group` ;;; Flat file database of groups: `group_name:password:GID:user_list`
 `getent group <name>` ;;; Look up a group entry (works with LDAP/NIS too, unlike a direct file read)

### Notable Groups
󰙎 `docker` ;;; Access to the Docker daemon socket (`/var/run/docker.sock`); effectively grants root-equivalent container privileges
󰙎 `sudo` ;;; Debian/Ubuntu: members may run commands as root via `sudo`
󰙎 `wheel` ;;; RHEL/Arch: equivalent to `sudo` group; controls `sudo` and `su` access
󰙎 `dialout` ;;; Access to serial ports (`/dev/ttyS*`, `/dev/ttyUSB*`); required for Arduino, modems, USB-serial adapters
󰙎 `plugdev` ;;; Access to pluggable devices (USB drives, cameras) without root; common on Debian/Ubuntu
󰙎 `audio` ;;; Direct access to audio devices (`/dev/snd/*`); needed when not using PulseAudio/PipeWire user sessions
󰙎 `video` ;;; Access to video capture devices (`/dev/video*`) and sometimes GPU DRM nodes
󰙎 `input` ;;; Access to raw input devices (`/dev/input/*`); needed for reading raw keyboard/mouse events
󰙎 `render` ;;; Access to GPU render nodes (`/dev/dri/renderD*`); required for GPU compute without display ownership
󰙎 `kvm` ;;; Access to `/dev/kvm`; required to run VMs with hardware acceleration (QEMU/KVM)
󰙎 `lp` ;;; Access to printer devices (`/dev/lp*`)
󰙎 `fuse` ;;; Access to FUSE filesystems; allows mounting user-space filesystems
󰙎 `systemd-journal` ;;; Read access to the full systemd journal; non-root users otherwise see only their own session logs (see [[dbus_messages]])
󰙎 `adm` ;;; Read access to system log files in `/var/log/`; often granted to admins alongside `sudo`
󰙎 `netdev` ;;; Manage network interfaces via NetworkManager without sudo; common on desktop systems

## Usage

### Inspecting Groups
 `id` ;;; Show current user's UID, GID, and all supplementary group memberships
 `groups <user>` ;;; List all groups a user belongs to
 `getent group` ;;; Dump all groups from the system group database
 `ls -l /dev/ttyUSB0` ;;; Inspect a device file's group ownership to identify which group grants access

### Managing Membership
 `sudo usermod -aG <group> <user>` ;;; Add user to a supplementary group (`-a` = append; omitting it replaces all groups)
 `sudo gpasswd -d <user> <group>` ;;; Remove a user from a group
 `newgrp <group>` ;;; Start a new shell with a different active group (temporary; no logout needed)
 `sudo groupadd <name>` ;;; Create a new group
 `sudo groupdel <name>` ;;; Delete a group

## Flashcards
󰠗 What command adds a user to a group without removing existing memberships? ;; `sudo usermod -aG <group> <user>` — the `-a` flag appends rather than replaces
󰠗 Why does a group membership change require logout to take effect? ;; Supplementary groups are resolved at login and stored in the process credential set; running processes inherit the old set
󰠗 Which group grants Docker access and why is it a security risk? ;; `docker` — the daemon runs as root, so socket access allows arbitrary privilege escalation via containers
