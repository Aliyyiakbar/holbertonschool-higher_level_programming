-- Convert hbtn_0c_0 database, first_table and name field to UTF8
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert first_table default charset to UTF8
ALTER TABLE hbtn_0c_0.first_table
DEFAULT CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Convert name field to UTF8
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256)
COLLATE utf8mb4_unicode_ci
DEFAULT NULL;
