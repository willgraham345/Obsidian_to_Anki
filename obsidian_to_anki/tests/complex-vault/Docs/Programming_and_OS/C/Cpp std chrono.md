---
type: note/library
headings:
  - "[[#Examples]]"
  - "[[#Syntax]]"
similar:
  - "[[Cpp std chrono_literals]]"
date created: Thursday, March 26th 2026, 10:00:00 am
date modified: Monday, April 6th 2026, 11:30:48 am
library_of:
  - "[[Cpp std]]"
tags: [programming/cpp]
template:
template-version:
---

# Summary
󰙎 Cpp std chrono (library) ;;; C++11 type-safe time library (`<chrono>`): clocks produce `time_point`s, arithmetic uses `duration`s, C interop via `system_clock::to_time_t`

# Additional Background
## Concepts of Note
### Duration
󰙎 `duration<Rep, Period>` ;;; A strongly typed tick count. Templated out for `Rep` (usually `int`) and `Period`; `Period = std::ratio<N,D>` = seconds-per-tick. 

### Time point 
󰙎 `time_point<Clock, Duration>` ;;; a single `Duration` offset from `Clock`'s epoch; `Duration` defaults to `Clock::duration`

### Clock types
󰙎 `system_clock` ;;; wall-clock; non-steady (`is_steady = false`); may jump (NTP); only clock with `to_time_t`/`from_time_t`
󰙎 `steady_clock` ;;; monotonic; never adjusts (`is_steady = true`); preferred for measuring elapsed time
󰙎 `high_resolution_clock` ;;; highest-resolution clock available; may alias `system_clock` or `steady_clock` — implementation-defined

### Current time
 `system_clock::now()` ;;; returns current wall `time_point<system_clock>`
 `tp.time_since_epoch()` ;;; returns `Duration` offset from clock epoch

󰙎 `system_clock::time_point` ;;; alias: `time_point<system_clock, system_clock::duration>`
 `system_clock::to_time_t(tp)` ;;; `time_point` → `std::time_t` (truncates sub-second precision)
 `system_clock::from_time_t(t)` ;;; `std::time_t` → `time_point<system_clock>`

### misc
 `tp + d` / `tp - d` ;;; shift time_point by a duration → `time_point`
 `tp2 - tp1` ;;; difference of two same-clock time_points → `Duration`
 `time_point_cast<D>(tp)` ;;; reinterpret resolution; truncates toward zero (no rounding)
 `time_point<Clock>{}` ;;; default-constructed = clock epoch (system_clock epoch = Unix epoch, Jan 1 1970)

## Usage
 `auto now = std::chrono::system_clock::now();` ;;; current wall time
 `auto t = std::chrono::system_clock::to_time_t(now);` ;;; → `time_t` for `std::ctime` / `std::strftime`
 `auto start = std::chrono::steady_clock::now();` ;;; capture start for elapsed measurement
 `auto elapsed = std::chrono::steady_clock::now() - start;` ;;; → `duration` (use `steady_clock`, not `system_clock`)
 `auto secs = std::chrono::duration_cast<std::chrono::seconds>(elapsed).count();` ;;; extract `long long` seconds count

### Go between time scales
 `auto ms = std::chrono::duration_cast<std::chrono::milliseconds>(time_fmt);` ;;; Convert `time_fmt` to a std chrono millisecond time
 `auto totalNanos = std::chrono::duration_cast<std::chrono::nanoseconds>(std::chrono::steady_clock::now().time_since_epoch()).count()` ;;; Get the total nanoseconds since unix epoch as a scalar

### Pretty printing 
 `std::format("{:%F %T}", now);` ;;; C++20 — format as `YYYY-MM-DD HH:MM:SS`; requires `<format>`

## Syntax
 `using millisecond_type = std::chrono::duration<int, std::ratio<1, 1000>>` ;;; Define a type `millisecond_type` which represents a 1/1000th of a second

## Examples
### Time something, print result
```cpp
auto startTime = std::chrono::steady_clock::now();

/* something which might take time */

auto endTime = std::chrono::steady_clock::now();
auto duration = std::chrono::duration<double>(endTime - startTime);
std::cout << "It took " << duration.count() << " seconds.\n";
```

### Pretty datetime
```cpp
// C++20
std::cout << "Now: " << std::chrono::system_clock::now() << '\n';

// Others
time_t now = std::chrono::system_clock::to_time_t(std::chrono::system_clock::now());
std::cout << "Now: " << ctime(&now) << '\n';
```