--display max temp of each state (order follows state name)

SELECT state, MAX(value) as max_temp FROM temperatures GROUP BY state ORDER BY state;
