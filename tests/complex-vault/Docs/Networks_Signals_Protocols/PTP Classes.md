---
type: note/class
headings:
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
  - "[[#Questions]]"
aliases: []
class_of:
  - "[[PTP Server]]"
date created: Monday, February 23rd 2026, 4:09:25 pm
date modified: Wednesday, March 18th 2026, 12:00:00 pm
id: PTP Classes
tags: [cs/networking/protocols/time, ieee/1588]
template: "[[base_note_template]]"
template-version: 1.0.2
uses:
  - "[[timespec]]"
  - "[[POSIX.1b]]"
---

# Summary
󰙎 Structures within the PTP classes

# Additional Background
### 5.3.2 TimeInterval
The `TimeInterval` type represents time intervals.

```c
typedef Integer64 TimeInterval;
```

TimeInterval is the time interval expressed in nanoseconds, multiplied by 2^16. Positive or negative time intervals outside the maximum range of this data type shall be encoded as the largest positive and negative values of the data type, respectively. For example, 2.5 ns is expressed as `0000 0000 0002 800016`. NOTE—In the 2008 edition of this standard, TimeInterval was defined as a `struct`. There are no backward compatibility issues because the on‑the‑wire format is the same.

### 5.3.3 Timestamp
The `Timestamp` type represents a positive time with respect to the epoch.

```c
struct Timestamp {
    UInteger48 secondsField;
    UInteger32 nanosecondsField;
};
```

The `secondsField` member is the integer portion of the timestamp in units of seconds. The `nanosecondsField` member is the fractional portion of the timestamp in units of nanoseconds. The `nanosecondsField` member is always less than 10^9. For example: `+2.000000001` seconds is represented by `secondsField = 0000 0000 0002 16` and `nanosecondsField = 0000 0000 0016`.

### 5.3.4 ClockIdentity
The `ClockIdentity` type identifies unique entities within a PTP Network, for example, a PTP Instance or an entity of a common service.

```c
typedef Octet[8] ClockIdentity;
```

### 5.3.5 PortIdentity
The `PortIdentity` type identifies a PTP Port (see 7.5) or a Link Port (see 16.6.1).

```c
struct PortIdentity {
    ClockIdentity clockIdentity;
    UInteger16 portNumber;
};
```

### 5.3.6 PortAddress
The `PortAddress` type represents the protocol address of a PTP Port.

```c
struct PortAddress {
    Enumeration16 networkProtocol;
    UInteger16 addressLength;
    Octet[addressLength] addressField;
};
```

The value of the `networkProtocol` member shall be taken from the networkProtocol enumeration (see 7.4.1). The `addressLength` is the length in octets of the address. The range shall be 1 to 16 octets. The `addressField` member holds the protocol address of a PTP Port in the format defined by the mapping annex of the protocol as identified by the `networkProtocol` member. The most significant octet of the `addressField` is mapped into the octet of the `addressField` member with index 0.

### 5.3.7 ClockQuality
The `ClockQuality` represents the quality of a clock.

```c
struct ClockQuality {
    UInteger8 clockClass;
    Enumeration8 clockAccuracy;
    UInteger16 offsetScaledLogVariance;
};
```

### 5.3.8 TLV
The `TLV` type represents TLV extension fields.

```c
struct TLV {
    Enumeration16 tlvType;
    UInteger16 lengthField;
    Octet[lengthField] valueField;
};
```

The length of all TLVs shall be an even number of octets.

### 5.3.9 PTPText
The `PTPText` data type is used to represent textual material in PTP messages.

```c
struct PTPText {
    UInteger8 lengthField;
    Octet[lengthField] textField;
};
```

## Concepts of Note
󰙎 TAI vs UTC ;;; PTP uses TAI (International Atomic Time) — monotonically increasing, no leap seconds. UTC offset is carried in Announce messages. CLOCK_REALTIME is UTC; PHC tracks TAI.
󰙎 EUI-64 ;;; 64-bit identifier derived from a 48-bit MAC by inserting `FF:FE` at bytes 3–4. Used as `ClockIdentity` source.
󰙎 `tmv_t` ;;; linuxptp internal time value typedef (`int64_t`); stores nanoseconds as a single integer rather than split sec/nsec fields

## Usage
### Linux Type Mappings

How each IEEE 1588 §5.3 type maps to Linux/POSIX representations used by [[linuxptp]] and the kernel.

#### Timestamp ↔ struct timespec

PTP `Timestamp` is 80 bits on wire (6-byte seconds + 4-byte nanoseconds, big-endian). Linux [[timespec]] stores both fields as signed 64-bit integers (LP64).

```c
struct timespec {
    time_t  tv_sec;   /* seconds — signed 64-bit on LP64 */
    long    tv_nsec;  /* nanoseconds [0, 999999999] */
};
```

󰙎 `tv_sec` ;;; seconds since UNIX epoch (UTC); PTP `secondsField` uses TAI epoch — conversion requires adding current TAI-UTC offset (leap seconds)
󰙎 `tv_nsec` ;;; nanoseconds sub-second; always < 10^9, same constraint as PTP `nanosecondsField`

`linuxptp` stores time internally as `tmv_t` (nanoseconds, `int64_t`) to avoid repeated sec/nsec splitting during arithmetic. Conversion from wire `Timestamp` to `tmv_t`:

