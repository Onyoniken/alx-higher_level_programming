--list records with same number of scores in second_table of hbtn_0c_0 in mysql
--records to display: score & number of individuals
--list to be sorted by no of records in descending order
--database name to be passed as an argument to mysql

SELECT score, COUNT(*) as number FROM second_table GROUP BY score ORDER BY number DESC;
