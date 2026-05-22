---
type: note
---
# Background on Timing Concepts
## Terminology
Time Axis: representation of time as ordered sequence of instants
Time scale: way of representing an instant relative to an origin that serves as the epoch
Monotonic = increasing


## Time Scales
- [International Atomic Time](https://en.wikipedia.org/wiki/International_Atomic_Time) (TAI) is a time scale based on averaging clocks that count in SI seconds. TAI is a montonic and continuous time scale.
- [Universal Time](https://en.wikipedia.org/wiki/Universal_Time) (UT) is a time scale based on Earth’s rotation. UT is a discontinuous time scale as it requires occasional adjustments ([leap seconds](https://en.wikipedia.org/wiki/Leap_second)) to maintain alignment to changes in Earth’s rotation. Thus the difference between TAI and UT varies over time. There are several variants of UT, with [UTC](https://en.wikipedia.org/wiki/Coordinated_Universal_Time) being the most common.
- UT times are independent of location. UT is the basis for Standard Time (or “local time”) which is the time at a particular location. Standard time has a fixed offset from UT at any given instant, primarily influenced by longitude, but the offset may be adjusted (“daylight saving time”) to align standard time to the local solar time. In a sense local time is “more discontinuous” than UT.
- [POSIX Time](https://tools.ietf.org/html/rfc8536#section-2) is a time scale that counts seconds since the “POSIX epoch” at 1970-01-01T00:00:00Z (i.e. the start of 1970 UTC). 
	- [UNIX Time](https://tools.ietf.org/html/rfc8536#section-2) is an extension of POSIX time using negative values to represent times before the POSIX epoch. Both of these scales assume that every day has exactly 86400 seconds. In normal use instants in these scales correspond to times in the UTC scale, so they inherit the discontinuity.
	- The continuous analogue is [UNIX Leap Time](https://tools.ietf.org/html/rfc8536#section-2) which is UNIX time plus all leap-second corrections added after the POSIX epoch (when TAI-UTC was 8 s).
# Time in Zephyr
- Zephyr ttick counter has no concept of leap seconds. 