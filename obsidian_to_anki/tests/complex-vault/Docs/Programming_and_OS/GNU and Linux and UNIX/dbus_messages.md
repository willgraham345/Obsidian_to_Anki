---
type: reference
tags:
  - programming/linux
  - programming/linux/systemd
  - programming/linux/ipc
date created: Wednesday, March 18th 2026, 12:00:00 pm
date modified: Wednesday, March 18th 2026, 12:00:00 pm
aliases:
  - DBus
  - D-Bus
up: "[[SystemD]]"
similar:
  - "[[POSIX Signals]]"
  - "[[Unix Domain Sockets]]"
tools:
  - "[[busctl]]"
  - "[[gdbus]]"
---

# Summary
󰙎 DBus ;;; inter-process communication (IPC) bus standard for Linux; provides a structured message-passing layer between userspace processes and the kernel/system services

# Additional Background
DBus (Desktop Bus) is a specification and reference implementation for IPC on Linux. Processes expose named objects with typed interfaces; other processes call methods, read/write properties, or listen to signals — all over a common bus managed by the `dbus-daemon`. [[SystemD]] registers its object tree on the system bus and is the primary way to query or control services programmatically.

## Concepts of Note

### Bus Types
󰙎 session bus ;;; per-user bus; scoped to a login session; used by desktop apps
󰙎 system bus ;;; single system-wide bus; `/run/dbus/system_bus_socket`; used by [[SystemD]], NetworkManager, udev, etc.
󰙎 peer-to-peer DBus ;;; direct socket connection without a daemon; used internally by systemd itself since v246

### Addressing Primitives
󰙎 service name ;;; well-known reverse-DNS identifier for a bus connection; e.g., `org.freedesktop.systemd1`
󰙎 unique name ;;; ephemeral bus address assigned at connect time; e.g., `:1.42`
󰙎 object path ;;; POSIX-path-like identifier for an object on a service; e.g., `/org/freedesktop/systemd1`
󰙎 interface ;;; named group of methods, signals, and properties on an object; e.g., `org.freedesktop.systemd1.Manager`
󰙎 member ;;; a single method, signal, or property within an interface

### Message Types
| Type | Direction | Description |
|------|-----------|-------------|
| Method call | caller → service | invoke a method; expects a reply |
| Method return | service → caller | success reply carrying return values |
| Error | service → caller | failure reply |
| Signal | service → all subscribers | broadcast notification; no reply |

### Properties
󰙎 DBus property ;;; named, typed value on an object; accessed via `org.freedesktop.DBus.Properties` `Get`/`Set`/`GetAll` methods
󰙎 PropertiesChanged signal ;;; emitted by `org.freedesktop.DBus.Properties` when a property value changes; used to watch unit state transitions

### Introspection
󰙎 Introspect ;;; standard method `org.freedesktop.DBus.Introspectable.Introspect` returning XML schema of all interfaces, methods, signals, and properties on an object path

### systemd DBus Integration
󰙎 org.freedesktop.systemd1 ;;; well-known service name systemd registers on the system bus
󰙎 /org/freedesktop/systemd1 ;;; root manager object; exposes `org.freedesktop.systemd1.Manager`
󰙎 /org/freedesktop/systemd1/unit/<encoded_name> ;;; per-unit object; exposes `Unit`, `Service`, `Socket`, `Timer` interfaces depending on unit type
󰙎 LoadUnit ;;; Manager method that returns the object path for a given unit name, loading it if needed

## Usage

### systemd1.Manager — key methods

##### StartUnit
󰡱 StartUnit:
- description: Start a unit by name
- args: `name` (string) — unit name e.g. `nginx.service`; `mode` (string) — `replace` | `fail` | `isolate` | `ignore-dependencies`
- calls: returns job object path
󰡱 end:

##### StopUnit
󰡱 StopUnit:
- description: Stop a named unit
- args: `name` (string); `mode` (string)
- calls: returns job object path
󰡱 end:

##### RestartUnit
󰡱 RestartUnit:
- description: Restart a unit (stop then start)
- args: `name` (string); `mode` (string)
󰡱 end:

##### GetUnit
󰡱 GetUnit:
- description: Return object path for an already-loaded unit; fails if not loaded (use `LoadUnit` to force load)
- args: `name` (string)
- calls: returns object path string
󰡱 end:

##### ListUnits
󰡱 ListUnits:
- description: Return array of all loaded units with name, description, load/active/sub state, job info
- args: none
󰡱 end:

### systemd1.Unit — key properties

##### ActiveState
󰫧 ActiveState:
- description: Current high-level unit state; one of `active` | `reloading` | `inactive` | `failed` | `activating` | `deactivating`
󰫧 end:

##### SubState
󰫧 SubState:
- description: Unit-type-specific sub-state; e.g., `running` for a Service unit in active state
󰫧 end:

##### LoadState
󰫧 LoadState:
- description: Whether the unit file has been loaded; `loaded` | `error` | `masked` | `not-found`
󰫧 end:

### Common Use Cases
- **Monitor service state** — subscribe to `PropertiesChanged` on a unit object to watch `ActiveState`
- **Start/stop services** — call `StartUnit`/`StopUnit` on `org.freedesktop.systemd1.Manager`
- **List failed units** — call `ListUnits`, filter where `ActiveState == "failed"`
- **Reload daemon** — call `Reload` method on Manager (equivalent to `systemctl daemon-reload`)
- **Transient units** — call `StartTransientUnit` to create ephemeral units at runtime without a unit file

## Examples

### busctl — introspect systemd root object
```bash
busctl introspect org.freedesktop.systemd1 /org/freedesktop/systemd1
```
 `busctl introspect <service> <path>` ;;; print all interfaces, methods, signals, properties on an object

### busctl — call a method
```bash
# Start nginx.service (mode: replace)
busctl call org.freedesktop.systemd1 \
  /org/freedesktop/systemd1 \
  org.freedesktop.systemd1.Manager \
  StartUnit "ss" nginx.service replace
```
 `busctl call <service> <path> <interface> <method> <sig> [args...]` ;;; invoke a DBus method; type signature uses GVariant type codes (`s`=string, `u`=uint32, `b`=bool, `a`=array)

### busctl — get a property
```bash
busctl get-property org.freedesktop.systemd1 \
  /org/freedesktop/systemd1/unit/nginx_2eservice \
  org.freedesktop.systemd1.Unit \
  ActiveState
```
 `busctl get-property <service> <path> <interface> <property>` ;;; read a single property value

### busctl — monitor signals
```bash
busctl monitor org.freedesktop.systemd1
```
 `busctl monitor <service>` ;;; capture all DBus messages to/from a service in real time; useful for observing `PropertiesChanged` and `JobRemoved` signals

### gdbus — introspect
```bash
gdbus introspect --system \
  --dest org.freedesktop.systemd1 \
  --object-path /org/freedesktop/systemd1
```
 `gdbus introspect --system --dest <service> --object-path <path>` ;;; GLib-based alternative to busctl introspect; output is identical XML

### gdbus — call method
```bash
gdbus call --system \
  --dest org.freedesktop.systemd1 \
  --object-path /org/freedesktop/systemd1 \
  --method org.freedesktop.systemd1.Manager.StopUnit \
  nginx.service replace
```

### Unit name encoding
Object paths cannot contain `.` or `@`; systemd encodes unit names:
- `.` → `_2e`
- `-` → `_2d`
- `@` → `_40`

 `systemd-escape --path <unit_name>` ;;; encode a unit name to its DBus object path segment

## Flashcards

󰠗 What socket does the system bus use by default? ;; `/run/dbus/system_bus_socket`
󰠗 What is the DBus service name for systemd? ;; `org.freedesktop.systemd1`
󰠗 How does a DBus signal differ from a method call? ;; signals are broadcast with no expected reply; method calls are directed and require a method return or error reply
󰠗 What method returns an already-loaded unit's object path? ;; `GetUnit` on `org.freedesktop.systemd1.Manager`; use `LoadUnit` if the unit may not be loaded yet
󰠗 What GVariant type code means "string"? ;; `s`
󰠗 What systemd DBus signal fires when a unit's ActiveState changes? ;; `PropertiesChanged` on `org.freedesktop.DBus.Properties` for the unit object
󰠗 How do you encode `nginx.service` as a DBus object path segment? ;; `nginx_2eservice` (`.` → `_2e`)
