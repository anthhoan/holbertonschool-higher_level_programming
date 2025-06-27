-- Create the MySQL server user user_0d_1
IF NOT EXIST 
CREATE USER 'user_0d_1'@'localhost' 
IDENTIFIED BY 'user_0d_1';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD on *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;