# SQL - Introduction

This directory contains my solutions for the Holberton School project
**"SQL - Introduction"**.

The goal of this project is to learn the basics of databases, relational
databases, SQL, and MySQL. It focuses on creating and deleting databases,
creating and altering tables, selecting data, inserting records, updating
records, deleting records, using functions, and working with subqueries.

## Learning Objectives

By the end of this project, I should be able to explain:

- What a database is
- What a relational database is
- What SQL stands for
- What MySQL is
- How to create a database in MySQL
- What DDL and DML stand for
- How to create or alter a table
- How to select data from a table
- How to insert, update, or delete data
- What subqueries are
- How to use MySQL functions

## Requirements

- Allowed editors: `vi`, `vim`, `emacs`
- OS: Ubuntu 22.04 LTS
- Database: MySQL 8.0
- MySQL version: 8.0.25
- All files must end with a new line
- All SQL queries must have a comment just before the query
- All files must start with a comment describing the task
- All SQL keywords must be in uppercase, such as `SELECT`, `WHERE`, and `INSERT`
- A `README.md` file at the root of this project folder is mandatory
- File length may be tested using `wc`

## Files

- `0-list_databases.sql`  
  Lists all databases on the MySQL server.

- `1-create_database_if_missing.sql`  
  Creates the database `hbtn_0c_0` if it does not already exist.

- `2-remove_database.sql`  
  Deletes the database `hbtn_0c_0` if it exists.

- `3-list_tables.sql`  
  Lists all tables of a database.

- `4-first_table.sql`  
  Creates a table called `first_table` with `id` and `name` columns.

- `5-full_table.sql`  
  Prints the full description of the table `first_table`.

- `6-list_values.sql`  
  Lists all rows of the table `first_table`.

- `7-insert_value.sql`  
  Inserts a new row into the table `first_table`.

- `8-count_89.sql`  
  Displays the number of records with `id = 89` in `first_table`.

- `9-full_creation.sql`  
  Creates a table called `second_table` and adds multiple rows.

- `10-top_score.sql`  
  Lists all records of `second_table` ordered by score.

- `11-best_score.sql`  
  Lists records from `second_table` with a score greater than or equal to 10.

- `12-no_cheating.sql`  
  Updates Bob's score in `second_table`.

- `13-change_class.sql`  
  Removes records from `second_table` with a score less than or equal to 5.

- `14-average.sql`  
  Computes the average score of all records in `second_table`.

- `15-groups.sql`  
  Lists the number of records with the same score in `second_table`.

- `16-no_link.sql`  
  Lists records from `second_table` where the name value is not empty.

## Usage

Start the MySQL service:

```bash
service mysql start
