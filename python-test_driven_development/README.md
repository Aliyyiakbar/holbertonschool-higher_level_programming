# Python - Test-driven Development

This directory contains my solutions for the Holberton School project
**"Python - Test-driven Development"**.

The goal of this project is to practice writing documentation and tests before
implementation. It focuses on doctests, unit tests, module documentation,
function documentation, and edge-case handling.

## Requirements

### Python Scripts

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3` (version 3.8.5)
- Style: `pycodestyle` (version 2.7.*)
- All files must be executable
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- All modules must have documentation
- All functions must have documentation
- A `README.md` file at the root of this project folder is mandatory

### Python Test Cases

- All test files must be inside the `tests` folder
- All test files must be text files with the `.txt` extension when using doctest
- Tests must be executable with `python3 -m doctest ./tests/*`
- Unit tests must be executable with `python3 -m unittest`

## Files

- `0-add_integer.py`  
  Adds two integers and handles float casting.

- `tests/0-add_integer.txt`  
  Doctests for integer addition.

- `2-matrix_divided.py`  
  Divides all elements of a matrix by a number.

- `tests/2-matrix_divided.txt`  
  Doctests for matrix division.

- `3-say_my_name.py`  
  Prints a full name using first name and last name values.

- `tests/3-say_my_name.txt`  
  Doctests for name printing.

- `4-print_square.py`  
  Prints a square using the `#` character.

- `tests/4-print_square.txt`  
  Doctests for square printing.

- `5-text_indentation.py`  
  Prints text with two new lines after `.`, `?`, and `:` characters.

- `tests/5-text_indentation.txt`  
  Doctests for text indentation.

- `6-max_integer.py`  
  Finds the maximum integer in a list.

- `tests/6-max_integer_test.py`  
  Unit tests for the max integer function.

- `100-matrix_mul.py`  
  Multiplies two matrices with full validation.

- `tests/100-matrix_mul.txt`  
  Doctests for matrix multiplication.

- `101-lazy_matrix_mul.py`  
  Multiplies two matrices using NumPy.

- `tests/101-lazy_matrix_mul.txt`  
  Doctests for lazy matrix multiplication.

## Usage

Example:

```bash
python3 -m doctest ./tests/*
python3 -m unittest tests.6-max_integer_test
```

## Author

Aliyyiakbar Shirinli