```c
/* pseudo-code: wire Timestamp → tmv_t */
tmv_t t = (int64_t)ts.secondsField * 1000000000LL + ts.nanosecondsField;
```

#### TimeInterval ↔ Fixed-Point Nanoseconds

`TimeInterval` is `Integer64` scaled ×2^16. No direct POSIX equivalent — linuxptp shifts right 16 bits to recover nanoseconds.

󰙎 `TimeInterval` scaling ;;; wire value ÷ 2^16 = nanoseconds (fractional); integer portion stored in `tmv_t`

#### ClockIdentity ↔ EUI-64 from MAC

`ClockIdentity` (8 bytes) is constructed from the NIC MAC via EUI-64 expansion: insert `FF:FE` at bytes 3–4.

```
MAC:  AA:BB:CC:DD:EE:FF  →  ClockIdentity: AA:BB:CC:FF:FE:DD:EE:FF
```

Linux provides the MAC via `SIOCGIFHWADDR` ioctl or `sysfs /sys/class/net/<iface>/address`. `ptp4l` reads this at startup.

#### clockid_t and PHC Clocks

Linux maps each PHC (`/dev/ptpN`) to a POSIX `clockid_t` synthesized from the file descriptor:

```c
#define CLOCKFD 3
#define FD_TO_CLOCKID(fd) ((~(clockid_t)(fd) << 3) | CLOCKFD)

int fd = open("/dev/ptp0", O_RDWR);
clockid_t clkid = FD_TO_CLOCKID(fd);
clock_gettime(clkid, &ts);   /* reads raw PHC counter */
```

󰙎 `CLOCK_REALTIME` ;;; kernel system clock (UTC-based); disciplined by `phc2sys` from the PHC — NOT read directly by `ptp4l`
󰙎 PHC `/dev/ptpN` ;;; PTP Hardware Clock — raw NIC counter; `ptp4l` disciplines this to the grandmaster; exposed as POSIX clock via `FD_TO_CLOCKID`

#### SO_TIMESTAMPING — Hardware Timestamps into Userspace

The kernel delivers NIC hardware RX/TX timestamps via `SO_TIMESTAMPING`. Timestamps arrive as `struct timespec[3]` in a `SCM_TIMESTAMPING` control message.

```c
int flags = SOF_TIMESTAMPING_RX_HARDWARE |
            SOF_TIMESTAMPING_RAW_HARDWARE |
            SOF_TIMESTAMPING_SOFTWARE;
setsockopt(sock, SOL_SOCKET, SO_TIMESTAMPING, &flags, sizeof(flags));

/* On recvmsg: cmsg type SOL_SOCKET/SCM_TIMESTAMPING carries: */
struct timespec ts[3];
/* ts[0] = software timestamp
   ts[1] = HW timestamp transformed to system time
   ts[2] = HW raw (PHC domain) — used by ptp4l as t2 or t4 */
```

TX hardware timestamps for Sync/Delay_Req egress arrive **after** `send()` returns, on the **socket error queue**. `ptp4l` calls `recvmsg(MSG_ERRQUEUE)` to retrieve `t1` or `t3`.

󰙎 `SOF_TIMESTAMPING_RX_HARDWARE` ;;; flag: capture RX timestamp in NIC at frame ingress; provides t2 (Sync arrival) and t4 (Delay_Req arrival)
󰙎 `SOF_TIMESTAMPING_TX_HARDWARE` ;;; flag: capture TX timestamp in NIC at frame egress; provides t1 (Sync departure) and t3 (Delay_Req departure); retrieved via error queue
󰙎 `SCM_TIMESTAMPING` ;;; socket control message type; carries `struct timespec[3]` from kernel to userspace

### Type Mapping Summary

| IEEE 1588 Type | Wire Width | Linux Representation |
|---|---|---|
| `Timestamp` | 80 bit (6+4) | `struct timespec` / `tmv_t` (ns) |
| `TimeInterval` | 64 bit (×2^16 scaled) | `int64_t`, shift >>16 for ns |
| `ClockIdentity` | 64 bit | EUI-64 derived from `SIOCGIFHWADDR` |
| `PortIdentity` | 80 bit | `struct ptp_clock_identity` (linuxptp) |
| `ClockQuality` | 32 bit | `struct ClockQuality` (linuxptp) |
| `TLV` | variable | `struct tlv_extra` (linuxptp) |

## Questions
󰠗 What is the two-stage discipline chain from grandmaster to CLOCK_REALTIME? ;; GM → ptp4l disciplines PHC (/dev/ptpN) via PTP messages → phc2sys disciplines CLOCK_REALTIME from PHC. Applications read CLOCK_REALTIME; ptp4l reads PHC directly.
󰠗 Why does PTP use TAI instead of UTC? ;; UTC has leap seconds causing discontinuities. TAI is monotonically increasing. PTP carries the TAI-UTC offset in Announce messages so slaves can derive UTC when needed.
󰠗 How does ptp4l get the t1 TX timestamp for a Sync message it sends? ;; Via the socket error queue. After send() returns, ptp4l calls recvmsg(MSG_ERRQUEUE) to retrieve the SOF_TIMESTAMPING_TX_HARDWARE timestamp captured by the NIC.
