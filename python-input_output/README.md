# Python - Input/Output

This directory contains my solutions for the Holberton School project
**"Python - Input/Output"**.

The goal of this project is to practice reading and writing files in Python,
working with the `with` statement, handling text files, using JSON, converting
Python objects to JSON strings, converting JSON strings back to Python objects,
and using command-line arguments.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3` (version 3.8.*)
- Style: `pycodestyle` (version 2.7.*)
- All files must be executable
- All files must end with a new line
- The first line of all Python files must be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of this project folder is mandatory
- File length will be tested using `wc`
- All modules, classes, and functions must include proper documentation
- Test files, when required, must be inside the `tests` folder
- Test files must use the `.txt` extension
- Tests must be executed with `python3 -m doctest ./tests/*`

## Learning Objectives

By the end of this project, I should be able to explain:

- How to open a file
- How to write text into a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor inside a file
- How to make sure a file is closed after use
- How to use the `with` statement
- What JSON is
- What serialization is
- What deserialization is
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
- How to use command-line parameters in a Python script

## Files

- `0-read_file.py`  
  Reads a UTF-8 text file and prints its content to standard output.

- `1-write_file.py`  
  Writes a string to a UTF-8 text file and returns the number of characters written.

- `2-append_write.py`  
  Appends a string to the end of a UTF-8 text file and returns the number of characters added.

- `3-to_json_string.py`  
  Converts a Python object into a JSON string.

- `4-from_json_string.py`  
  Converts a JSON string into a Python object.

- `5-save_to_json_file.py`  
  Saves a Python object to a text file using JSON representation.

- `6-load_from_json_file.py`  
  Creates a Python object from a JSON file.

- `7-add_item.py`  
  Adds command-line arguments to a Python list and saves the list to a JSON file.

- `8-class_to_json.py`  
  Returns the dictionary description of an object for JSON serialization.

- `9-student.py`  
  Defines a `Student` class and retrieves its dictionary representation.

- `10-student.py`  
  Improves the `Student` class by allowing filtered dictionary retrieval.

- `11-student.py`  
  Adds the ability to reload a `Student` instance from a JSON dictionary.

- `12-pascal_triangle.py`  
  Returns a list of lists representing Pascal's Triangle.

## Usage

Example for reading a file:

```bash
chmod +x 0-main.py
./0-main.py
```

Example for running doctests:

```bash
python3 -m doctest ./tests/*
```

## Author

Aliyyiakbar Shirinli
