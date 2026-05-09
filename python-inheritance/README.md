# Python - Inheritance

This directory contains my solutions for the Holberton School project
**"Python - Inheritance"**.

The goal of this project is to practice inheritance in Python, including
parent classes, subclasses, method overriding, object type checking, inherited
attributes and methods, and the use of built-in functions such as `isinstance`,
`issubclass`, `type`, and `super`.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3` (version 3.8.*)
- Style: `pycodestyle` (version 2.7.*)
- All files must be executable
- All files must end with a new line
- The first line of all Python files must be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the repository is mandatory
- A `README.md` file at the root of this project folder is mandatory
- File length will be tested using `wc`
- All modules, classes, and functions must include proper documentation
- Test files must be inside the `tests` folder
- Test files must use the `.txt` extension
- Tests must be executed with `python3 -m doctest ./tests/*`

## Learning Objectives

By the end of this project, I should be able to explain:

- What a superclass, base class, or parent class is
- What a subclass is
- How to list all attributes and methods of a class or instance
- When an instance can have new attributes
- How to inherit from another class
- How to use multiple inheritance
- What class every Python class inherits from by default
- How to override inherited methods and attributes
- Which attributes and methods are inherited by subclasses
- The purpose of inheritance
- How to use `isinstance`, `issubclass`, `type`, and `super`

## Files

- `0-lookup.py`  
  Returns the list of available attributes and methods of an object.

- `1-my_list.py`  
  Defines a class `MyList` that inherits from `list` and prints the list sorted.

- `2-is_same_class.py`  
  Checks whether an object is exactly an instance of a specified class.

- `3-is_kind_of_class.py`  
  Checks whether an object is an instance of, or inherited from, a specified class.

- `4-inherits_from.py`  
  Checks whether an object is an instance of a class that inherited from a specified class.

- `5-base_geometry.py`  
  Defines an empty class `BaseGeometry`.

- `6-base_geometry.py`  
  Defines `BaseGeometry` with an `area()` method that raises an exception.

- `7-base_geometry.py`  
  Adds integer validation to `BaseGeometry`.

- `8-rectangle.py`  
  Defines a `Rectangle` class that inherits from `BaseGeometry`.

- `9-rectangle.py`  
  Improves `Rectangle` by adding area calculation and string representation.

- `10-square.py`  
  Defines a `Square` class that inherits from `Rectangle`.

- `11-square.py`  
  Improves `Square` by adding a custom string representation.

- `100-my_int.py`  
  Defines a rebel integer class `MyInt` that inverts equality and inequality.

- `101-add_attribute.py`  
  Adds a new attribute to an object when possible.

## Tests

Doctest files are stored in the `tests` directory.

Run all tests from the `python-inheritance` directory:

```bash
python3 -m doctest ./tests/*
```

Run one specific test file:

```bash
python3 -m doctest -v ./tests/1-my_list.txt
```

## Usage

Example:

```bash
chmod +x 0-lookup.py
./0-main.py
```

## Author

Aliyyiakbar Shirinli
