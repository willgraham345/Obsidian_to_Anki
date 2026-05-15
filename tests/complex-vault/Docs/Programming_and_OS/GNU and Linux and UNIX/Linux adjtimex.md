---
type:
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Properties]]"
implements:
  - "[[NTP server]]"
aliases: [clock_adjtime, ntp_adjtime]
date created: Tuesday, March 3rd 2026, 3:55:11 pm
date modified: Tuesday, March 3rd 2026, 4:00:15 pm
libraries:
  - "[[Cpp std sys time]]"
  - "[[Cpp std sys timex]]"
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
used_by:
  - "[[NTP server]]"
uses:
  - "[[timex]]"
---

# Summary
󰙎 Linux adjtimex ;;; Tunes kernel clock using NTP

# Additional Background
## Concepts of Note
```cpp
struct timex {
	 int  modes;      /* Mode selector */
	 long offset;     /* Time offset; nanoseconds, if STA_NANO
											 status flag is set, otherwise
											 microseconds */
	 long freq;       /* Frequency offset; see NOTES for units */
	 long maxerror;   /* Maximum error (microseconds) */
	 long esterror;   /* Estimated error (microseconds) */
	 int  status;     /* Clock command/status */
	 long constant;   /* PLL (phase-locked loop) time constant */
	 long precision;  /* Clock precision
											 (microseconds, read-only) */
	 long tolerance;  /* Clock frequency tolerance (read-only);
											 see NOTES for units */
	 struct timeval time;
										/* Current time (read-only, except for
											 ADJ_SETOFFSET); upon return, time.tv_usec
											 contains nanoseconds, if STA_NANO status
											 flag is set, otherwise microseconds */
	 long tick;       /* Microseconds between clock ticks */
	 long ppsfreq;    /* PPS (pulse per second) frequency
											 (read-only); see NOTES for units */
	 long jitter;     /* PPS jitter (read-only); nanoseconds, if
											 STA_NANO status flag is set, otherwise
											 microseconds */
	 int  shift;      /* PPS interval duration
											 (seconds, read-only) */
	 long stabil;     /* PPS stability (read-only);
											 see NOTES for units */
	 long jitcnt;     /* PPS count of jitter limit exceeded
											 events (read-only) */
	 long calcnt;     /* PPS count of calibration intervals
											 (read-only) */
	 long errcnt;     /* PPS count of calibration errors
											 (read-only) */
	 long stbcnt;     /* PPS count of stability limit exceeded
											 events (read-only) */
	 int tai;         /* TAI offset, as set by previous ADJ_TAI
											 operation (seconds, read-only,
											 since Linux 2.6.26) */
	 /* Further padding bytes to allow for future expansion */
};
```

## Properties
## Examples
```cpp
#include <sys/timex.h>
#include <sys/time.h>
#include <iostream>
#include <stdexcept>

struct NtpSnapshot {
    long     offset_ns;      // current clock offset (nanoseconds)
    long     freq_ppm_scaled;// frequency correction (ppm * 2^16)
    long     max_error_us;   // maximum error estimate (microseconds)
    long     est_error_us;   // estimated error (microseconds)
    int      status;         // kernel clock status flags
    long     tick_us;        // tick duration (microseconds)
    timespec current_time;   // current time at moment of query
};

NtpSnapshot readNtpState() {
    struct timex tx{};
    tx.modes = 0; // read-only

    int ret = ntp_adjtime(&tx);
    // Return values:
    //   TIME_OK    (0) — synchronized, no leap second
    //   TIME_INS   (1) — insert leap second tonight
    //   TIME_DEL   (2) — delete leap second tonight
    //   TIME_OOP   (3) — leap second in progress
    //   TIME_WAIT  (4) — just completed leap second
    //   TIME_ERROR (5) — clock NOT synchronized
    if (ret < 0) {
        throw std::runtime_error("ntp_adjtime() failed");
    }

    NtpSnapshot snap{};
    snap.offset_ns       = tx.offset;      // nanoseconds if STA_NANO set
    snap.freq_ppm_scaled = tx.freq;
    snap.max_error_us    = tx.maxerror;
    snap.est_error_us    = tx.esterror;
    snap.status          = tx.status;
    snap.tick_us         = tx.tick;

    // Also grab high-res current time
    clock_gettime(CLOCK_REALTIME, &snap.current_time);

    return snap;
}
```

