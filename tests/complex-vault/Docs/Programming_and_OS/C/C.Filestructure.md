---
type: note
---
# Common Organization Patterns

``` C
project_name/
├── include/
│   └── project_name/
│       └── public_header_files.h
├── src/
│   ├── private_source_files.c
│   └── main.c (optional - the entry point of the program)
├── interface/ (Optional - Contains external APIs, bindings, etc.)
│   └── external_api.h
├── build/ (Optional - Created during build)
├── bin/   (Optional - Created during build)
├── tests/ (Optional - Test-related files)
│   ├── unit/
│   │   └── unit_test_files.c
│   ├── integration/
│   │   └── integration_test_files.c
│   └── test_data/
├── docs/ (Optional - Documentation files)
│   ├── user_guide.md
│   └── developer_guide.md
├── examples/ (Optional - Example code demonstrating usage)
│   └── example_usage.c
├── resources/ (Optional - Additional project resources)
└── README.md


```

## Explanation

- **include/:** This directory contains header files (.h) that define the public interface of the project. Header files declare functions, data structures, and constants that other parts of the program can use to interact with the project's functionality.
- **src/:** This directory contains the source files (.c) that implement the functionality defined in the header files. It houses the actual code that makes up the project's logic.
- **build/ (Optional):** This directory is created during the build process and contains intermediate build artifacts, such as object files (.o), generated during compilation. It's a good practice to keep build artifacts separate from the source code to avoid cluttering the main project directory.
- **bin/ (Optional):** If the project generates executable files, this directory is created during the build process to hold the resulting binary/executable files.
- **tests/ (Optional):** If the project includes test files, this directory contains test-related code and data. It's common to have separate folders for unit tests, integration tests, and other test resources.
- **README.md:** A documentation file that provides information about the project, its purpose, usage, and any other relevant details. It serves as a useful reference for developers and users.
- **interface/ (Optional):** If the project involves providing external APIs, bindings for other languages, or any interfaces intended for external use, this folder can house the necessary header files or interface definitions.
- **tests/:** This directory is for housing various types of tests for the project. It may include folders for unit tests, integration tests, and any test data required for testing purposes.
- **docs/ (Optional):** If your project includes documentation, this folder can contain user guides, developer guides, or any other relevant documentation files.
- **examples/ (Optional):** This folder can include example code that demonstrates how to use the project's features and functionality. Providing examples can make it easier for users to understand and adopt your project.
- **resources/ (Optional):** If your project requires additional resources, such as configuration files, data files, or assets, you can place them in this folder.

This more complete organization pattern is suitable for larger and more complex C projects, as it provides a well-structured and organized layout for different types of project files and resources. As always, the specific structure may vary based on the project's needs and the preferred development practices of the team or organization.