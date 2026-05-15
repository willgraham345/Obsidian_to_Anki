---
type: note/concept
headings:
ai_generated: true
date created: Tuesday, August 20th 2024, 2:05:34 pm
date modified: Wednesday, April 15th 2026, 4:25:14 pm
tags: [programming/cs]
template:
template-version:
---

# Summary
󰙎 CS Binary Storage ;;; Binary (base-2), hex (base-16), decimal (base-10) conversions, common values, and storage representations

# Additional Background
4 bits = 1 hex digit (nibble). 8 bits = 1 byte = 2 hex digits. Hex is shorthand for binary — each digit maps directly to 4 bits.

## Concepts of Note

### Base Conversion Table (0–15)

| Dec | Bin  | Hex |
| --- | ---- | --- |
| 0   | 0000 | 0   |
| 1   | 0001 | 1   |
| 2   | 0010 | 2   |
| 3   | 0011 | 3   |
| 4   | 0100 | 4   |
| 5   | 0101 | 5   |
| 6   | 0110 | 6   |
| 7   | 0111 | 7   |
| 8   | 1000 | 8   |
| 9   | 1001 | 9   |
| 10  | 1010 | A   |
| 11  | 1011 | B   |
| 12  | 1100 | C   |
| 13  | 1101 | D   |
| 14  | 1110 | E   |
| 15  | 1111 | F   |

### Powers of 2

| Power | Decimal       | Hex           | Common Name |
| ----- | ------------- | ------------- | ----------- |
| 2^0   | 1             | 0x1           |             |
| 2^4   | 16            | 0x10          |             |
| 2^7   | 128           | 0x80          |             |
| 2^8   | 256           | 0x100         |             |
| 2^10  | 1,024         | 0x400         | 1 KiB       |
| 2^16  | 65,536        | 0x10000       | 64 KiB      |
| 2^20  | 1,048,576     | 0x100000      | 1 MiB       |
| 2^30  | 1,073,741,824 | 0x40000000    | 1 GiB       |
| 2^32  | 4,294,967,296 | 0x100000000   | 4 GiB       |

### Common Hex Sentinels

| Hex    | Dec    | Meaning                    |
| ------ | ------ | -------------------------- |
| 0x00   | 0      | Null / zero                |
| 0x7F   | 127    | Max signed byte            |
| 0x80   | 128    | Min negative signed byte   |
| 0xFF   | 255    | Max unsigned byte          |
| 0x7FFF | 32,767 | Max signed 16-bit          |
| 0xFFFF | 65,535 | Max unsigned 16-bit        |
| 0xDEADBEEF | 3,735,928,559 | Debug/poison marker |
| 0xCAFEBABE | 3,405,691,582 | Java class file magic |

### Representations
󰙎 nibble ;;; 4 bits — maps to exactly 1 hex digit
󰙎 byte ;;; 8 bits = 2 hex digits; unsigned range 0–255
󰙎 0b prefix ;;; binary literal notation (e.g. `0b1010` = 10)
󰙎 0x prefix ;;; hexadecimal literal notation (e.g. `0xFF` = 255)
󰙎 two's complement ;;; standard signed integer encoding; flip bits + 1 = negation

## IEEE 754 Floating Point
Standard binary float storage format.
󰙎 single precision ;;; 32 bits — 1 sign + 8 exponent + 23 mantissa
󰙎 double precision ;;; 64 bits — 1 sign + 11 exponent + 52 mantissa
󰙎 sign bit ;;; 0 = positive, 1 = negative
󰙎 exponent ;;; biased encoding (bias = 127 for single, 1023 for double)
󰙎 special values ;;; 0x7F800000 = +Inf, 0xFF800000 = -Inf, NaN when exponent all 1s and mantissa ≠ 0

## Q Number Format
Texas Instruments fixed-point notation. ARM uses variant.
󰙎 Q format ;;; Qm.n = m integer bits + n fractional bits (e.g. Q8.8 = 8 integer, 8 fraction)
󰙎 resolution ;;; 2^-n for Qm.n format

## Flashcards
󰠗 How many bits per hex digit? ;; 4 bits (nibble)
󰠗 0xFF in decimal? ;; 255
󰠗 0b1010 in decimal? ;; 10
󰠗 2^10 = ? ;; 1,024 (1 KiB)
󰠗 Max unsigned byte value? ;; 255 (0xFF)
󰠗 Max signed byte value? ;; 127 (0x7F)
󰠗 Convert 0xAB to binary ;; 1010 1011
󰠗 How many bytes in a 32-bit int? ;; 4 bytes (8 hex digits)
󰠗 Single precision float size? ;; 32 bits: 1 sign + 8 exp + 23 mantissa
