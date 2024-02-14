-- list records of second_table of hbtn_0c_0
-- rows shouldnt be listed without name value
-- result to display score and name
-- records to be listed by descending score
-- database to be passed as arg to mysql

SELECT score, name FROM second_table WHERE name IS NOT NULL AND name != '' ORDER BY score DESC;
