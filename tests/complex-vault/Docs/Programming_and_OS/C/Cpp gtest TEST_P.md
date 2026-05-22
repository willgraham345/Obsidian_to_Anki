---
summary: Parameterized tests let you test your code with different parameters while avoiding writing multiple copies of the same test.
headings: ["[[#Concepts of Note]]", "[[#Examples]]", "[[#Usage]]"]
type: note/item
date created: Tuesday, September 16th 2025, 9:18:32 am
date modified: Tuesday, September 16th 2025, 9:56:40 am
---

# Summary
`VIEW[**{summary}**][text(renderMarkdown)]`

# Additional Background
## Concepts of Note
[Testing Reference \| GoogleTest](https://google.github.io/googletest/reference/testing.html#INSTANTIATE_TEST_SUITE_P)
- Basic workflow
	1. Create a parameterized test fixture
	2. Fill it with values using a predefined type
	3. Grab a value in the `TEST_P` using `GetParam()`
	4. 

## Usage
- [p] `TEST_P(TestSuiteName, TestName) {`
      `... test body ... `
      `{` = Creates a parameterized google test named `TestName`, within the suite `TestSuiteName` in gtest. Note, the names cannot contain underscores. = #lang/test/gtest/macros #lang/test/gtest/create-a-test #lang/test/gtest/parameterized-tests 
  `GetParam()` ;;; Parameterized test macro, which grabs the test fixture from the `TestWithParam<T>` class. = #lang/test/gtest/macros #lang/test/gtest/fixtures #lang/test/gtest/parameterized-tests
<!--ID: 1758253289826-->

  `INSTANTIATE_TEST_SUITE_P( instantiationName, SuiteName, param_generator)` ;;; Instantiate a value-parameterized test using `instatiationName`, `SuiteName`, and `param_generator`. = #lang/test/gtest/parameterized-tests #lang/test/gtest/macros 
<!--ID: 1758253289832-->

  `Values(v1, v2, ..., vN)` ;;; Create sequence `{v1, v2, ..., vM}` in a parameterized gtest. Defined in the `::testing` namespace. = #lang/test/gtest/parameterized-tests 
<!--ID: 1758253289838-->

  `ValuesIn(container)` ;;; Create values from a C-style array, an STL-style container, or an iterator range `[begin, end)` parameterized gtest. Defined in the `::testing` namespace. = #lang/test/gtest/parameterized-tests 
<!--ID: 1758253289844-->

  `Range(begin, end, [,step])` ;;; Create range `{begin, begin+step, begin+step+step, ...,}` in a parameterized gtest. Does *not* include `end`. = #lang/test/gtest/parameterized-tests 
<!--ID: 1758253289851-->

  `Range(begin, end, [,step])` ;;; Create range `{begin, begin+step, begin+step+step, ...,}` in a parameterized gtest. Does *not* include `end`. = #lang/test/gtest/parameterized-tests 
  `Bool(v1, v2, ..., vN)` ;;; Create sequence `{false, true}`. Defined in the `::testing` namespace. = #lang/test/gtest/parameterized-tests 
<!--ID: 1758253289860-->

  `Combine(g1, g2, ..., gN)` ;;; Create `std::tuple` `n`-tuples  sequence `{false, true}`. Defined in the `::testing` namespace. = #lang/test/gtest/parameterized-tests 
<!--ID: 1758253289866-->

  `ConvertGenerator<T>(g)` ;;; Convert generator `g`, using a `static_cast` (behind the scenes) to convert from `T`. = #lang/test/gtest/parameterized-tests  
<!--ID: 1758253289873-->


## Examples
### Footest to test multiple parameters
```cpp
class FooTest :
    public testing::TestWithParam<absl::string_view> {
  // You can implement all the usual fixture class members here.
  // To access the test parameter, call GetParam() from class
  // TestWithParam<T>.
};

// Or, when you want to add parameters to a pre-existing fixture class:
class BaseTest : public testing::Test {
  ...
};
class BarTest : public BaseTest,
                public testing::WithParamInterface<absl::string_view> {
  ...
};
```

Then, use the `TEST_P` macro to define as many test patterns using this fixture as you want. The `_P` suffix is for “parameterized” or “pattern”, whichever you prefer to think.

```cpp
TEST_P(FooTest, DoesBlah) {
  // Inside a test, access the test parameter with the GetParam() method
  // of the TestWithParam<T> class:
  EXPECT_TRUE(foo.Blah(GetParam()));
  ...
}

TEST_P(FooTest, HasBlahBlah) {
  ...
}


//Instantaite 
```

```
- `MeenyMinyMoe/FooTest.DoesBlah/0` for `"meeny"`
- `MeenyMinyMoe/FooTest.DoesBlah/1` for `"miny"`
- `MeenyMinyMoe/FooTest.DoesBlah/2` for `"moe"`
- `MeenyMinyMoe/FooTest.HasBlahBlah/0` for `"meeny"`
- `MeenyMinyMoe/FooTest.HasBlahBlah/1` for `"miny"`
- `MeenyMinyMoe/FooTest.HasBlahBlah/2` for `"moe"`
```
