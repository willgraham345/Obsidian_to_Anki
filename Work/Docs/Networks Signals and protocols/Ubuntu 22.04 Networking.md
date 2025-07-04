---
type: note/component
component_of: ["[[Ubuntu Network Interface Names]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Monday, December 2nd 2024, 11:30:46 am
---
If you are connected to the internet, you (likely) have at least two IP addresses:
- System's local address
	- Used to communicate with other devices on your home network
- Public IP address
	- IP address that is routable on the world wide web. Typically, a home network has one public IP. 

# What am I looking At?
## Basic Ethernet Interfaces
| Interface   | Usage                                                                                              |
| ----------- | -------------------------------------------------------------------------------------------------- |
| IP address  | Unique identifier for a device on a network                                                        |
| Netmask     | Used to mask part of the IP address, allowing the device to distinguish between different networks |
| Gateway     | Address of the router that the device uses to connect to other networks                            |
| DNS Servers | Used to resolve hostnames to IP addresses                                                                                                   |

DNS = Domain name system, which translates domain names into IP addresses

## IPv4 Methods by Connection Type
[Wired, Wireless, and DSL Connection Methods](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/7/html/networking_guide/sec-configuring_ipv4_settings)

# How do I set it?
## How to Connect two computers
[Ethernet Data or file transfer](https://askubuntu.com/questions/59906/how-do-i-connect-my-desktop-and-my-laptop-using-an-ethernet-cable-to-transfer-fi)

## Commands
| Command                                 | Usage                                                                                             | Additional Info                                                                                                   |     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------- | --- |
| `ip a`                                  | Use it to see your local ip address                                                               | This will show interface names (`en0`, `eth0`) with assigned IP addresses, MAC addresses, and status (UP or DOWN) |     |
| `echo $(curl -s https://api.ipify.org)` | Good way to get your publbic ip address                                                           |                                                                                                                   |     |
| `systemd-resolve --status               | grep Current`                                                                                     | Check for currently used DNS system IP address                                                                    |     |
| `sudo lshw -class network`              | Lists all network interfaces, with more info on each interface                                    |                                                                                                                   |     |
| `ethtool`                               | Utillity that displays configured settings and supported features of ethernet adapters like speed |                                                                                                                   |     |

## Setting a Static IP Address, Subnet Mask, and Default Gateway with GUI

![[03-ubuntu-22-04-network-configuration-1024x575.webp]]

## Setting a Static IP from CLI
1. Go to `/etc/netplan/50-cloud-init.yaml`
```
network:
    ethernets:
        enp0s3:
            dhcp4: false
            addresses: [192.168.1.202/24]
            gateway4: 192.168.1.1
            nameservers:
              addresses: [8.8.8.8,8.8.4.4,192.168.1.1]
    version: 2
```

2. Apply netplan changes
```shell
sudo netplan apply
%% or alternatively.... %%
sudo netplan --debug apply
```
