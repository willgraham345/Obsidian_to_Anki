---
summary: A cli tool that allows you to manage/monitor [[Linux systemd]] system and service manager
type: note/tool
headings:
date created: Friday, September 13th 2024, 2:46:21 pm
date modified: Thursday, January 22nd 2026, 4:04:28 pm
tags: [cs/linux, cs/linux/process/systemd, cs/linux/process/systemd/inspection, cs/linux/process/systemd/management]
template:
template-version:
tool_of: ["[[Linux systemd]]"]
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
  `systemctl enable <service.name>` ;;; Enables system service
  `systemctl start <service.name>` ;;; Starts system service
  `systemctl stop <service.name>` ;;; Stops a system service
  `systemctl reload <service.name>` ;;; Reload the configuration file (without restarting).
  `systemctl restart <service.name>` ;;; Restarts a system service
  `systemctl status <service.name>` ;;; Get the status of a system service with location, unit name, status, uptime and processes
  `systemctl list-units` ;;; See a list of all active units that `systemd` knows about
  `systemctl list-unit-files` ;;; See every available unit file within the systemd paths, including those that systemd has not attempted to load. State will usually be `enabled, disabled, static, or masked`.
  `systemctl cat <unit_name.unit_type>` ;;; Display the unit file that systemd has loaded into its system
  `systemctl list-dependencies <unit_name.unit_type>` ;;; Display hierarchy mapping dependencies that must be dealt with in order to start the unit in question. Includes units that are either required or wanted by the units above it.
  `systemctl mask <unit_name.unit_type>` ;;; Marks a unit as completely unstartable, automatically or manually, by linking it to `/dev/null`.
  `systemctl show <unit_name.unit_type>` ;;; Show low level properties of a unit
  `systemctl edit <unit_name.unit_type>` ;;; Edit will open a unit file snippet as a blank file to override (if override, then you get `override.conf`) or add directives to unit definition. A directory will be created within the `/etc/systemd/system`.
