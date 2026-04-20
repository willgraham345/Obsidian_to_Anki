# Activity 1
1. For each of the cases, use an oscilloscope to measure jitter and drift of the time keeping method.
    1. Read through the code, see what it does.
    2. Load the code onto your board (e.g. `pio run -t upload -e sleep`)
    3. Measure the jitter (see instructions below)
    4. Once you are finished, modify the code - introduce a k_busy_wait call after the GPIO is toggled. 1.Busy wait sets the processor in a tight loop (usually a counter loop with a noop body). 1. Measure the jitter with several delay values.
2. Measure the jitter of the Agilent function generator operating at the same frequency for comparison.

## Sleep
| Sleep Normal   | Min     | Max    | Mean    | StdDev    |
| -------------- | ------- | ------ | ------- | --------- |
| Period    (ms) | 2.19472 | 2.1956 | 2.19472 | 176 ns    |
| Frequency (Hz) | 455.518 | 455.77 | 455.595 | 28.35 mHz |
| Duty Cycle  (%)   | 49.98 % | 50.04% | 50.04%  |.01%           | 

| Sleep w/k_busy_wait  | Min     | Max     | Mean    | StdDev     |
| -------------- | ------- | ------- | ------- | ---------- |
| Period (ms)    | 4.1816  | 4.18792 | 4.18704 | 246.4 ns   |
| Frequency (Hz) | 238.794 | 238.912 | 238.834 | 14.554 mHz |
| Duty Cycle (%)    | 50      | 50.02   | 50.02   | 0.00       |

## Kernel

| Kernel Normal  | Min     | Max     | Mean     | StdDev |
| -------------- | ------- | ------- | -------- | ------ |
| Period (ms)    | 1.99584 | 1.99584 | 1.999584 | 0      |
| Frequency (Hz) | 500.951 | 501.103 | 501.037  | 31 mHz |
| Duty Cycle (%)     | 50.0    | 50.04   | 50.04    | 0.01       |

| Kernel w/k_busy_wait | Min     | Max      | Mean    | StdDev    |
| -------------------- | ------- | -------- | ------- | --------- |
| Period (ms)          | 3.98816 | 3.989904 | 3.98904 | 431.2 ns  |
| Frequency  (Hz)      | 250.674 | 250.756  | 250.716 | 19.68 mHz |
| Duty Cycle (%)       | 49.9    | 50.02    | 50.02   | 0.01          |

## Busy 
| Busy           | Min     | Max     | Mean    | StdDev      |
| -------------- | ------- | ------- | ------- | ----------- |
| Period (ms)    | 1.99958 | 2.00035 | 2.00002 | 150.7 ns    |
| Frequency (Hz) | 499.87  | 500.17  | 499.97  | 55.7136 mHz |
| Duty Cycle (%) | 49.97   | 50.05   | 50.01   | 0            |

| Busy w/k_busy_wait | Min     | Max     | Mean    | StdDev     |
| ------------------ | ------- | ------- | ------- | ---------- |
| Period (ms)        | 3.99773 | 3.9949  | 3.99861 | 233.2 ns   |
| Frequency (Hz)     | 250.01  | 250.141 | 250.081 | 17.963 mHz |
| Duty Cycle (%)     | 49.98   | 50.03   | 50.01   | 0          | 



# Activity 2
1. Review and run the code `gpio_interrupt.c`
2. Attach the Sync output from the signal generator to the oscilloscope and use as the trigger.
3. Drive the board with the signal generator output on pin A1.
    1. **Make sure to check the output voltages on the oscilloscope before attaching it to your board or you'll let the magic smoke out!** Set amplitude HiLevel to 3.3V, LoLevel to 0.0 V.
4. Measure the delay between the sync signal and the output from the board.
5. Increase the delay using a busy wait loop as before.


# Activity 3
1. Modify the interrupt handler by adding in a message queue.
2. From the interrupt handler send a message.
3. Create a new thread that reads messages from the queue and toggles the output pin when a message is received.
4. Measure the latency again.
5. Add a busy wait delay to the message handler.