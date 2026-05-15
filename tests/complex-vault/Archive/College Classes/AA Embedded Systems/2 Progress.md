# Macro conditionals
In the `uart_hello.*` files, a functions is defined which uses a UART device. It echoes back any character received (in uppercase), until a newline character is received.

1. ~~Use the preprocessor to conditionally control the implementation of the system uart functions.~~
    1. ~~Define new functions `test_uart_out` and `test_uart_in` in your header file. Wrap them in a conditional, testing for the definition of TESTING_ENV.~~
    2. ~~Wrap the call to `uart_poll_out` and `uart_poll_in` in a preprocessor conditional~~
2. ~~We'll implement the test functions next.~~

# Testing with Mocks

## Controlled
- [x] In your test code, define TESTING_ENV.
- [x] Implement the `test_uart_in` and `test_uart_out` functions in your test code.
- [x] Implement the `test_uart_in` to return sequence of UART bytes.

## Asserting Functionality
- [x] Implement the `test_uart_out` UART sending behavior, asserting that the correct sequence of bytes is sent.' ✅ 2024-06-21

## Manipulating Bindings with Function Pointers
#### Activity

The higher order function `map` takes as input a list or other container, a function to apply to each element, and returns a list of the same size after applying the function to each element.

- [x] Copy the test_map.c file into your project. ✅ 2024-06-21
- [x] Implement the map function. ✅ 2024-06-21


- [x] Create a new version of the UART code, using function pointers for the system calls. (be sure to use new non-conflicting function names) ✅ 2024-06-21


## Change Static Linking
- [x] Create a new test, and implement `uart_poll_in` and `uart_poll_out` functions directly in the test. ✅ 2024-06-21




# How to run the Project
`pio run -e disco_f072rb --without-uploading`
`pio test --environment disco_f072rb --without-uploading`
- For verbose testing: `pio test -vv --environment disco_f072rb --without-uploading`