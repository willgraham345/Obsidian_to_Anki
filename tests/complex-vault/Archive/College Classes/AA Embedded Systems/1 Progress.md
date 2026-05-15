### Unit vs Integration Testing
 - [x] Write `zephyr/prj.conf`
 - [x] Find main function, interrupt handlers and thread entry points
 - [x] Identify the behavioral code in these contexts
 - [x] Find any infinite loops in the code (main setup, main loop)
    - [x] Identify the difference between setup and repeated execution
    - [x] Identify any time dependent behavior, especially delays between iterations

#### Decompose Code into Functions Technique and Activity 
- [x] Create new header file in the `lib/lab1/include` directory to hold definition of your function
- [x] Create new source file in the `lib/lab1/src` directory to hold your function
- [x] Take a block of code you identified in the infinite loop of your main execution context. Create a function in your new files, and move all of the code in a block into it
    - [x] Done to an extent (main loop finished)
- [x] Put a call to the function where the code used to be.
- [x] Compile the code. You will be missing includes, variables, references, outputs, etc.



#### Convert State and Dependencies to Inputs and Outputs Technique and Activity
- [x] For each missing variable or reference in the function you created, add input to the function
- [x] If you need to return more than one value, pass it as an `out param`, which is a pointer to a value in the caller that the function will populate. 
- [x] Once your function is compiling, switch to the original location it was called from and populate the parameters of the function.

#### Break dependencies and separate concerns technique and activity
- [x] In the function you extracted, identify any references to global variables, HAL devices, system functions, etc.
- [x] See if you can remove the dependency by separating the concern of your code from the behavior of the dependency. For example, you could move a call to get data from a peripheral to the caller and pass the data into your function instead.
- [x] Create new inputs to your function for pointers to dependencies.

#### Write the Test Technique and Activity
- [x] Make sure your code compiles.
- [x] Commit the code you extracted.
- [x] Add the following lines to your platformio.ini file.





- [x] Create a new file in the test directory.
  - It can have any name, but by convention it has a similar name to the file you put your code in.
	  - This can make it easier for another person to find the test later.
  - Add the code template from test.c in this directory to the file.
- [x] Remove the example tests and add your own.
  - Your test must include a `setUp` and `tearDown` function. You can put any code in here that will be run at before and after each of test.
  - Your tests must have a `main` function.
	  - This sets up the testing framework with the `UNITY_BEGIN` and `UNITY_END` macros.
	  - For each test, you will call the `RUN_TEST` macro.
Tests by convention start with test_ but don't need to.
Each test should generally demonstrate one possible case. Having multiple tests instead of one big one makes it easier to identify what is failing.
- [x] In your test, use any one of the GPIO peripherals available.
- [x] Exercise the function under test and check the state of the GPIO peripherals.
Hint: check the docs at https://docs.zephyrproject.org/2.7.5/reference/peripherals/gpio.html for what functions are available to check the state of the GPIO peripheral.
- [x] If you find yourself having trouble setting up the test, you have too many parameters, or a dependency is getting in the way, try refactoring the function further. Follow the same techniques from the previous activities.



Testing command
to test running
`pio run --environment disco_f0724b --without-uploading`
`pio test --without-uploading --environment disco_f072rb`