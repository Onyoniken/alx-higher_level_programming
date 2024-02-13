--list records with scores >= 10 in second_table of hbtn_0c_0 in mysql
--results should have name and score
--results should be ordered, starting with the first
--database is passed as an arg of mysql

SELECT score, name FROM second_table WHERE score >= 10 ORDERED BY score DESC;

