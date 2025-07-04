---
type: note
---
# Background
A value type that derives implicitly from `System.ValueType`, which is derived from `System.Object`
- Structures are useful for representing values whose memory requirements are small, and for passing values as by-value parameters to methods that have strongly typed parameters.
- In .NET, all primitive data types are defined as structures.
- For each value type, the common language runtime supplies a corresponding boxed type, which is a class that has the same state and behavior as the value type. 