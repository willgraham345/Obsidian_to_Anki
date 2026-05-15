 Boolean Symbols
 rr
| Symbol           | Meaning | Boolean Logic  |
| ---------------- | ------- | -------------- |
| `*`              | AND     | Multiplication |
| `+`              | OR      | Addition       |
| `'`              | NOT     |                |
| `^`              | XOR     |                |
| $\overline{A*B}$ | NAND    |                |
| $\overline{A+B}$ | NOR     |                |

# Boolean Algebra
## Boolean Identities
| Pattern                   | Result |
| ------------------------- | ------ |
| $A +$TRUE                 | $A$    |
| $A+$FALSE                 | A      |
| $A*$FALSE                 | FALSE  |
| $A*$TRUE                  | TRUE   |
| $\overline{\overline{A}}$ | $A$    |
| $A * \overline{A}$        | FALSE  |
| $A+\overline{A}$          | TRUE   |
| $A*A$                     | $A$    |
| $A+A$                     | $A$       |



## Overline AND/OR
| Pattern                | Result                        |
| ---------------------- | ----------------------------- |
| $\overline{A \cdot B}$ | $\overline{A} + \overline{B}$ |
| $\overline{A+B}$       | $\overline{A}*\overline{B}$                                |

## Distribution
| Pattern             | Result                      |
| ------------------- | --------------------------- |
| $A * (B + C)$       | $(A \cdot B) + (A \cdot C)$ |
| $(A * B) + (A * C)$ | $(A + B) * (A + C)$         |
| $A*(A+B)$           | $A$                         |
| $A+(A*B)$           | $A$                            |

## Multiplication w/Parenthesis








# Other
| Notation   | LaTeX Symbol            | Meaning               | True When:                                            |
| ---------- | ----------------------- | --------------------- | ----------------------------------------------------- |
| T or 1     | $T$ or $1$              | True                  |                                                       |
| F or 0     | $F$ or $0$              | False                 |                                                       |
| AND (·, &) | $A \cdot B$ or $A \& B$ | Logical AND           | $A$ and $B$ are true                                  |
| OR         | $A + B$                 | Logical OR            | Either $A$ and $B$ is true                            |
| NOT (¬, !) | $\neg A$ or $\lnot A$   | Logical NOT           | Neither $A$ or $B$ is true                            |
| XOR        | $A \oplus B$   and $A ^\wedge B$         | Exclusive OR          | If $A$ and $B$ are true, or $A$ and $B$ are both true |
| NAND       | $\overline{A \cdot B}$  | NOT AND               | True unless both inputs are True                      |
| NOR        | $\overline{A + B}$      | NOT OR                | True when both inputs are false, false in all other cases                                                      |
| XNOR       | $\overline{A \oplus B}$ | NOT XOR (Equivalence) | True when both inputs are the same                    |





