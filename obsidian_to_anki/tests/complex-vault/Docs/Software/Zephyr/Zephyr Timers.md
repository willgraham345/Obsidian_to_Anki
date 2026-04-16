---
type: note
---
# Background
- A timer is a kernel object that measures the passage of time using the kernel's system clock. When a timer is reach it can perform an application-defined action. 

# Timers
## Timer Properties
- A _duration_ specifying the time interval before the timer expires for the first time. This is a `k_timeout_t` value that may be initialized via different units.
- A _period_ specifying the time interval between all timer expirations after the first one, also a `k_timeout_t`. It must be non-negative. A period of `K_NO_WAIT` (i.e. zero) or `K_FOREVER` means that the timer is a one shot timer that stops after a single expiration. (For example then, if a timer is started with a duration of 200 and a period of 75, it will first expire after 200ms and then every 75ms after that.)
- An _expiry function_ that is executed each time the timer expires. The function is executed by the system clock interrupt handler. If no expiry function is required a `NULL` function can be specified.
- A _stop function_ that is executed if the timer is stopped prematurely while running. The function is executed by the thread that stops the timer. If no stop function is required a `NULL` function can be specified.
- A _status_ value that indicates how many times the timer has expired since the status value was last read.

## Timer Terms