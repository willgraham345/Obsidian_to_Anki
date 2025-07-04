---
tags: note/python
type: note
---
# Modifying Python's traceback printing


| Command                               | Description                                       |
| ------------------------------------- | ------------------------------------------------- |
| `pytest -v`                           | Verbose mode, provides more details on test runs. |
| `pytest --show-capture=stdout`        | Show captured stdout output during test runs.    |
| `pytest --capture=tee-sys`            | Tee system stdout/stderr to the terminal.         |
| `pytest -rs`                          | Report details on skipped tests.                  |
| `pytest --durations=3`                | Display the top 3 slowest test durations.        |
| `pytest --junitxml=path/to/report.xml`| Generate JUnit-style XML report for CI tools.     |
| `pytest --cov=your_module`            | Measure test coverage for your code.              |

# Display Print Outputs
```bash
pytest -s
```

# Capture Warnings
Starting in 3.1, pytest automatically catches warnings during test execution and displays them at the end of the session.

## Display All Warnings
```shell
pytest -W always
```


## Display a Specific Warning
```shell
pytest -W error::UserWarning
```
- Shows which warnings are ignored, displayed or turned into errors
- The same option can be set in the `pytest.ini` or `pyproject.toml` file
```python
# pytest.ini
[pytest]
filterwarnings =
    error
    ignore::UserWarning
    ignore:function ham\(\) is deprecated:DeprecationWarning
```