# MySQL Basics

This README provides a brief overview of essential MySQL concepts and operations.

## Creating a New MySQL User

To create a new MySQL user, you can use the `CREATE USER` statement followed by the username and identified by a password. For example:

```sql
CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
Managing Privileges for a User
You can manage privileges for a user using the GRANT and REVOKE statements. GRANT gives privileges to users, while REVOKE revokes privileges. For example:

sql
Copy code
GRANT ALL PRIVILEGES ON database_name.* TO 'username'@'localhost';
PRIMARY KEY
A PRIMARY KEY is a column or a set of columns that uniquely identifies each row in a table. It ensures that each row in a table is uniquely identified. For example:

sql
Copy code
CREATE TABLE table_name (
    id INT PRIMARY KEY,
    ...
);
FOREIGN KEY
A FOREIGN KEY is a column or a set of columns in one table that points to the PRIMARY KEY in another table. It establishes a relationship between two tables. For example:

sql
Copy code
CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    ...
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
NOT NULL and UNIQUE Constraints
NOT NULL ensures that a column cannot contain NULL values, while UNIQUE ensures that all values in a column are unique. For example:

sql
Copy code
CREATE TABLE table_name (
    column1 INT NOT NULL,
    column2 VARCHAR(50) UNIQUE,
    ...
);
Retrieving Data from Multiple Tables
To retrieve data from multiple tables in one request, you can use JOIN operations. JOINs allow you to combine rows from two or more tables based on a related column between them.

Subqueries
A subquery is a query nested inside another query. It allows you to use the result of one query as a condition in another query. Subqueries can be used in SELECT, INSERT, UPDATE, or DELETE statements.

JOIN and UNION
JOIN is used to combine rows from two or more tables based on a related column between them. UNION is used to combine the results of two or more SELECT statements into a single result set.

css
Copy code

This README provides a brief overview of key MySQL concepts and operations. Each sect
