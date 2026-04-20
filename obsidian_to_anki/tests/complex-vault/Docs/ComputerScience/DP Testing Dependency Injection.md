---
summary: An object or function receives other objects/functions it requires rather than creating them internally. Tight coupling between code is bad and inflexible. We want to avoid hard-coded dependencies.
type: note/concept
headings:
  - "[[#Concepts of Note]]"
  - "[[#Concepts of Note]]"
  - "[[#Usage]]"
similar:
  - "[[DP Testing Mocking]]"
concept_of:
  - "[[DP Principles]]"
date created: Wednesday, November 6th 2024, 9:29:18 am
date modified: Friday, March 20th 2026, 5:40:42 pm
implementations:
tags: []
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 DP Testing Dependency Injection ;;; Design pattern where an object or function receives other objects/functions it requires (usually in the constructor or template pattern) rather than creating them internally. This leads to flexible code without tightly coupled dependencies.

# Additional Background
## Concepts of Note
󰙎 Null Valued Objects ;;; An object which doesn't implement any functionality, just satisfieds types. This is as simple as having all the virtual methods return `true`.
 Law of demeter ;;; Don't talk to strangers--only call methods on objects you directly own, or were directly given. I.e., you shouldn't call more than one method deep when you own a class. 

### Methods to Inject
󰙎 Interface injection ;;; Inject dependencies by making members of a class an interface, and then using references/pointers to the interface for easy injection.
󰙎 Constructor injection ;;; Dependencies are provided through a client's class constructor, meaning you cannot create a new instance of the class without passing in a variable of the type required by the constructor. Make sure to avoid the possibility of passing in a null parameter.
󰙎 Template injection ;;; inject via template parameter — dependency is duck-typed at compile-time; no interface or vtable needed; preferred when only one runtime implementation exists
󰙎 Type erasure injection ;;; inject using [[Cpp std function]] — wraps any callable (free function, lambda, functor); suits single-method dependencies where an interface would be overkill

### Types of Injection
󰙎 Property (setter) injection ;;; dependency set post-construction via a setter — use only for optional or runtime-swappable dependencies; weaker than constructor injection because object can exist in an invalid/unusable state. Don't use this.

Method dependency injection ;;; Also bad

### When You Can't Create an Interface
When a dependency is a third-party class you cannot modify or inherit from:

󰙎 Template injection ;;; duck-typed at compile-time — mock only needs matching method signatures; no inheritance required
󰙎 Type erasure ;;; store as `std::function<Sig>` — inject any callable that matches the signature; no class or vtable needed
󰙎 Adapter pattern ;;; write a thin wrapper that implements your interface and delegates to the third-party type; keeps production code clean

### Decision Guide
󰠗 What type of dependency injection should be used with multiple implementations needed at runtime? ;; Interface + virtual functions
󰠗 What type of dependency injection should be used with a single implementation, zero vtable overhead wanted? ;; Template injection
󰠗 What type of dependency injection should be used with a single-method dependency, any callable will do? ;; `std::function` type erasure
󰠗 What type of dependency injection should be used when you can't modify or inherit from the dependency? ;; Template injection or Adapter pattern
󰠗 Interface or template: which to prefer by default? ;; Prefer templates when only one runtime impl exists; interfaces when dynamic dispatch is genuinely required

## Usage
Original code
```cpp
class DcMotor {
public:
   int getSpeed();
   void stop();
};

class Car {
public:
   void controlSpeed() {
       if (mMotor.getSpeed() > 50) {
           mMotor.stop();
       }
   }
private:
   DcMotor mMotor;
};
```

### Interface Injection
Use when: multiple runtime implementations exist, or the dependency crosses a library/module boundary. Enables full GMock interaction testing.
Not when: only one implementation will ever exist (templates are cheaper), or you cannot inherit from the class (use templates or Adapter).

Source code
```cpp
struct Motor {
   virtual ~Motor()       = default;
   virtual int getSpeed() = 0;
   virtual void stop()    = 0;
};

class Car {
public:
   Car(Motor& motor) : mMotor{motor} {}

   void controlSpeed() {
       if (mMotor.getSpeed() > 50) {
           mMotor.stop();
       }
   }
private:
   Motor& mMotor;
};
```

Production and mock 
```cpp
// Production implementation
class DcMotor : public Motor
{
public:
   int getSpeed() override;
   void stop() override;
};

// Mock implementation
struct MockMotor : public Motor
{
   MOCK_METHOD(int, getSpeed, (), (override));
   MOCK_METHOD(void, stop, (), (override));
};
```

### Template injection
Use when: single runtime implementation, performance-critical (no vtable overhead), or no interface exists. The mock needs no inheritance — just matching method signatures (duck-typed).

Source code
```cpp
struct MockMotor {
   MOCK_METHOD(int, getSpeed, (), ());
   MOCK_METHOD(void, stop, (), ());
};

template<typename MotorType>
class Car {
public:
   Car(MotorType& motor) : mMotor{motor} {}
   void controlSpeed() {
       if (mMotor.getSpeed() > 50) {
           mMotor.stop();
       }
   }
private:
   MotorType& mMotor;
};
```



```cpp
TEST(CarTest, controlSpeedWhenSpeedTooHighWillStop) {
   MockMotor motor;
   Car<MockMotor> car{motor};
   EXPECT_CALL(motor, getSpeed())
       .WillOnce(Return(100));
   EXPECT_CALL(motor, stop());
   car.controlSpeed();
}

TEST(CarTest, controlSpeedWhenSpeedLowWillNotStop) {
   MockMotor motor;
   Car car{motor}; // C++17 and up
   EXPECT_CALL(motor, getSpeed())
       .WillOnce(Return(49));
   EXPECT_CALL(motor, stop()).Times(0);
   car.controlSpeed();
}
```

Production and mock

### Type erasure
Store dependencies as [[Cpp std function]] — accepts any callable (lambda, free function, functor, bound member) matching the signature. No interface, no vtable, no inheritance required.

Key snippets:
 `using SpeedGetter = std::function<int()>;` ;;; alias for each dependency; store as member

 `Car(SpeedGetter gs, Stopper s) : mGetSpeed{std::move(gs)}, mStop{std::move(s)} {}` ;;; inject callables via constructor; use `std::move` to avoid copying

 `if (mGetSpeed() > 50) mStop();` ;;; invoke through the stored function — no virtual dispatch

Test — inject lambdas directly, no mock framework needed:
 `Car car{[] { return 100; }, [&] { stopped = true; }};` ;;; lambdas satisfy the function signatures

 `EXPECT_TRUE(stopped);` ;;; verify behaviour via captured state

See: [[Cpp std function]], [[Cpp std move]], [[Cpp std invoke]]
Caveat: harder to set up multi-call interaction expectations — prefer interface + GMock when interaction complexity is high.
![[DP Testing Dependency Injection.png]]

## Design for Mockability
Rules for writing code that is naturally testable via DI:

󰙎 Prefer constructor injection ;;; dependencies visible in the type signature; impossible to create an object in an invalid state
󰙎 Depend on abstractions ;;; store an interface reference, template parameter, or `std::function` — never a concrete type unless it is a value object
󰙎 Narrow interfaces (ISP) ;;; split large interfaces by responsibility; one role per interface is easier to mock and stub
󰙎 Avoid internal `new` ;;; if a class constructs its own dependency, it owns it forever and it cannot be swapped in tests — inject instead
󰙎 Avoid static/global state ;;; untestable; cannot be swapped at test time; infects all callers
󰙎 Avoid `final` on injectable classes ;;; `final` blocks inheritance-based mocking

