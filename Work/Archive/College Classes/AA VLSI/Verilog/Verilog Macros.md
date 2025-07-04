Defined with a grave mark (see below), and are simple text substitutions. Do not permit arguments
```verilog
`define macro_name value
```



## Table (note, there should be a \` before all of these statements)
| Compiler Directives                 | Description                              |
|------------------------------------|------------------------------------------|
| `resetall`                          | Resets all compiler directives to default values.                     |
| `define`                            | Text-macro substitution.                                              |
| `timescale 1ns / 10ps`              | Specifies time unit/precision.                                       |
| `ifdef`, `else`, `endif`           | Conditional compilation.                                             |
| `include`                           | File inclusion.                                                       |
| `signed`, `unsigned`                | Operator selection (OVI 2.0 only).                                   |
| `celldefine`, `endcelldefine`       | Library modules.                                                      |
| `default_nettype wire`              | Default net types.                                                    |
| `unconnected_drive pull0 pull1`     | Unconnected drive pull0 or pull1. There should be a \| in there.                                    |
| `nounconnected_drive`               | Pullup or down unconnected ports.                                    |
| `protect`, `endprotect`            | Encryption capability.                                                |
| `protected`, `endprotected`        | Encryption capability.                                                |
| `expand_vectornets`, `noexpand_vectornets`, `autoexpand_vectornets` | Vector expansion options.  |
| `remove_gatename`, `noremove_gatenames` | Remove gate names for more than one instance.              |
| `remove_netname`, `noremove_netnames` | Remove net names for more than one instance.              |
