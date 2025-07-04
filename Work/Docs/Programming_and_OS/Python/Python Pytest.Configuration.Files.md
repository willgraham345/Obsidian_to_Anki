---
tags: note/python
type: note
---
# Configuration Files
Similar functions, and choice depends on your preference. 
## pytest.ini
- **Function:** `pytest.ini` is a configuration file that allows you to customize the behavior of pytest for your project.
- **Usage:** You can use this file to set various options and configure pytest according to your project's requirements. For example, you can define test markers, set command line options, specify custom test discovery rules, etc.
- **Location:** The file is typically placed in the root of your project.

### Example `pytest.ini` file:
```ini
[pytest]
addopts = -rsxX
markers =    
	slow: marks tests as slow
	integration: marks tests as integration tests`
```
- In this example, it specifies additional command line options (`-rsxX`) and defines two custom markers (`slow` and `integration`).
## pyproject.toml
- **Function:** `pyproject.toml` is a configuration file for Python projects. It is not specific to pytest but is part of the broader Python tooling ecosystem.
- **Usage:** It is used to define project metadata, build system configuration, and various tool configurations, including testing tools like pytest.
- **Location:** It is usually placed in the root of your project.

```toml
[tool.pytest]
addopts = "-rsxX"
markers = ["slow", "integration"]
```
This example achieves similar functionality as the `pytest.ini` example. The `[tool.pytest]` section is used to configure pytest settings.