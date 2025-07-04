---
type: note/function
date created: Friday, September 13th 2024, 2:49:34 pm
date modified: Thursday, February 6th 2025, 10:10:44 am
function_of: ["[[Linux systemd]]"]
---
# Background
- A service = any resource that the operating system can recognize and manage. 
	- Can be a software application

# Usage
| **Command**                           | **Description**                                                |
| ------------------------------------- | -------------------------------------------------------------- |
| `systemctl status`                    | Display the status of a system or service                      |
| `systemctl start <service>`           | Start a service                                                |
| `systemctl stop <service>`            | Stop a service                                                 |
| `systemctl restart <service>`         | Restart a service                                              |
| `systemctl reload <service>`          | Reload configuration for a service without stopping it         |
| `systemctl enable <service>`          | Enable a service to start on boot                              |
| `systemctl disable <service>`         | Disable a service from starting on boot                        |
| `systemctl is-active <service>`       | Check if a service is currently active                         |
| `systemctl is-enabled <service>`      | Check if a service is enabled to start on boot                 |
| `systemctl list-units`                | List all units (services, sockets, etc.)                       |
| `systemctl list-units --type=service` | List all active services                                       |
| `systemctl show <service>`            | Show properties of a service                                   |
| `systemctl mask <service>`            | Prevent a service from being started manually or automatically |
| `systemctl unmask <service>`          | Remove a mask on a service to allow it to be started           |
| `systemctl daemon-reload`             | Reload systemd manager configuration                           |
| `systemctl restart <service> --now`   | Restart a service and immediately reflect changes              |
| `systemctl reset-failed`              | Reset the failed state of all services                         |
