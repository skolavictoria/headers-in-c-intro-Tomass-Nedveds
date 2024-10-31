
# Headers in C - Introduction

## Overview
This module introduces the concept of header files in C programming. Header files are a crucial component of C programs, especially when dealing with large projects. They provide a way to separate the definition of a function from its implementation, allowing for better organization and code management.

## Description
In C, header files typically have a `.h` extension and contain function prototypes, macro definitions, and structures. They act as an interface to the corresponding source files, which contain the actual code definitions.

## Importance of Header Files
- **Modularity**: Header files enable a modular programming approach, allowing for separate compilation of source files.
- **Reusability**: Functions defined in one file can be easily used in other files through the inclusion of header files.
- **Maintainability**: Separating declarations from implementations makes the code easier to navigate and maintain.
- **Scalability**: For large projects, headers provide a way to scale the codebase in an organized manner.

## Basic Usage
To use a header file, you must include it in your C source file using the `#include` preprocessor directive. There are two types of includes:
- `#include <filename>`: Used for standard library header files.
- `#include "filename"`: Used for user-defined header files.

## Header Guards
Header files should have header guards to prevent double inclusion, which can cause errors. Header guards are typically implemented using preprocessor directives:
```c
#ifndef HEADER_FILE_NAME_H
#define HEADER_FILE_NAME_H

// Declarations

#endif // HEADER_FILE_NAME_H
```

## Task Details and Output Specifications

### Task 1: Single Header Inclusion
**Objective**: Create a header file and include it in your main program file.

- **File Organization**: Place all files for this task in a folder named `Task1`.
- **Requirements**:
  - Create a header file `greetings.h` that declares a function `void say_hello(void);`.
  - Implement `say_hello` in `greetings.c` to print the exact output: `Hello, World!\n`
  - In `main.c`, include `greetings.h` and call `say_hello`.

- **Executable**: Name the executable `hello`.
- **Expected Output**:
  ```plaintext
  Hello, World!
  ```

### Task 2: Multiple Header Inclusions
**Objective**: Create multiple header files and include them in a single main program file.

- **File Organization**: Place all files for this task in a folder named `Task2`.
- **Requirements**:
  - Create two header files, `math_operations.h` and `print_operations.h`.
    - `math_operations.h` should declare functions: `int add(int a, int b);`, `int subtract(int a, int b);`, `int divide(int a, int b);`, `int multiply(int a, int b);`.
    - `print_operations.h` should declare `void print_result(int result);`.
  - Implement the functions in `math_operations.c` and `print_operations.c`.
  - In `main.c`, include both headers and:
    - Call `add(10, 5)`, store the result, and pass it to `print_result`.

- **Executable**: Name the executable `math_printer`.
- **Expected Output**:
  ```plaintext
  Result: 15
  ```

### Task 3: Nested Header Inclusions
**Objective**: Create a nested header inclusion scenario where one header file includes another.

- **File Organization**: Place all files for this task in a folder named `Task3`.
- **Requirements**:
  - Create a header file `array_utils.h` that declares `void fill_array(int* array, int size, int value);`.
  - Create another header file `utils.h` that includes `array_utils.h` and declares `void print_array(int* array, int size);`.
  - Implement these functions in `array_utils.c` and `utils.c`.
  - In `main.c`, include only `utils.h` and:
    - Create an array of five elements.
    - Use `fill_array` to populate the array with `3` and `print_array` to display the contents.

- **Executable**: Name the executable `array_util_demo`.
- **Expected Output**:
  ```plaintext
  3 3 3 3 3 
  ```

## Resources
- C Programming Language
- Organizing Code Files in C and C++
- Header Files in C

## Conclusion
Mastering the use of header files is an essential skill for any C programmer. It enhances code organization, maintainability, and scalability, making it easier to manage large and complex codebases. By following best practices and completing tasks on single, multiple, and nested header inclusions, you will develop a deeper understanding of creating efficient and organized C programs.
