---
type: note
---
## Performance of a computer
Latency = time that it takes to complete a task (memory request)

Bandwidth = Rate of completion of a task (in this case, memory requests per second)

### Metrics
MIPS = million instructions per second
Clock frequency
FLOPS = Floating operations per second
Peak ratings


## Formulas
A is $n$ times faster than B means: $\dfrac{B_{execution time}}{A_{execution time}} x 100 = m$ 

## Principles of CA Design
Take advantage of parallelism
- System level: Multiple processors, multiple disks
- Processor level: operate on multiple instructions at once
- Circuit level: Operate on multiple bits at once (CLA, ALU)
Principle of locality
- Spatial and temporal locality
- 90% of programming executing in 10% of code
	- E.g. Caches
Focus on the common cause
- Amdahl’s law, CPU performance equation
- RISC design principle

Amdahl’s Law
- Speedup due to an enhancement $E$

$Speedup(S) = \dfrac{A}{B}$
- A = Execution time before $E$
- B = Execution time after $E$
- Suppose that enhancement $E$ accelerates a fraction $F$ of the task by a factor $S$, and the remainder of the task is unaffected. What is the execution time after Speedup(S)

$Executiontime_{after} = ExecTime_{before}[(1 - F) + F/S]$
$Speedup(S) = \dfrac{ExecTime_{before}}{ExecTime_{after}} = \dfrac{1}{[(1-F) + F/S]}$

## Factors that affect CPU performance
IC = Instruction Count
- Compiler, ISA
Cycles per instruction (CPI)
- ISA, Microarchitecture
Clock time (1/f)
- Microarchitecture, technology


$CPU_{time} = IC * CPI * ClockTime$
- CPU time = execution time
- IC = number of instructions executed (Instruction count)
- CPI = Number of average clock cycles per instruction

## Improving CPU Performance
IC:
- Compiler optimizations (constant folding, constant propagation)
- ISA (more complex instructions)
CPI: 
- Microarchitecture (Pipelining, out-of-order execution, branch prediction)
- Compiler (Instruction scheduling)
- ISA (Simpler instructions)
Clock period:
- Technology (Smaller transistors)
- ISA (Simple instructions that can be easily decoded)
- Microarchitecture (simple architecture)
