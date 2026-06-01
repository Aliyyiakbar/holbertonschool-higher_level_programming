# SQL - More queries

This directory contains my solutions for the Holberton School project
**"SQL - More queries"**.

The goal of this project is to expand on SQL database management by practicing user privileges, roles, constraints (`NOT NULL`, `UNIQUE`), primary and foreign keys, and various `JOIN` operations (INNER, LEFT, RIGHT, FULL) using MySQL.

## Requirements

- OS: Ubuntu 22.04 LTS
- Database: MySQL 8.0
- Allowed editors: `vi`, `vim`, `emacs`
- All SQL files must end with a new line
- All SQL files must start with a comment describing the task
- All SQL queries must have a comment before the query
- All SQL keywords must be written in uppercase
- A `README.md` file at the root of the project folder is mandatory
- The length of your files will be tested using `wc`

## Files

- `0-privileges.sql`  
  Lists all privileges of the MySQL users `user_0d_1` and `user_0d_2` on your server (in localhost).

- `1-create_user.sql`  
  Creates the MySQL server user `user_0d_1` with all privileges and password `user_0d_1_pwd`.

- `2-create_read_user.sql`  
  Creates the database `hbtn_0d_2` and the user `user_0d_2` with only `SELECT` privilege in the database.

- `3-force_name.sql`  
  Creates the table `force_name` on your MySQL server where the `name` column cannot be null.

- `4-never_empty.sql`  
  Creates the table `id_not_null` where the `id` column has a default value of `1`.

- `5-unique_id.sql`  
  Creates the table `unique_id` with a default and unique `id` value of `1`.

- `6-states.sql`  
  Creates the database `hbtn_0d_usa` and the table `states` (with an auto-generated, unique, non-null primary key).

- `7-cities.sql`  
  Creates the database `hbtn_0d_usa` and the table `cities` containing a foreign key referencing the `states` table.

- `8-cities_of_california_subquery.sql`  
  Lists all the cities of California that can be found in the database `hbtn_0d_usa` using a subquery (without using `JOIN`).

- `9-cities_by_state_join.sql`  
  Lists all cities contained in the database `hbtn_0d_usa` using a `JOIN` to display the city ID, city name, and state name.

- `10-genre_id_by_show.sql`  
  Lists all shows contained in `hbtn_0d_tvshows` that have at least one genre linked.

- `11-genre_id_all_shows.sql`  
  Lists all shows contained in the database `hbtn_0d_tvshows`, displaying `NULL` if a show doesn't have a genre.

- `12-no_genre.sql`  
  Lists all shows contained in `hbtn_0d_tvshows` without a genre linked.

- `13-count_shows_by_genre.sql`  
  Lists all genres from `hbtn_0d_tvshows` and displays the number of shows linked to each.

- `14-my_genres.sql`  
  Lists all genres of the show *Dexter*.

- `15-comedy_only.sql`  
  Lists all Comedy shows in the database `hbtn_0d_tvshows`.

- `16-shows_by_genre.sql`  
  Lists all shows, and all genres linked to that show, from the database `hbtn_0d_tvshows`.

## Usage

You can test your scripts by piping them into the MySQL engine. 

Example of running script `0-privileges.sql`:

```bash
cat 0-privileges.sql | mysql -hlocalhost -uroot -p
```

Example of importing a database dump and running a query against it:

```bash
echo "CREATE DATABASE hbtn_0d_tvshows;" | mysql -uroot -p
curl "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/274/hbtn_0d_tvshows.sql" -s | mysql -uroot -p hbtn_0d_tvshows
cat 10-genre_id_by_show.sql | mysql -uroot -p hbtn_0d_tvshows
```

## Author

Aliyyiakbar Shirinli
