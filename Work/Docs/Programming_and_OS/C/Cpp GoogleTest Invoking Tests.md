---
type: note/workflow
workflows: ["[[CMake GoogleTest Building]]"]
date created: Tuesday, August 20th 2024, 2:05:33 pm
date modified: Friday, January 3rd 2025, 11:49:43 am
workflow_of: ["[[Cpp GoogleTest]]"]
---
# Background
`TEST()` and `TEST_F()` implicitly register with GoogleTest
After defining all tests, run them with `RUN_ALL_TETS()`
- Return `0` if all tests are successful, `1` if not. 
- 

# Usage
## Example

Create a `hello_test.cc` in the `my_project` directory
```cpp
#include <gtest/gtest.h>

// Demonstrate some basic assertions.
TEST(HelloTest, BasicAssertions) {
  // Expect two strings not to be equal.
  EXPECT_STRNE("hello", "world");
  // Expect equality.
  EXPECT_EQ(7 * 6, 42);
}
```
Add to end of `CMakeLists.txt`
```cmake
enable_testing()

add_executable(
  hello_test
  hello_test.cc
)
target_link_libraries(
  hello_test
  GTest::gtest_main
)

include(GoogleTest)
gtest_discover_tests(hello_test)
```


```shell
my_project$ cmake -S . -B build
-- The C compiler identification is GNU 10.2.1
-- The CXX compiler identification is GNU 10.2.1
...
-- Build files have been written to: .../my_project/build

my_project$ cmake --build build
Scanning dependencies of target gtest
...
[100%] Built target gmock_main

my_project$ cd build && ctest
Test project .../my_project/build
    Start 1: HelloTest.BasicAssertions
1/1 Test #1: HelloTest.BasicAssertions ........   Passed    0.00 sec

100% tests passed, 0 tests failed out of 1

Total Test time (real) =   0.01 sec
```

## RUN_ALL_TESTS()
Runs *all* tests in your link unit.
Can be from different test suites, or even different source files. 
NOTE: Do not ignore return value for `RUN_ALL_TESTS()` or you'll get a compiler error.
- Should only be called once. Calling it more than once will conflict with thread-safe death tests.

### When invoked:
- Saves the state of all GoogleTest flags.
- Creates a test fixture object for the first test.
- Initializes it via `SetUp()`.
- Runs the test on the fixture object.
- Cleans up the fixture via `TearDown()`.
- Deletes the fixture.
- Restores the state of all GoogleTest flags.
- Repeats the above steps for the next test, until all tests have run.

### main function
- Typically not needed to write this. Instead link to `gtest_main`, which is a great entry point. 
- If you do write your own `main` function, it should return the value of `RUN_ALL_TESTS()`

#### Example main
```cpp
#include "this/package/foo.h"

#include <gtest/gtest.h>

namespace my {
namespace project {
namespace {

// The fixture for testing class Foo.
class FooTest : public testing::Test {
 protected:
  // You can remove any or all of the following functions if their bodies would
  // be empty.

  FooTest() {
     // You can do set-up work for each test here.
  }

  ~FooTest() override {
     // You can do clean-up work that doesn't throw exceptions here.
  }

  // If the constructor and destructor are not enough for setting up
  // and cleaning up each test, you can define the following methods:

  void SetUp() override {
     // Code here will be called immediately after the constructor (right
     // before each test).
  }

  void TearDown() override {
     // Code here will be called immediately after each test (right
     // before the destructor).
  }

  // Class members declared here can be used by all tests in the test suite
  // for Foo.
};

// Tests that the Foo::Bar() method does Abc.
TEST_F(FooTest, MethodBarDoesAbc) {
  const std::string input_filepath = "this/package/testdata/myinputfile.dat";
  const std::string output_filepath = "this/package/testdata/myoutputfile.dat";
  Foo f;
  EXPECT_EQ(f.Bar(input_filepath, output_filepath), 0);
}

// Tests that Foo does Xyz.
TEST_F(FooTest, DoesXyz) {
  // Exercises the Xyz feature of Foo.
}

}  // namespace
}  // namespace project
}  // namespace my

int main(int argc, char **argv) {
  testing::InitGoogleTest(&argc, argv);
  return RUN_ALL_TESTS();
}
```