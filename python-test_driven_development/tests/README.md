# Tests

This directory contains test cases for the Holberton School project
**"Python - Test-driven development"**.

The goal of this folder is to store doctest files used to check Python
functions through examples written in text files. These tests help verify
normal cases, edge cases, invalid input, and expected error messages before
or while writing the actual implementation.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3` (version 3.8.*)
- Test framework: `doctest`
- All test files must be inside this `tests` folder
- All test files must be text files with the `.txt` extension
- All files must end with a new line
- Tests should be executed from the project directory
- Each module and function tested must include proper documentation

## Test Files

- `0-add_integer.txt`  
  Tests integer addition, float casting, missing arguments, invalid types,
  and edge cases for `0-add_integer.py`.

- `2-matrix_divided.txt`  
  Tests matrix division, invalid matrix values, invalid divisor values,
  zero division, and correct rounding behavior for `2-matrix_divided.py`.

- `3-say_my_name.txt`  
  Tests name printing, missing arguments, empty strings, and invalid name
  types for `3-say_my_name.py`.

- `4-print_square.txt`  
  Tests square printing with `#`, zero size, invalid size types, and negative
  values for `4-print_square.py`.

- `5-text_indentation.txt`  
  Tests text indentation after `.`, `?`, and `:`, including invalid input
  and spacing behavior for `5-text_indentation.py`.

- `100-matrix_mul.txt`  
  Tests matrix multiplication, invalid matrix formats, empty matrices,
  incompatible matrix sizes, and valid multiplication cases for
  `100-matrix_mul.py`.

- `101-lazy_matrix_mul.txt`  
  Tests matrix multiplication using NumPy for `101-lazy_matrix_mul.py`.

## Usage

Run all doctests from the `python-test_driven_development` directory:

```bash
python3 -m doctest ./tests/*
```

Run one specific test file:

```bash
python3 -m doctest -v ./tests/0-add_integer.txt
```

## Example Test Format

```text
>>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
```

## Author

Aliyyiakbar Shirinli
