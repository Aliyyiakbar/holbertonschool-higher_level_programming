# RESTful API

This directory contains my solutions for the Holberton School project
**"RESTful API"**.

The goal of this project is to understand how RESTful APIs work, how clients
and servers communicate using HTTP and HTTPS, how to consume APIs from the
command line and with Python, and how to build simple APIs using Python tools
such as `http.server` and Flask.

This project also introduces API security, authentication, and documentation
standards such as OpenAPI.

## Requirements

- Interpreter: `python3` version 3.9
- All files must end with a new line
- All Python scripts should be executable when required
- Code should be clear, readable, and follow Python style conventions
- External libraries should be installed only when required by the task
- API-related files should follow the task instructions carefully

## Learning Objectives

By the end of this project, I should be able to explain:

- What an API is
- What REST means
- How HTTP and HTTPS work
- The difference between common HTTP methods such as `GET`, `POST`, `PUT`, and `DELETE`
- How to consume an API using command-line tools such as `curl`
- How to consume an API using Python
- How to process JSON responses
- How to convert API data into CSV format
- How to build a simple API using Python's `http.server` module
- How to build a simple API using Flask
- How routing works in Flask
- How to return JSON responses from an API
- How authentication and API security work
- Why API documentation matters
- What OpenAPI is used for

## Files

- `task_00_http_https.md`  
  Explains the basics of HTTP and HTTPS, including request methods, status
  codes, headers, and the difference between secure and non-secure connections.

- `task_01_curl.sh`  
  Uses command-line tools such as `curl` to consume data from an API.

- `task_02_requests.py`  
  Uses the `requests` library to fetch posts from JSONPlaceholder, print post
  titles, and save selected post data into a CSV file.

- `task_03_http_server.py`  
  Builds a simple API using Python's built-in `http.server` module.

- `task_04_flask.py`  
  Builds a simple RESTful API using Flask with basic routes and JSON responses.

- `task_05_basic_security.py`  
  Demonstrates API security and authentication techniques.

## Task 2 Summary

The file `task_02_requests.py` contains two main functions:

- `fetch_and_print_posts()`  
  Fetches posts from JSONPlaceholder, prints the response status code, and
  prints the title of each post when the request is successful.

- `fetch_and_save_posts()`  
  Fetches posts from JSONPlaceholder, extracts the `id`, `title`, and `body`
  fields, and saves them into a CSV file named `posts.csv`.

## Usage

Install `requests` if needed:

```bash
pip install requests
```

Run the task 2 main file:

```bash
python3 main_02_requests.py
```

Expected output starts with:

```text
Status Code: 200
sunt aut facere repellat provident occaecati excepturi optio reprehenderit
qui est esse
ea molestias quasi exercitationem repellat qui ipsa sit aut
```

After running `fetch_and_save_posts()`, a file named `posts.csv` should be
created with these columns:

```text
id,title,body
```

## Author

Aliyyiakbar Shirinli
