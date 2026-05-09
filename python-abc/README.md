# Python - Abstract Classes and Interfaces

This directory contains my solutions for the Holberton School project
**"Python - Abstract Classes and Interfaces"**.

The goal of this project is to practice advanced object-oriented programming
concepts in Python, including abstract classes, interfaces, duck typing,
subclassing built-in classes, method overriding, iterators, multiple
inheritance, and mixins.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3`
- All files must be executable
- All files must end with a new line
- The first line of all Python files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of this project folder is mandatory
- Code should be clear, readable, and follow Python style conventions
- No unnecessary imports should be used

## Learning Objectives

By the end of this project, I should be able to explain:

- What abstract classes are
- How to use the `abc` module
- How to create abstract methods
- How subclasses implement abstract methods
- What interfaces are in Python
- What duck typing means
- How to subclass standard base classes
- How to override inherited methods
- How to create and use custom iterators
- How multiple inheritance works
- How mixins help share behavior between classes

## Files

- `task_00_abc.py`  
  Defines an abstract class `Animal` with an abstract method `sound`.
  Also defines `Dog` and `Cat` subclasses that return `"Bark"` and `"Meow"`.

- `task_01_duck_typing.py`  
  Defines shape classes using duck typing and a common interface for area
  and perimeter behavior.

- `task_02_verboselist.py`  
  Defines a custom list class that extends Python's built-in `list` and
  prints notifications when items are added or removed.

- `task_03_countediterator.py`  
  Defines a custom iterator that keeps track of how many items have been
  iterated over.

- `task_04_flyingfish.py`  
  Demonstrates multiple inheritance through a `FlyingFish` class that combines
  behavior from different parent classes.

- `task_05_dragon.py`  
  Demonstrates mixins by creating a `Dragon` class with shared flying and
  swimming behavior.

## Usage

Run a main file:

```bash
chmod +x main_00_abc.py
./main_00_abc.py
```

Example for task 0:

```python
#!/usr/bin/env python3
from task_00_abc import Animal, Dog, Cat

bobby = Dog()
garfield = Cat()

print(bobby.sound())
print(garfield.sound())
```

Expected output:

```text
Bark
Meow
```

Trying to instantiate the abstract class directly should raise a `TypeError`:

```python
animal = Animal()
```

## Author

Aliyyiakbar Shirinli
