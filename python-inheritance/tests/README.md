# Tests

This directory contains doctest files for the Holberton School project
**"Python - Inheritance"**.

The goal of this folder is to store text-based test cases used to check the
behavior of modules, functions, and classes related to inheritance,
object validation, subclass behavior, and method overriding.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3` (version 3.8.*)
- Test framework: `doctest`
- All test files must be inside this `tests` folder
- All test files must be text files with the `.txt` extension
- All files must end with a new line
- Tests must be executed from the `python-inheritance` directory
- Modules, classes, and functions tested must include proper documentation

## Test Files

- `1-my_list.txt`  
  Tests the `MyList` class and its sorted printing behavior.

- `7-base_geometry.txt`  
  Tests integer validation and error handling in `BaseGeometry`.

## Usage

Run all doctests:

```bash
python3 -m doctest ./tests/*
```

Run one specific doctest file:

```bash
python3 -m doctest -v ./tests/7-base_geometry.txt
```

## Example Test Format

```text
>>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
>>> bg = BaseGeometry()
>>> bg.integer_validator("width", 10)
>>> bg.integer_validator("width", -1)
Traceback (most recent call last):
...
ValueError: width must be greater than 0
```

## Author

Aliyyiakbar Shirinli
