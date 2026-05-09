# Python - Serialization

This directory contains my solutions for the Holberton School project
**"Python - Serialization"**.

The goal of this project is to practice serialization and marshaling in Python.
It covers converting Python data into formats that can be saved, transferred,
and later restored, using formats such as JSON, pickle, CSV, and XML.

## Requirements

- OS: Ubuntu 20.04 LTS
- Interpreter: `python3`
- All files must be executable
- All files must end with a new line
- The first line of all Python files should be exactly `#!/usr/bin/env python3`
- A `README.md` file at the root of this project folder is mandatory
- Code should be clear, readable, and follow Python style conventions

## Learning Objectives

By the end of this project, I should be able to explain:

- What marshaling is
- What serialization is
- The difference between marshaling and serialization
- How to serialize Python data into JSON
- How to deserialize JSON data back into Python objects
- How to use pickle to save and reload custom Python objects
- How to convert CSV data into JSON format
- How to serialize and deserialize data using XML
- How serialized data can be used in files, web applications, databases, and network communication

## Files

- `task_00_basic_serialization.py`  
  Serializes a Python dictionary to a JSON file and deserializes the JSON file
  back into a Python dictionary.

- `task_01_pickle.py`  
  Uses pickle to serialize and deserialize a custom Python class instance.

- `task_02_csv.py`  
  Converts data from a CSV file into JSON format.

- `task_03_xml.py`  
  Serializes and deserializes data using XML.

## Usage

Example for task 0:

```bash
chmod +x task_00_basic_serialization.py
./main_00_basic_serialization.py
```

Example Python usage:

```python
#!/usr/bin/env python3
from task_00_basic_serialization import (
    load_and_deserialize,
    serialize_and_save_to_file
)

data_to_serialize = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

serialize_and_save_to_file(data_to_serialize, "data.json")
deserialized_data = load_and_deserialize("data.json")

print(deserialized_data)
```

Expected output:

```text
{'name': 'John Doe', 'age': 30, 'city': 'New York'}
```

## Author

Aliyyiakbar Shirinli
