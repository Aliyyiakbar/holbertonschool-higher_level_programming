# Python - Import & Modules

This directory contains my solutions for the Holberton School project
**"Python - Import & Modules"**.

The goal of this project is to practice importing functions from other files,
creating modules, using imported functions, protecting code from execution when
imported, and working with command-line arguments.

## Requirements

- OS: Ubuntu 22.04 LTS
- Interpreter: `python3` (version 3.10.*)
- Style: `pycodestyle` (version 2.7.*)
- All files must be executable
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of this project folder is mandatory
- File length will be tested using `wc`
- No wildcard imports are allowed where restricted by the task

## Files

- `0-add.py`  
  Imports the function `add` from `add_0.py` and prints the result of `1 + 2`.

- `1-calculation.py`  
  Imports calculator functions and prints addition, subtraction, multiplication,
  and division results.

- `2-args.py`  
  Prints the number of command-line arguments and lists each argument.

- `3-infinite_add.py`  
  Adds all command-line arguments and prints the total.

- `4-hidden_discovery.py`  
  Prints all names defined by a compiled module, except names starting with `__`.

- `5-variable_load.py`  
  Imports a variable from another file and prints its value.

- `100-my_calculator.py`  
  Builds a command-line calculator that supports addition, subtraction,
  multiplication, and division.

- `101-easy_print.py`  
  Prints `#pythoniscool` using a restricted number of lines.

- `102-magic_calculation.py`  
  Recreates the behavior of a given Python bytecode operation.

- `103-fast_alphabet.py`  
  Prints the uppercase alphabet using a compact Python expression.

## Usage

Example:

```bash
chmod +x 0-add.py
./0-add.py
```

## Author

Aliyyiakbar Shirinli
