---
summary: Technique that hides a value's concrete type behind a uniform interface, allowing heterogeneous callables or objects to be stored and invoked without the caller knowing the real type.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Examples]]"
  - "[[#Usage]]"
similar:
  - "[[DP Testing Dependency Injection]]"
concept_of:
  - "[[DP Principles]]"
date created: Friday, March 20th 2026, 5:40:00 pm
date modified: Monday, March 23rd 2026, 3:10:52 pm
implementations:
  - "[[Cpp std function]]"
tags: [todo]
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 DP Type Erasure ;;; Technique that hides a value's concrete type at the point of storage — any callable or object satisfying the required signature can be stored and invoked without the caller knowing its real type. Primary C++ tool: [[Cpp std function]].

# TODO
- [ ] Compare this note with [[Cpp std function]] to make them agree
- [ ] Make sure I have all the type erasure/dependency injection stuff handled between this note and [[DP Testing Dependency Injection]]

# Additional Background
[Type erasure — Part I \| Andrzej's C++ blog](https://akrzemi1.wordpress.com/2013/11/18/type-erasure-part-i/)

## Concepts of Note
󰙎 Type erasure ;;; the concrete type is discarded at the point of storage; only the required behaviour (signature or concept) is retained by the wrapper. 

󰙎 Small-buffer optimization (SBO) ;;; `std::function` stores small callables inline (typically between 16-32 bytes) to avoid heap allocation; callables with large captures heap-allocate
 ^c4e56e

󰙎 Indirect call ;;; invocation dispatches through a stored function pointer inside something like `std::function` — prevents inlining; measurable overhead in hot loops

### Comparison with Alternatives
󰙎 Virtual interface (inheritance) ;;; type erased behind a vtable; concrete type IS recoverable via `dynamic_cast`; requires the dependency to inherit from your interface
󰙎 Template (compile-time duck typing) ;;; concrete type known and instantiated at compile time; zero overhead; NOT erased — each instantiation is a distinct type

### Costs
󰙎 Lost type identity ;;; cannot compare two `std::function` instances for equality; cannot `dynamic_cast` back to the original type
󰙎 Possible heap allocation ;;; callables whose captures exceed the SBO threshold heap-allocate inside `std::function`; keep captures small or use `std::move`
󰙎 No multi-call interaction testing ;;; `std::function` has no built-in call counting or argument capture — use an interface + GMock when you need `EXPECT_CALL` / `WillOnce`

### Decision Guide
󰠗 Need to store callables of different concrete types in one variable? ;; `std::function` type erasure
󰠗 Need runtime swappability, can use inheritance, need GMock interaction testing? ;; Virtual interface
󰠗 Concrete type known at compile time, want zero overhead? ;; Template
󰠗 Dependency is a single method — interface would be overkill? ;; Prefer `std::function` over a full interface
󰠗 Type erasure vs template: key difference? ;; Templates fix the concrete type per instantiation; type erasure hides it at runtime — any matching callable accepted

## Usage
Injecting a single-method dependency without creating an interface:

 `using Callback = std::function<void(int)>;` ;;; define the expected signature as a named alias
 `class Foo { Callback mCb; public: Foo(Callback cb) : mCb{std::move(cb)} {} };` ;;; store via constructor; [[Cpp std move]] avoids a redundant copy
 `mCb(value);` ;;; invoke — works for any callable that was stored, with no virtual dispatch
 `Foo foo{[](int v) { /* ... */ }};` ;;; inject a lambda at the call site — no class or interface needed
 `Foo foo{std::bind(&MyClass::onEvent, &obj, std::placeholders::_1)};` ;;; or inject a bound member function

Test — no mock framework required:
 `bool called = false; int received = 0;` ;;; capture test state in locals
 `Foo foo{[&](int v) { called = true; received = v; }};` ;;; inject a capturing lambda as the dependency
 `EXPECT_TRUE(called);` ;;; assert via captured state; see [[DP Testing Dependency Injection]]

See: [[Cpp std function]], [[Cpp std move]], [[Cpp std invoke]]

## Examples
### Injecting a speed-check dependency (no interface)
Original `Car` owns a concrete `DcMotor`. To test without an interface, erase the motor's type:

 `using SpeedFn = std::function<int()>;` ;;; erases the motor type — any int-returning callable is accepted
 `using StopFn  = std::function<void()>;` ;;; erases the stop behaviour
 `Car(SpeedFn getSpeed, StopFn stop) : mGetSpeed{std::move(getSpeed)}, mStop{std::move(stop)} {}` ;;; constructor injection; move avoids copying the captured state
 `if (mGetSpeed() > 50) mStop();` ;;; call through stored functions — no vtable, no `override`

Production wiring:
 `DcMotor motor; Car car{[&]{ return motor.getSpeed(); }, [&]{ motor.stop(); }};` ;;; wrap the real motor in lambdas at the composition root

Test wiring — lambdas replace a mock object entirely:
 `bool stopped = false;` ;;; local flag captured by the lambda
 `Car car{[] { return 100; }, [&] { stopped = true; }};` ;;; inject plain lambdas; no mock class needed
 `car.controlSpeed(); EXPECT_TRUE(stopped);` ;;; verify outcome through captured state

### Storing a heterogeneous list of callbacks
Type erasure also lets you collect callbacks of different concrete types in one container:

 `std::vector<std::function<void()>> handlers;` ;;; one container holds lambdas, free functions, and functors alike
 `handlers.push_back([] { doA(); });` ;;; lambda — concrete type erased on push
 `handlers.push_back(std::bind(&Obj::doB, &obj));` ;;; bound member — different concrete type, same slot
 `for (auto& h : handlers) h();` ;;; invoke all uniformly — caller has no knowledge of the original types
