---
summary: Has more systemd and unit files.
type: note/workflow
date created: Tuesday, December 3rd 2024, 10:53:00 am
date modified: Tuesday, December 3rd 2024, 11:59:58 am
workflow_of: ["[[Linux systemd units]]"]
---
# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

[Understanding Systemd Units and Unit Files | DigitalOcean](https://www.digitalocean.com/community/tutorials/understanding-systemd-units-and-unit-files)

# Usage
## Naming Convention
```
name.type
```
- `ssh.socket`

## Sections of Unit files

### Unit Section
How the thing is actually added into a dependency tree. Connects to another unit, and goes from there.
- First section found in the most unit files is the `[Unit]` section
- Case sensitive
- If you need to add a non-standard sections to be parsed by applications other than systemd, add a `X-` prefix to the section name.

#### Directives and examples
- **`Description=`**:  
    A brief description of the unit's name and basic functionality. This is displayed by various `systemd` tools. It should be short, specific, and informative.
- **`Documentation=`**:  
    Specifies URIs for documentation related to the unit. These can be local man pages or web URLs. Displayed by `systemctl status` for easy access.
- **`Requires=`**:  
    Lists units that this unit depends on. If this unit is activated, the listed units must also successfully activate; otherwise, this unit fails. Dependencies are activated in parallel by default.
- **`Wants=`**:  
    Similar to `Requires=`, but less strict. Systemd attempts to start the listed units when this unit is activated, but failure of those units does not stop this unit. Best for most dependency configurations, with parallel activation unless otherwise specified.
- **`BindsTo=`**:  
    Like `Requires=`, but also ensures that this unit stops if the associated unit terminates.
- **`Before=`**:  
    Ensures that units listed here will not start until this unit has started if they are activated at the same time. Does not imply a dependency; use with `Requires=` or `Wants=` for that purpose.
- **`After=`**:  
    Specifies that the listed units must start before this unit starts. Like `Before=`, this does not create a dependency relationship by itself.
- **`Conflicts=`**:  
    Defines units that cannot run simultaneously with this unit. Starting one will stop the others.
- **`Condition...=`**:  
    A group of directives that test conditions before starting the unit. Useful for creating generic unit files that only run on appropriate systems. If the condition fails, the unit is gracefully skipped.
- **`Assert...=`**:  
    Similar to `Condition...=`, but stricter. If a condition fails, the unit activation fails instead of being skipped. Used to enforce critical checks on the environment.

### Service Unit Section
Specific to section, tells what binary you should run, and who you want to run it as.
Restart policy, typically conficuted restart the thing

#### Service Unit Types
- Simple: default, for executables which run without daemonising 
- Forking: For executables which daemonise themselves (this executable dies as soon as its started...? Not sure on this)
- Oneshot: Usually short-lived programs which run to completion and terminate
	- Great for bootstrapping services.
- Notify: For executables which will notify systemd when they are started and available for work.

### Install Section

```
[Section]
Directive1=value
Directive2=value

. . .
```

Other end of the `[Install]` directive section.