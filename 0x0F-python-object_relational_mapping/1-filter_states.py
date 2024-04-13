#!/usr/bin/python3

import MySQLdb
import sys


def my_city(mysql_username, mysql_password, database_name):
    connection = MySQLdb.connect(
            user=mysql_username,
            passwd=mysql_password,
            host="localhost",
            port=3306,
            db=database_name
            )

    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id ASC"

    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()

if __name__ == "__main__":

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    my_city(mysql_username, mysql_password, database_name)
