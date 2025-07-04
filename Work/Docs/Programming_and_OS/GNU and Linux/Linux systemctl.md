---
summary: A cli tool that allows you to manage/monitor [[Linux systemd]] system and service manager 
type: note/function
date created: Friday, September 13th 2024, 2:46:21 pm
date modified: Thursday, January 9th 2025, 5:31:51 pm
tags: [command/linux, command/linux/process/systemd, command/linux/process/systemd/inspection, command/linux/process/systemd/management]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Usage
- [p] `systemctl enable <service.name>` = Enables system service = #command/linux/process/systemd/management 
<!--ID: 1751434090782-->

- [p] `systemctl start <service.name>` = Starts system service = #command/linux/process/systemd/management 
<!--ID: 1751434090786-->

- [p] `systemctl stop <service.name>` = Stops a system service = #command/linux/process/systemd/management 
<!--ID: 1751434090790-->

- [p] `systemctl reload <service.name>` = Reload the configuration file (without restarting). = #command/linux/process/systemd/management   
<!--ID: 1751434090793-->

- [p] `systemctl restart <service.name>` = Restarts a system service = #command/linux/process/systemd/management  
<!--ID: 1751434090797-->

- [p] `systemctl status <service.name>` = Get the status of a system service with location, unit name, status, uptime and processes = #command/linux/process/systemd/inspection 
<!--ID: 1751434090801-->

- [p] `systemctl list-units` = See a list of all active units that `systemd` knows about = #command/linux/process/systemd/inspection  = Columns for this command include the UNIT (name in systemd), LOAD (whether the unit's config has been parsed by systemd), ACTIVE, SUB (lower-level state that indicates more detailed info about the unit. Varies by unit type, state, and method in which the unit runs), DESCRIPTION
<!--ID: 1751434090806-->

      `--all` Show all files
      `--state=<input>`
      `--type=<unit_type>`
- [p] `systemctl list-unit-files` = See every available unit file within the systemd paths, including those that systemd has not attempted to load. State will usually be `enabled, disabled, static, or masked`. = #command/linux/process/systemd/inspection 
<!--ID: 1751434090810-->

- [p] `systemctl cat <unit_name.unit_type>` = Display the unit file that systemd has loaded into its system = #command/linux/process/systemd/inspection  
<!--ID: 1751434090813-->

- [p] `systemctl list-dependencies <unit_name.unit_type>` = Display hierarchy mapping dependencies that must be dealt with in order to start the unit in question. Includes units that are either required or wanted by the units above it. = #command/linux/process/systemd/inspection 
<!--ID: 1751434090817-->

- [p] `systemctl show <unit_name.unit_type>` = Show low level properties of a unit = #command/linux/process/systemd/inspection 
<!--ID: 1751434090821-->

- [p] `systemctl mask <unit_name.unit_type>` = Marks a unit as completely unstartable, automatically or manually, by linking it to `/dev/null`. = #command/linux/process/systemd/management 
<!--ID: 1751434090825-->

- [p] `systemctl edit <unit_name.unit_type>` = Edit will open a unit file snippet as a blank file to override (if override, then you get `override.conf`) or add directives to unit definition. A directory will be created within the `/etc/systemd/system`.