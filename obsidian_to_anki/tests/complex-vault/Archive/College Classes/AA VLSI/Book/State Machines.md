# Mealy Machine
FSM whose output depends on the present state, as well as the present input.

## Description
6 tuple
- **Q**
	- is a finite set of states.
- **∑**
	- is a finite set of symbols called the input alphabet.
- **O**
	- is a finite set of symbols called the output alphabet.
- **δ**
	- is the input transition function where δ: Q × ∑ → Q
- **X**
	- is the output transition function where X: Q × ∑ → O
- **q0**
	- is the initial state from where any input is processed (q0 ∈ Q).

# Moore Machine
FSM whose outputs depend only on the present state
## Description
- **Q**
	- is a finite set of states.
- **∑**
	- is a finite set of symbols called the input alphabet.
- **O**
	- is a finite set of symbols called the output alphabet.
- **δ**
	- is the input transition function where δ: Q × ∑ → Q
- **X**
	- is the output transition function where X: Q → O
- **q0**
	- is the initial state from where any input is processed (q0 ∈ Q).
# Moore vs Mealy State Machines
| Mealy Machine                                                                                                                         | Moore Machine                                                                                                                                 |
| ------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------- |
| Output depends both upon the present state and the present input                                                                      | Output depends only upon the present state.                                                                                                   |
| Generally, it has fewer states than Moore Machine.                                                                                    | Generally, it has more states than Mealy Machine.                                                                                             |
| The value of the output function is a function of the transitions and the changes, when the input logic on the present state is done. | The value of the output function is a function of the current state and the changes at the clock edges, whenever state changes occur.         |
| Mealy machines react faster to inputs. They generally react in the same clock cycle.                                                  | In Moore machines, more logic is required to decode the outputs resulting in more circuit delays. They generally react one clock cycle later. |
