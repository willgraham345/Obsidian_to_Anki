---
summary: Inline namespace of UDL suffixes for std::chrono duration and calendar types; activated with `using namespace std::chrono_literals` (C++14, <chrono>).
type: note/library/module
tags: [programming/cpp]
up:
  - "[[Cpp std]]"
similar:
  - "[[Cpp.Literals and Macros]]"
date created: Tuesday, March 24th 2026, 10:00:00 am
date modified: Tuesday, March 24th 2026, 10:00:00 am
---
# Summary
󰙎 Cpp std chrono_literals ;;; Inline namespace of UDL suffixes for `std::chrono` duration types; enabled with `using namespace std::chrono_literals` (C++14, `<chrono>`)

# Additional Background
## Concepts of Note
- [I] user-defined literal (UDL) ;;; C++11 feature — suffix operators on numeric values that construct typed objects; chrono_literals uses this to produce `std::chrono::duration` values directly from integer/float literals
- [I] inline namespace ;;; Declared as `std::literals::chrono_literals`; re-exported by `std::chrono` — both `using namespace std::chrono_literals` and `using namespace std::literals` work

### Duration Suffixes (C++14)
- [p] `1h` ;;; `std::chrono::hours{1}` — `long long` tick representation
- [p] `30min` ;;; `std::chrono::minutes{30}`
- [p] `2s` ;;; `std::chrono::seconds{2}`
- [p] `500ms` ;;; `std::chrono::milliseconds{500}`
- [p] `100us` ;;; `std::chrono::microseconds{100}`
- [p] `50ns` ;;; `std::chrono::nanoseconds{50}`

### Calendar Suffixes (C++20)
- [p] `15d` ;;; `std::chrono::day{15}` — day-of-month (1–31); **not** a duration
- [p] `2026y` ;;; `std::chrono::year{2026}` — calendar year; **not** a duration

## Usage
- [p] `using namespace std::chrono_literals;` ;;; enables all suffixes in scope — place in function body, never in a header at global/namespace scope
- [p] `std::this_thread::sleep_for(200ms);` ;;; sleep 200 ms — canonical motivating example; requires `<thread>`
- [p] `auto t = 1h + 30min + 45s;` ;;; mixed-unit arithmetic — result deduced as `std::chrono::seconds` (common duration)
- [p] `auto deadline = std::chrono::steady_clock::now() + 5s;` ;;; add duration to a `time_point`
- [p] `std::chrono::duration<double> d = 1.5s;` ;;; floating-point literal produces `duration<double, ratio<1>>`
