--  script that lists all records of the table second_table of the database
SELECT `name`, `score`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC;
