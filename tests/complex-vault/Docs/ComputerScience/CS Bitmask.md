---
type: note/concept
headings:
  - "[[#Examples]]"
implements:
  - "[[CS Binary Storage]]"
ai_generated: true
concept_of:
  - "[[CS Data Structures]]"
date created: Tuesday, March 31st 2026, 12:00:00 pm
date modified: Tuesday, March 31st 2026, 12:57:29 pm
item_of:
  - "[[CS Data Structures]]"
tags: [programming/cs, programming/cs/data-structures]
template: "[[base_note_template]]"
template-version: 1.0.2
---

# Summary
󰙎 CS Bitmask ;;; An integer used as a compact array of boolean flags, manipulated via bitwise operators. An easy and graphical way of managing a series of flags at a glance.

# Additional Background
## Concepts of Note
󰙎 bitmask ;;; an integer treated as an ordered sequence of bits; bit k occupies the 2^k position. Each bit is a true/false, and 
󰙎 bit flag ;;; a single bit within a bitmask representing one boolean condition. Think of this as the "index" of the flags.
󰙎 mask ;;; a bitmask used to isolate, set, or clear specific bits via AND / OR / XOR

Each bit position is independently meaningful. A 32-bit integer stores 32 independent flags in a single CPU word — far more compact than an array of booleans.

### Testing Composite Masks
󰙎 test all bits set ;;; `(n & mask) == mask` — every bit in mask is 1 in n
󰙎 test any bit set ;;; `(n & mask) != 0` — at least one bit in mask is 1 in n
󰙎 OR-combine flags ;;; `A | B | C` — build a composite mask from individual named constants

## Usage
### Access Control / Permissions
Unix file permissions encode read / write / execute for owner, group, and world in 9 bits:
 `mode & 0o400` ;;; test owner-read permission via octal mask

### Feature Flags
Enable, disable, and query named capabilities without separate boolean fields:
 `flags |= FEATURE_X` ;;; enable feature X
 `flags &= ~FEATURE_X` ;;; disable feature X
 `flags & FEATURE_X` ;;; check if feature X is enabled

### Set Membership (bit sets)
Represent any subset of integers 0–63 as a single `uint64`. Set operations reduce to single instructions:
󰙎 union ;;; `a | b`
󰙎 intersection ;;; `a & b`
󰙎 complement ;;; `~a`
󰙎 difference ;;; `a & ~b`

### Bitwise Operations
Core operations on value `n` at bit position `k` (0-indexed from LSB):

 `n | (1 << k)` ;;; set bit k — force to 1
 `n & ~(1 << k)` ;;; clear bit k — force to 0
 `n ^ (1 << k)` ;;; toggle bit k — flip current value
 `(n >> k) & 1` ;;; test bit k — returns 0 or 1
 `n & mask` ;;; extract bits — keep only positions set in mask
 `n & (n - 1)` ;;; clear lowest set bit (useful in bit-counting loops)
 `n & -n` ;;; isolate lowest set bit only

## Examples

```
0x0001 = 0000 0000 0000 0001
0x0002 = 0000 0000 0000 0010
0x0004 = 0000 0000 0000 0100
0x0008 = 0000 0000 0000 1000
0x0010 = 0000 0000 0001 0000
...
0x8000 = 1000 0000 0000 0000
```

So a status value of `0x0041` means three flags are set at once:

```
0x0041 = 0000 0000 0100 0001
                   ^  ^    ^
             UNSYNC  FLL  PLL
```