---
type: note
up: ["[[Linux Networking and Internet]]"]
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Friday, December 13th 2024, 6:23:55 pm
tags: [command/linux/networking]
---
# Background
- [NetworkManager](https://networkmanager.dev/) is a program for providing detection and configuration for systems to automatically connect to networks. NetworkManager's functionality can be useful for both wireless and wired networks. For wireless networks, NetworkManager prefers known wireless networks and has the ability to switch to the most reliable network. NetworkManager-aware applications can switch from online and offline mode. NetworkManager also prefers wired connections over wireless ones, has support for modem connections and certain types of VPN. NetworkManager was originally developed by Red Hat and now is hosted by the [GNOME](https://wiki.archlinux.org/title/GNOME "GNOME") project.

- `nmtui`
	- Launches a nice dropdown simple verison
- NetworkManager comes with [nmcli(1)](https://man.archlinux.org/man/nmcli.1) and [nmtui(1)](https://man.archlinux.org/man/nmtui.1).

# Usage
- [p] `nmcli device wifi list` = List nearby Wi-Fi networks = #command/linux/networking
<!--ID: 1751434090833-->

- [p] `nmcli device wifi connect _SSID_or_BSSID_ password _password_` = Connect to a Wi-Fi network = #command/linux/networking
<!--ID: 1751434090837-->

- [p] `nmcli device wifi connect _SSID_or_BSSID_ password _password_ hidden yes` = Connect to a hidden Wi-Fi network = #command/linux/networking
<!--ID: 1751434090841-->

- [p] `nmcli device wifi connect _SSID_or_BSSID_ password _password_ ifname wlan1 _profile_name_` = Connect to a Wi-Fi on the `wlan1` interface = #command/linux/networking
<!--ID: 1751434090844-->

- [p] `nmcli device disconnect ifname eth0` = Disconnect an interface = #command/linux/networking
<!--ID: 1751434090847-->

- `$nmcli connection show` = Get a list of connections with their names, UUIDs, types and backing devices = #command/linux/networking
- [p] `nmcli connection up _name_or_uuid_` = Activate a connection (i.e. connect to a network with an existing profile) = #command/linux/networking
- [p] `nmcli connection delete _name_or_uuid_` = Delete a connection = #command/linux/networking
- [p] `nmcli device` = See a list of network devices and their state = #command/linux/networking
- [p] `nmcli radio wifi off` = Turn off Wi-Fi = #command/linux/networking

## Edit a connection

For a comprehensive list of settings, see [nm-settings(5)](https://man.archlinux.org/man/nm-settings.5).

Firstly, you need to get a list of connections:

`$ nmcli connection`
NAME                UUID                                  TYPE      DEVICE
Wired connection 2  e7054040-a421-3bef-965d-bb7d60b7cecf  ethernet  enp5s0
Wired connection 1  997f2782-f0fc-301d-bfba-15421a2735d8  ethernet  enp0s25
MY-HOME-WIFI-5G     92a0f7b3-2eba-49ab-a899-24d83978f308  wifi       --

Here you can use the first column as connection-id used later. In this example, we pick `Wired connection 2` as a connection-id.

You have three methods to configure a connection `Wired connection 2` after it has been created:

## nmcli interactive editor

`nmcli connection edit 'Wired connection 2'`.  
Usage is well documented from the editor.

nmcli command line interface

`nmcli connection modify 'Wired connection 2' _setting_._property_ _value_`. See [nmcli(1)](https://man.archlinux.org/man/nmcli.1) for usage. For example, you can change its IPv4 route metric to 200 using `nmcli connection modify 'Wired connection 2' ipv4.route-metric 200` command.

To remove a setting, pass an empty field ("") to it like this:

`nmcli connection modify 'Wired connection 2' _setting_._property_ ""`

Connection file

In `/etc/NetworkManager/system-connections/`, modify the corresponding `Wired connection 2.nmconnection` file .  
Do not forget to reload the configuration file with `nmcli connection reload`.