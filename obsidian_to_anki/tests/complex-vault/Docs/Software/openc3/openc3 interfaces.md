---
summary: Interfaces implement physical connection to one or more targets. Typically ethernet connections implemented using TCP or UDP.
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Flashcards]]"
  - "[[#Properties]]"
  - "[[#Usage]]"
date created: Thursday, October 24th 2024, 2:59:57 pm
date modified: Friday, March 20th 2026, 9:59:15 am
item_of:
  - "[[openc3 configuration]]"
items:
  - "[[openc3 protocols]]"
tags: [tools/openc3/interfaces]
template:
template-version:
used_by:
  - "[[openc3 plugins]]"
uses:
  - "[[openc3 protocols]]"
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background

## Concepts of Note
󰙎  Interface ;;; The connection definition to the external embedded systems described in "Targets". Typically these are ethernet connections using TCP/UDP but can also be serial. = 
󰙎  Router ;;; These flow streams of telemetry packets out of COSMOS, and commands into COMSOS.
- Provide the code that COSMOS uses to receive real-time telemetry from targets and to send commands to targets.
	- Important that this is a customizable and reusable Command/Telemetry system.
	- Most common is TCP/IP sockets, and COSMOS has interface solutions for these.

### Provided Interfaces
- TCPIP Client, TCPIP Server, UDP, HTTP Client, HTTP Server, MQTT, MQTT Streaming, Serial, File, and custom

#### TCPIP Client
- Params: Host, Write Port, Read Port, Write Timeout, Read Timeout, Protocol Type
- Pass `None` to Write/Read Port to make read-only or write-only

#### TCPIP Server
- Params: Write Port, Read Port, Write Timeout, Read Timeout, Protocol Type
- Option: `LISTEN_ADDRESS` (default: 0.0.0.0)

#### UDP
- Params: Host, Write Dest Port, Read Port, Write Source Port, Interface Address, TTL (default 128), Write/Read Timeout

#### Serial
- Params: Write Port, Read Port, Baud Rate, Parity (NONE/EVEN/ODD), Stop Bits, Write/Read Timeout
- Options: `FLOW_CONTROL` (NONE/RTSCTS), `DATA_BITS` (default: 8)

#### MQTT / MQTT Streaming
- Params: Host, Port (default: 1883), SSL (default: false)
- Options: `USERNAME`, `PASSWORD`, `CERT`, `KEY`, `CA_FILE`, `ACK_TIMEOUT`
- Uses `META TOPIC` in cmd/tlm definitions to set per-packet topics

#### File
- Params: Command Write Folder, Telemetry Read Folder, Telemetry Archive Folder (use `DELETE` to auto-delete)
- Options: `EXTENSION` (default: .bin), `POLLING`, `RECURSIVE`, `THROTTLE`

### Interface Modifiers
󰙎  DONT_CONNECT ;;; Prevents auto-connection at startup
󰙎  DONT_RECONNECT ;;; Disables automatic reconnection after disconnect
󰙎  RECONNECT_DELAY ;;; Seconds between reconnection attempts (default: 5)
󰙎  DISABLE_DISCONNECT ;;; Removes user disconnect capability in the UI
󰙎  MAP_TARGET ;;; Routes both commands and telemetry for a named target through this interface
󰙎  MAP_CMD_TARGET ;;; Routes commands only for a named target
󰙎  MAP_TLM_TARGET ;;; Routes telemetry only for a named target
󰙎  LOG_STREAM ;;; Logs raw stream data without OpenC3 packet headers
󰙎  PROTOCOL ;;; Attaches a protocol (READ, WRITE, or READ_WRITE) for data processing

## Usage
[OpenC3 Docs](https://docs.openc3.com/docs/configuration/interfaces#tcpip-client-interface)

  `INTERFACE` ;;; Keyword to define an interface within COSMOS plugin.txt file. Typically ethernet connections implemented using TCP or UDP.

  `ROUTER` ;;; Keyword to define a router in COSMOS in plugin.txt file.

 `INTERFACE <name> tcpip_client_interface.rb <host> <write_port> <read_port> <write_timeout> <read_timeout>` ;;; TCPIP Client declaration syntax in plugin.txt

 `INTERFACE <name> tcpip_server_interface.rb <write_port> <read_port> <write_timeout> <read_timeout>` ;;; TCPIP Server declaration syntax in plugin.txt

 `INTERFACE <name> serial_interface.rb <write_port> <read_port> <baud> <parity> <stop_bits> <write_timeout> <read_timeout>` ;;; Serial interface declaration syntax in plugin.txt

 `INTERFACE <name> udp_interface.rb <host> <write_dest_port> <read_port>` ;;; UDP interface declaration syntax in plugin.txt

 `INTERFACE <name> mqtt_interface.rb <host> <port> <ssl>` ;;; MQTT interface declaration syntax in plugin.txt

## Properties





## Flashcards
󰠗  What interfaces does OpenC3 provide? ;; TCPIP client, TCPIP server, UDP, HTTP Client, HTTP Server, MQTT, MQTT Streaming, Serial, File, and custom.
󰠗  Where are interfaces defined? ;; In the `plugin.txt` file with `INTERFACE` plugin.
