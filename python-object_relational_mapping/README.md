# Python - Object-relational mapping

This directory contains my solutions for the Holberton School project
**"Python - Object-relational mapping"**.

The goal of this project is to link Databases and Python. In the first part,
I used the module `MySQLdb` to connect to a MySQL database and execute SQL queries.
In the second part, I used `SQLAlchemy`, an Object Relational Mapper (ORM), to
abstract the storage and interact with the database using Python objects instead
of SQL queries.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3` (version 3.8.5)
- Database: MySQL 8.0
- MySQLdb version: 2.0.x
- SQLAlchemy version: 1.4.x
- Style: `pycodestyle` (version 2.7.*)
- All files must be executable
- All files must end with a new line
- The first line of all files must be exactly `#!/usr/bin/python3`
- A `README.md` file at the root of the project folder is mandatory
- All modules, classes, and functions must be properly documented

## Tasks / Files

- `0-select_states.py`
  Script that lists all states from the database `hbtn_0e_0_usa`.
- `1-filter_states.py`
  Script that lists all states with a name starting with N (upper N).
- `2-my_filter_states.py`
  Script that takes in an argument and displays all values in the `states` table where `name` matches the argument.
- `3-my_safe_filter_states.py`
  Script that takes in arguments and displays all values in the `states` table, safe from MySQL injections.
- `4-cities_by_state.py`
  Script that lists all cities from the database `hbtn_0e_4_usa`.
- `5-filter_cities.py`
  Script that takes in the name of a state as an argument and lists all cities of that state.
- `model_state.py`
  Python file that contains the class definition of a `State` and an instance `Base = declarative_base()`.
- `7-model_state_fetch_all.py`
  Script that lists all `State` objects from the database `hbtn_0e_6_usa` via SQLAlchemy.
- `8-model_state_fetch_first.py`
  Script that prints the first `State` object from the database `hbtn_0e_6_usa`.
- `9-model_state_filter_a.py`
  Script that lists all `State` objects that contain the letter `a` from the database `hbtn_0e_6_usa`.
- `10-model_state_my_get.py`
  Script that prints the `State` object with the `name` passed as argument.
- `11-model_state_insert.py`
  Script that adds the `State` object "Louisiana" to the database `hbtn_0e_6_usa`.
- `12-model_state_update_id_2.py`
  Script that changes the name of a `State` object in the database.
- `13-model_state_delete_a.py`
  Script that deletes all `State` objects with a name containing the letter `a`.
- `model_city.py` & `14-model_city_fetch_by_state.py`
  Contains the class definition of a `City` and a script that prints all `City` objects by state.

*(Note: Assumed standard Holberton filenames for tasks 1-14 based on the task descriptions).*

## Usage

Example of running `0-select_states.py`:

```bash
./0-select_states.py root root hbtn_0e_0_usa
```

## Author

Aliyyiakbar Shirinli
