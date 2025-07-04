I want the four inputs (x1, x2, x3, and x4) to not be a vector but rather have 12 wires feeding in, with a two bit number selecting where these inputs should feed. The idea is to multiplex x1, x2, x3, and x4 into a parallel network of input wires which can toggle different registers for storing the rows. 


```mermaid
graph LR
	subgraph selector
		x
		clk
		reset
		tx_ready
		t1_reg
		t2_reg
		t3_reg
		t4_reg
		sel_tx_ready
		sel_count
	end

	subgraph sum_and_output
		sum_count
	end
```