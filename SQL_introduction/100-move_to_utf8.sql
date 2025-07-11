-- Converts hbtn_0c_0 database to UTF8 (utf8mb4, collate utf8mb4_unicode_ci) in your MySQL server

-- Converts the database to UTF
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8
COLLATE utf8mb4_unicode_ci;

-- Selects a database to use
USE hbtn_0c_0;

-- Converts the table to UTF
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8
COLLATE utf8mb4_unicode_ci;

-- Converts the 'name' column to UTF
ALTER TABLE first_table
MODIFY name VARCHAR(256)
CHARACTER SET utf8
COLLATE utf8mb4_unicode_ci;