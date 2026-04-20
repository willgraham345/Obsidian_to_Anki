---
type: note/item
headings:
  - "[[#Concepts of Note]]"
  - "[[#Properties]]"
ai_generated: true
date created: Tuesday, March 31st 2026, 10:34:12 am
date modified: Tuesday, March 31st 2026, 11:08:25 am
item_of:
  - "[[Networking Systems and Conventions]]"
processes:
  - "[[Networking CRC#CRC process]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[Networking Messaging]]"
  - "[[Space Networking Protocols]]"
---

# Summary
󰙎  CRC ;;; Cyclic redundancy check error, a check on digital data where a short check value is attached. On retrieval, a calculation repeated on this communication, and if these values don't match, corrective action can be taken against data corruption.

# Additional Background
[Cyclic redundancy check - Wikipedia](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)

## Concepts of Note
- A way to answer the question: "Did what I receive match what was sent?"
󰙎 GF(2) ;;; Galois Field of 2 — binary arithmetic where XOR = addition, AND = multiplication; no carries; the mathematical basis of CRC polynomial division
󰙎 Generator polynomial ;;; The fixed divisor used in CRC division; choice determines which error patterns are reliably detectable (e.g., CRC-32 uses `0x04C11DB7`)
󰙎 FCS ;;; Frame Check Sequence — the CRC value appended to a transmitted frame (see [[Ethernet Frame Overview]])
󰙎 Burst error ;;; A contiguous run of corrupted bits; CRC reliably detects all burst errors of length ≤ degree of generator polynomial
- **Detection only** — CRC signals corruption but cannot locate or correct it; a failed check triggers retransmission (cf. [[Networking Messaging]])
- **Not cryptographic** — CRC is easily forged; use only for accidental corruption detection, not security integrity (cf. [[Networking TLS]])

### CRC variants
󰙎 CRC-8 ;;; 8-bit remainder; ATM headers, SMBus, Dallas/Maxim 1-Wire
󰙎 CRC-16 / CRC-CCITT ;;; 16-bit; USB, Bluetooth, X.25, HDLC, Modbus (see [[Serial Protocols]])
󰙎 CRC-32 (IEEE 802.3) ;;; 32-bit; Ethernet FCS, ZIP, PNG, SATA — polynomial `0x04C11DB7` (see [[Ethernet Frame Overview]], [[ECE Memory Storage Protocols]])
󰙎 CRC-32C (Castagnoli) ;;; 32-bit; iSCSI, SCTP, Btrfs — hardware-optimised; better error coverage than CRC-32

### vs. other error detection
󰙎 Parity bit ;;; Detects single-bit errors only; 1-bit overhead; weakest option
󰙎 Internet checksum ;;; 16-bit ones-complement addition; used in IPv4/TCP/UDP headers; weaker than CRC (misses some burst patterns)
󰙎 Hamming code ;;; Can detect and correct single-bit errors; higher overhead; used in ECC RAM, not network links

## Properties
### processes
##### CRC process
 start:
1. Sender divides data by generator (XOR-based) long division
2. Remainder of the division is the CRC val
3. CRC appended to packet before sending
4. Receiver performs the same division on the received data and CRC
5. If remainder is zero -> no detected error. If nonzero -> error

