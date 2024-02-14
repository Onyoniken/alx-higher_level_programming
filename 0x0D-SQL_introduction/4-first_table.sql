-- creates table with a name first_table in mysql database
-- database name is passed as an argument
-- first_table description
-- if table first_table exsists, script shouldn't fail
-- don't use select or show statements

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
