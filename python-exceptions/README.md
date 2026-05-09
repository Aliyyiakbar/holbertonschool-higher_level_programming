# Python - Exceptions

This directory contains my solutions for the Holberton School project
**"Python - Exceptions"**.

The goal of this project is to practice Python errors and exceptions, including
safe printing, handling invalid values, raising exceptions, and using cleanup
logic after an exception.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3` (version 3.8.5)
- Style: `pycodestyle` (version 2.7.*)
- All files must be executable
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of this project folder is mandatory
- File length will be tested using `wc`
- No modules may be imported unless the task allows it

## Files

- `0-safe_print_list.py`  
  Prints a specific number of elements from a list safely.

- `1-safe_print_integer.py`  
  Prints an integer safely using string formatting.

- `2-safe_print_list_integers.py`  
  Prints only the integer values from a list.

- `3-safe_print_division.py`  
  Divides two integers and prints the result in a cleanup block.

- `4-list_division.py`  
  Divides two lists element by element while handling errors.

- `5-raise_exception.py`  
  Raises a type exception.

- `6-raise_exception_msg.py`  
  Raises a name exception with a custom message.

- `100-safe_print_integer_err.py`  
  Prints an integer safely and writes the error message to `stderr` when needed.

- `101-safe_function.py`  
  Executes a function safely and prints errors to `stderr`.

- `102-magic_calculation.py`  
  Recreates the behavior of a given Python bytecode operation.

## Usage

Example:

```bash
chmod +x 0-safe_print_list.py
./0-main.py
```

## Author

Aliyyiakbar Shirinli
