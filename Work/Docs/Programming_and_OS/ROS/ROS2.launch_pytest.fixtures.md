---
tags: note/ROS
type: note
---
# Background
The launch_pytest plugin will:
1. Launch the nodes found in the `launch_description` fixture
2. Run the tests from the `test_read_stdout()` class, 
3. Run the statements after the `yield` statement in `test_read_stdout()`

A `@launch_pytest.fixture` function should return a `launch.LaunchDescription` object, or a sequence of objects whose first item is a `launch.LaunchDescription`. 
- The `launch.LaunchDescription` will be used in all tests with a mark `@pytest.mark.launch(fixture=<your_fixture_name>)`
- It can also include a `ReadyToTest` action signal to the rest of the test framework signalling that it is safe to start the active tests. 

## Example
```python
@launch_pytest.fixture
def launch_description(hello_world_proc):
    """Launch a simple process to print 'hello_world'."""
    return launch.LaunchDescription([
        hello_world_proc,
        # Tell launch when to start the test
        # If no ReadyToTest action is added, one will be appended automatically.
        launch_pytest.actions.ReadyToTest()
    ])
```

# Scope
Fixtures can have `module`, `class`, or `function` scope. Default is `function`. 
## Example code to be referenced
```python
@launch_pytest.fixture(scope=my_scope)
def my_fixture():
    return LaunchDescription(...)

@pytest.mark.launch(fixture=my_fixture)
def test_case_1():
    pass

@pytest.mark.launch(fixture=my_fixture)
def test_case_2():
    pass
```

### Function Scope
If `my_scope=function`, the following happens:
- A launch service using the `LaunchDescription` returned by `my_fixture()` is started.
- `test_case_1()` is run.
- The launch service is shutdown.
- Another launch service using the `LaunchDescription` returned by `my_fixture()` is started, `my_fixture()` is called again.
- `test_case_2()` is run.
- The launch service is shutdown.
### Module Scope
Whereas when `my_scope=module`, `test case_2()` will run immediately after `test case_1()`, concurrently with the same launch service.

It's not recommended to mix fixtures with `module` scope with fixtures of `class`/`function` scope in the same file. It's not recommended to use fixtures with scope larger than `module`. A test shouldn't depend on more than one `launch_pytest` fixture. Neither of the three things above automatically generates an error in the current `launch_pytest` implementation, but future versions might.