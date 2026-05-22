---
type: note/tool
headings:
  - "[[#Syntax]]"
similar:
  - "[[Linux systemd template directives]]"
date created: Wednesday, April 8th 2026, 1:00:38 pm
date modified: Wednesday, April 8th 2026, 1:06:54 pm
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[Linux systemd system conf]]"
  - "[[Linux systemd unit]]"
---

# Summary
󰙎 Linux systemd directives ;;; Directives used within Systemd files.

# Additional Background
[systemd.directives(7) - Linux manual page](https://man7.org/linux/man-pages/man7/systemd.directives.7.html)

## Syntax


```
[Unit]
 Description={{ description }}
 Wants=network-online.target
 After=network-online.target

 [Service]
 Type=simple
 ExecStart={{ command }}
 Restart=on-failure  (or "always", "on-success", ...)
 # Run as:
 User={{ user }}
 Group={{ groupname }}
 # SupplementaryGroups=name1 name2 name3
 WorkingDirectory={{ directory }}

 [Install]
 WantedBy=multi-user.target
```

### `[Unit]` Directives
󰙎 Description= ;;; Human-readable name shown in journal and status output
󰙎 Documentation= ;;; URIs for man pages or URLs; space-separated
󰙎 After= ;;; Start this unit after the listed units are active (ordering only, not dependency)
󰙎 Before= ;;; Start this unit before the listed units
󰙎 Wants= ;;; Weak dependency; listed units are started but failure is tolerated
󰙎 Requires= ;;; Hard dependency; listed units must activate or this unit fails
󰙎 PartOf= ;;; Stop/restart this unit when the listed unit stops/restarts (one-way)
󰙎 BindsTo= ;;; Like Requires= but also stops this unit if the bound unit stops
󰙎 Conflicts= ;;; Cannot run simultaneously with listed units; starts this, stops them

### Conditions and Assertions
󰙎 ConditionPathExists= ;;; Skip start silently if path does not exist (prefix ! to negate)
󰙎 ConditionFileNotEmpty= ;;; Skip start silently if file is empty or missing
󰙎 ConditionHost= ;;; Skip start if hostname does not match
󰙎 ConditionKernelVersion= ;;; Skip start if kernel version does not match expression
󰙎 ConditionEnvironment= ;;; Skip start if environment variable is not set
󰙎 AssertPathExists= ;;; Like Condition* but failure marks unit failed instead of skipping

### `[Service]` Directives
󰙎 Type= ;;; Declares process start-up type; controls when unit is considered active (simple, exec, forking, oneshot, notify, dbus, idle)
󰙎 ExecStart= ;;; Command (and args) to run as the main process
󰙎 ExecStartPre= ;;; Commands to run before ExecStart=; failure (without -) aborts start
󰙎 ExecStartPost= ;;; Commands to run after ExecStart= succeeds
󰙎 ExecStop= ;;; Command to stop the service; default is SIGTERM to main process
󰙎 ExecReload= ;;; Command to reload config without stopping (e.g. kill -HUP $MAINPID)
󰙎 Restart= ;;; When to auto-restart: no | on-success | on-failure | on-abnormal | always
󰙎 RestartSec= ;;; Delay before restart attempt (default 100ms)
󰙎 RemainAfterExit= ;;; If yes, unit is active even after main process exits (use with oneshot)
󰙎 Environment= ;;; Set environment variables inline (KEY=val KEY2=val2)
󰙎 EnvironmentFile= ;;; Load environment from a file; prefix - to ignore if missing
󰙎 StandardOutput= ;;; Where to send stdout: journal (default), syslog, null, file:path, etc.
󰙎 TimeoutStartSec= ;;; Abort start if not ready within this time (default 90s)
󰙎 TimeoutStopSec= ;;; Kill if not stopped within this time after SIGTERM

### `[Install]` Directives
󰙎 WantedBy= ;;; Creates a wants symlink when enabled; most services use multi-user.target
󰙎 RequiredBy= ;;; Like WantedBy= but hard; enabling fails if target missing
󰙎 Also= ;;; Other units to enable/disable alongside this one
󰙎 Alias= ;;; Symlink names the unit can be referenced by
