```verilog
always @(rst)// simple if -else
	if (rst)
		// procedural assignment
		q = 0;
	else // remove the above continous assign
		deassign q;
	always @(WRITE or READ or STATUS)
	begin
	// if - else - if
		if (!WRITE) begin
			out = oldvalue ;
		end
		else if (!STATUS) begin
			q = newstatus ;
			STATUS = hold ;
		end
		else if (!READ) begin
			out = newvalue ;
	end
end
```