Can you create a left to right mermaid chart that describes an ASIC with following elements:
- 32 input wires. These can be grouped together, and labelled as one node if there is too much going on in the graph. They are titled as  `w0`, `w1`, and so forth.
- A `receiver_parser` subgraph. This takes in 32 input wires, and assigns four 12-bit register outputs of x1 through x4.
- A module titled `sel` that performs the hadamard transform and 2's complement on the four outputs from `receiver_parser`. It outputs four 12-bit registers t1-t4. It also has a `sel_tx_ready` register and a 4-bit `sel_count` register as an output

```mermaid
classDiagram

class hadamard_transform_ASIC {
receiver_parser 
sel
sum
}

class input_wires {
	wire w0
	wire w1
	...
	wire w31
}


class receiver_parser {
[11:0] reg x1
[11:0] reg x2
[11:0] reg x3
[11:0] reg x4
}

class sel {
[11:0] reg t1
[11:0] reg t2
[11:0] reg t3
[11:0] reg t4
reg sel_tx_ready
hadamardTransform(x1, x2, x3, x4)
twosComplement(t1, t2, t3, t4)
}

class sum {
	v1
	v2
	...
	v3
	reg sum_tx_ready
}

input_wires -- > receiver_parser
receiver_parser --> sel
sel --> sum

```
