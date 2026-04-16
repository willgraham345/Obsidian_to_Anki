---
type: note
---
# Example
```c
/**
 * @file myclass.h
 * @brief Header file for MyClass class.
 */

/**
 * @class MyClass
 * @brief A simple class for demonstration.
 */
class MyClass {
public:
    /**
     * @brief Constructor for MyClass.
     * @param value An integer value to initialize the object.
     */
    MyClass(int value);

    /**
     * @brief Destructor for MyClass.
     */
    ~MyClass();

    /**
     * @brief A member function that performs an operation.
     * 
     * This function performs a simple operation and returns the result.
     * @param x An input integer.
     * @param y An input integer.
     * @return The result of the operation.
     */
    int PerformOperation(int x, int y);

private:
    int data_; /**< An integer member variable. */
};

```