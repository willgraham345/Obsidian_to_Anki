---
type: note
---
# Things to keep in mind
- Everything in C is a pointer with some flavor added
- Remember to increment your pointer within the loop if you want to iteratively change values
## Typical Pointer Setup and use
```c
// 1. Create pointer of the right type
float *f;
// 2. Assign it to a memory location
f = &boat;
// 3. Use the pointer
printf("%.0f", *f);
```



# Usage
## Pointers Parenthesis and Math
| Pointer thing | Memory Address                   | Memory Contents              |
| ------------- | -------------------------------- | ---------------------------- |
| `p`           | Yep                              | Nope                         |
| `*p`          | Nope                             | Yep                          |
| `*p++`        | Incremented after value is read  | Unchanged                    |
| `*(p++)`      | Incremented after value is read  | Unchanged                    |
| `(*p)++`      | Unchanged                        | Incremented after it's used  |
| `*++p`        | Incremented before value is read | Unchanged                    |
| `*(++p)`      | Incremented before value is read | Unchanged                    |
| `++*p`        | Unchanged                        | Incremented before it's used |
| `++(*p)`      | Unchanged                        | Incremented before it's used |
| `p*++`        | Not a pointer                    | Not a pointer                |
| `p++*`        | Not a pointer                    | Not a pointer                |

## Pointers and Array Brackets
| Array Notation | Pointer Equivalent |
| -------------- | ------------------ |
| `array[0]`     | `*a`               |
| `array[1]`     | `*(a+1)`           |
| `array[x]`     | `*(a+x)`                   |

# Examples
## Using Pointers to Map a Function Onto an Array
### Main Function Call
```c
void func_to_apply(int x){}


int main(void)
{
	map(data, 5, func_to_apply);
}
```

### Map.c
```c
void map(int *input_list, int list_length, int (*applied_fun)(int))

{

for (int i = 0; i < list_length; i++, input_list++)

*input_list = applied_fun(*input_list);

}
```

