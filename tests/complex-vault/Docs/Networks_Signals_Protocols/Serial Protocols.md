---
summary: Protocols used frequently in serial communication, defining how your data is encoded into bytes.
headings:
type: note/item
date created: Friday, October 3rd 2025, 11:27:55 am
date modified: Thursday, November 20th 2025, 12:15:58 pm
item_of: ["[[Networking Protocols]]"]
items: ["[[ARINC 818]]", "[[CAN]]", "[[HDMI]]", "[[I2C]]", "[[JSON]]", "[[PCI]]", "[[Protobuf]]", "[[RS-232]]", "[[RS-422]]", "[[RS-423]]", "[[Serial Protocol Wiring]]", "[[SPI]]", "[[USB]]"]
tags: [cs/networking/protocols/serial]
template:
template-version:
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
󰙎  UART ;;; Universal asynchronous receiver-transmitter, peripheral device for asynchronous communication in which data format and transmissions speeds are configurable. Sends bits one by one, from LSB to MSB. Implemented in [[RS-232]], [[RS-485]] and raw TTL. = #cs/networking/protocols/serial
󰙎  TTL ;;; Single-ended serial communication (low is 0, high is 1). = #cs/networking/protocols/serial 

| Feature                          | Protobuf                   | Cap'n Proto                                          | SBE                    | FlatBuffers    |
| -------------------------------- | -------------------------- | ---------------------------------------------------- | ---------------------- | -------------- |
| Schema evolution                 | yes                        | yes                                                  | caveats                | yes            |
| Zero-copy                        | no                         | yes                                                  | yes                    | yes            |
| Random-access reads              | no                         | yes                                                  | no                     | yes            |
| Safe against malicious input     | yes                        | yes                                                  | yes                    | opt-in upfront |
| Reflection / generic algorithms  | yes                        | yes                                                  | yes                    | yes            |
| Initialization order             | any                        | any                                                  | preorder               | bottom-up      |
| Unknown field retention          | removed  <br>in proto3     | yes                                                  | no                     | no             |
| Object-capability RPC system     | no                         | yes                                                  | no                     | no             |
| Schema language                  | custom                     | custom                                               | XML                    | custom         |
| Usable as mutable state          | yes                        | no                                                   | no                     | no             |
| Padding takes space on wire?     | no                         | optional                                             | yes                    | yes            |
| Unset fields take space on wire? | no                         | yes                                                  | yes                    | no             |
| Pointers take space on wire?     | no                         | yes                                                  | no                     | yes            |
| C++                              | yes                        | yes (C++11)*                                         | yes                    | yes            |
| Java                             | yes                        | yes*                                                 | yes                    | yes            |
| C#                               | yes                        | yes*                                                 | yes                    | yes*           |
| Go                               | yes                        | yes                                                  | no                     | yes*           |
| Other languages                  | lots!                      | 6+ others*                                           | no                     | no             |
| Authors' preferred use case      | distributed  <br>computing | [platforms /  <br>sandboxing](https://sandstorm.io/) | financial  <br>trading | games          |
